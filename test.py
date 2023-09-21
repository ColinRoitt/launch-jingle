import launchpad_py as launchpad
import pygame

# Define the Launchpad Mini button layout
top_right_button = (7, 0)

# Define the path to your MP3 file
mp3_file_path = "By Students, For Students (Dry) [7s].wav"

# Initialize the Launchpad Mini
lp = launchpad.Launchpad()

if lp.Open():
    print("Launchpad Mini is connected")
else:
    print("Could not open the Launchpad Mini")
    exit(1)

# Initialize Pygame for playing MP3
pygame.mixer.init()

def play_mp3():
    pygame.mixer.music.load(mp3_file_path)
    pygame.mixer.music.play()

try:
    while True:
        # Poll for button presses
        button_states = lp.ButtonStateXY()

        if button_states != []:
            print(button_states)
            if button_states[0] == 0 and button_states[1] == 1 and button_states[2] == True:
                print("Top right button pressed!")
                play_mp3()
            if button_states[0] == 0 and button_states[1] == 1 and button_states[2] == False:
                print("Top right button released!")
                pygame.mixer.music.stop()
        
        # if button_states[top_right_button[0]][top_right_button[1]] == 1:
        #     print("Top right button pressed!")
        #     play_mp3()
            
except KeyboardInterrupt:
    lp.Close()
