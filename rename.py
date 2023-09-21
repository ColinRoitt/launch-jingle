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
    '1,3': 'University Radio York [6s].mp3',
    '2,3': 'On Air, Online, On Tap (Jazz) [7s].mp3',
    '3,3': 'By Students, For Students 1 (Dry) [7s].mp3',
    '4,3': 'Message via the Website (Dry) [5s].mp3',
    '5,3': 'On Air, Online, On Tap (Dry) [7s].mp3',
    '6,3': 'Message via the Website [7s].mp3',
    '7,3': 'On Air, Online, On Tap [8s].mp3',

    # Group 4: Medium to Long Jingles
    '0,5': 'Text Now (Dry) [4s].mp3',
    '1,5': 'Text Now [5s].mp3',
    '2,5': 'Mixcloud [8s].mp3',
    '3,5': 'Spotify [9s].mp3',
    '4,5': 'Join Now 2 [6s].mp3',
    '5,5': 'UoY Student Station 3 [9s].mp3',
    '6,5': 'Join Now 1 [10s].mp3',

    # Group 5: Long Jingles
    '0,7': 'clap - time machine team.mp3',
    '1,7': 'aww - time machine team.mp3',
    '2,7': 'yay - time machine team.mp3'
}

jingles = ['By Students, For Students 2 [6s].mp3'
,'Broadcasting URY [3s].mp3'
,'By Students, For Students 1 (Dry) [7s].mp3'
,'Broadcasting URY (Dry) [3s].mp3'
,'Message via the Website [7s].mp3'
,'Message via the Website (Dry) [5s].mp3'
,'On Air, Online, On Tap (Dry) [7s].mp3'
,'On Air, Online, On Tap [8s].mp3'
,'On Air, Online, On Tap (Jazz) [7s].mp3'
,'Spotify [9s].mp3'
,'University Radio York [6s].mp3'
,'UoY Student Station 3 [9s].mp3'
,'URY 1 [2s].mp3'
,'URY 3 (Dry) [2s].mp3'
,'URY Whisper 3 (Dry) [2s].mp3'
,'Mixcloud [8s].mp3'
,'Join Now 2 [6s].mp3'
,'Join Now 1 [10s].mp3'
,'Text Now [5s].mp3'
,'Text Now (Dry) [4s].mp3'
,'clap - time machine team.mp3'
,'aww - time machine team.mp3'
,'yay - time machine team.mp3']

#  rename each file in the jingles folder to its corresponding key in the jingle_mapping dictionary
import os
import re
files_to_rename = os.listdir('Jingles')
print(files_to_rename)
for i, file in enumerate(files_to_rename):
    if file.startswith('managed'):
        # index_of_jingle_name = int(file.split('(')[1].split(')')[0])
        # get the number in brackets from the file name with regex
        index_of_jingle_name = int(re.findall('\((.*?)\)', file)[0])
        new_name = jingles[index_of_jingle_name]
        os.rename(f'Jingles/{file}', f'Jingles/{new_name}')
        print(f'{file} renamed to {new_name}')