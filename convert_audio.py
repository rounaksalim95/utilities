'''
python3 script that converts .webm and .m4a audio files to .mp3 files
For now pass sys arguments for folders to be processed
* Currently removes old files
Libraries required: pydub (for format conversion)
E.g.: python3 convert_audio.py "audio0" "audio1" "audio2"
'''

# import argparse

# # Handle parsing arguments
# parser = argparse.ArgumentParser()
# parser.add_argument("folders", metavar="F", help="Folders in current folder\
#     that contain .webm and .m4a files")

# args = parser.parse_args()

# Add flag for removing old files

import os
import sys

from pydub import AudioSegment

def convert_audio(directoy_path):
    '''
    Converts all the .webm and .m4a audio files to .mp3 files
    directory_path: The path to the folder containing the audio files
    '''
    full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), directoy_path)
    for audio_file in os.listdir(full_path):
        audio = os.path.join(full_path, audio_file)
        
        strip_num = 0
        audio_type = ""

        if ".webm" in audio_file:
            audio_type = "webm"
            strip_num = 5
        elif ".m4a" in audio_file:
            audio_type = "m4a"
            strip_num = 4
        else:
            continue

        song = AudioSegment.from_file(audio, audio_type)
        song.export(audio[:-strip_num] + ".mp3", format="mp3")

# Check whether arguments have been provided
if len(sys.argv) == 1:
    print("Please provide the folders that contain the audio files")
    sys.exit()

# Convert audio files
for i in range(len(sys.argv)):
    if i != 0:
        print("Converting files in " + sys.argv[i])
        convert_audio(sys.argv[i])

print("Done converting all files!")
