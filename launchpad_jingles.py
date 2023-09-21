import launchpad_py as launchpad
import pygame

# Create a dictionary to map button numbers to jingle names
jingle_mapping = {
    # Group 1: Short Jingles
    '0,1': 'URY 3 (Dry) [2s].mp3',
    '1,1': 'URY 1 [2s].mp3',
    '2,1': 'URY Whisper 3 (Dry) [2s].mp3',

    # Group 2: Short to Medium Jingles
    '4,1': 'Broadcasting URY [3s].mp3',
    '5,1': 'Broadcasting URY (Dry) [3s].mp3',

    # Group 3: Medium Jingles
    '0,3': 'By Students, For Students 2 [6s].mp3',
    '1,3': 'By Students, For Students 1 (Dry) [7s].mp3',
    '2,3': 'On Air, Online, On Tap [8s].mp3',
    '3,3': 'On Air, Online, On Tap (Jazz) [7s].mp3',
    '4,3': 'On Air, Online, On Tap (Dry) [7s].mp3',
    '5,3': 'Message via the Website [7s].mp3',
    '6,3': 'Message via the Website (Dry) [5s].mp3',
    '7,3': 'University Radio York [6s].mp3',

    # Group 4: Medium to Long Jingles
    '0,5': 'Text Now [5s].mp3',
    '1,5': 'Text Now (Dry) [4s].mp3',
    '2,5': 'Mixcloud [8s].mp3',
    '3,5': 'Spotify [9s].mp3',
    '4,5': 'Join Now 2 [6s].mp3',
    '5,5': 'Join Now 1 [10s].mp3',
    '6,5': 'UoY Student Station 3 [9s].mp3',

    # Group 5: Long Jingles
    '0,7': 'clap - time machine team.mp3',
    '1,7': 'aww - time machine team.mp3',
    '2,7': 'yay - time machine team.mp3',

    # controls
    '8,4': 'hold_mode',
    '8,1': 'stop'
}

controls = ['hold_mode', 'stop']

def get_jingle_name(x, y):
    return jingle_mapping.get(f'{str(x)},{str(y)}', "Button not mapped")

def play_mp3(audio_file_name):
    try:
        pygame.mixer.music.load(f'Jingles/{audio_file_name}')
        pygame.mixer.music.play()
    except pygame.error:
        # pass
        print("Could not load audio file: " + audio_file_name)

def set_lights():
    # Turn on all the buttons that have jingles mapped to them
    lp.Reset()
    for button in jingle_mapping:
        x, y = button.split(',')
        name = jingle_mapping[button]
        if name in controls:
            if name == "hold_mode":
                if button_hold_mode: lp.LedCtrlXY(int(x), int(y), 0, 3)
                else: lp.LedCtrlXY(int(x), int(y), 3, 0)
            elif name == "stop":
                lp.LedCtrlXY(int(x), int(y), 3, 0)
        elif name.find("(Dry)") == -1:
            lp.LedCtrlXY(int(x), int(y), 0, 3)
        else:
            lp.LedCtrlXY(int(x), int(y), 3, 0)

button_hold_mode = False

# Define the Launchpad Mini button layout
top_right_button = (7, 0)

# Initialize the Launchpad Mini
lp = launchpad.Launchpad()

if lp.Open():
    print("Launchpad Mini is connected")
else:
    print("Could not open the Launchpad Mini")
    exit(1)

# Initialize Pygame for playing MP3
pygame.mixer.init()

set_lights()

try:
    while True:
        # Poll for button presses
        button_states = lp.ButtonStateXY()

        if button_states != []:
            print(button_states)
            jingle = get_jingle_name(button_states[0], button_states[1])
            if jingle != "Button not mapped" and button_states[2] == True:
                match jingle:
                    case "hold_mode":
                        button_hold_mode = not button_hold_mode
                        set_lights()
                    case "stop":
                        pygame.mixer.music.stop()
                    case _:
                        print(jingle + " pressed!")
                        play_mp3(jingle)
            if button_hold_mode and button_states[2] == False:
                pygame.mixer.music.stop()
            
except KeyboardInterrupt:
    lp.Close()