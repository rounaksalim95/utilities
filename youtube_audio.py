'''
python3 script that downloads audio file from provided list of YouTube video
links (found in .txt file) in current directoy by each individual file; multiple
different .txt files can be used.
Requires: python3, youtube-dl, pafy
'''

import os

import pafy


def create_folder(folder):
    '''
    Creates a folder
    folder: The path to the folder that needs to be created
    '''
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
    except OSError:
        print('Error: Creating directory. ' +  folder)


def download_audio(directoy_path):
    '''
    Downloads audio files for all links in provided .txt file and stores
    them in the corresponding folder
    directory_path: The path to the .txt file
    '''
    f = open(directoy_path, "r")
    for link in f:
        if link != "":
            print("Link : " + link)
            video = pafy.new(link)
            bestaudio = video.getbestaudio()
            bestaudio.download(quiet=False, filepath="./" + directoy_path[:-4])

    f.close()


directories = []

# Get all the .txt files in the current directory
for item in os.listdir():
    if ".txt" in item:
        directories.append(item)

# Create folders for individual .txt files and download the audio files there
for directory in directories:
    create_folder("./" + directory[:-4] + "/")
    download_audio(directory)
