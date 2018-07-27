'''python3 script that converts new shortened youtu.be links to
the older youtube.com links for all .txt files ih the current directory
'''

import os

def convert_links(txt_file):
    '''
    Converts the shortened link to the old format
    txt_file: .txt file containing shortened links
    '''
    f_old = open(txt_file, "r")
    f_new = open(txt_file + "_tmp", "w")
    for link in f_old:
        if link.strip() != "":
            if "youtu.be" in link:
                parts = link.split("/")
                youtube_id = parts[-1]
                f_new.write("https://www.youtube.com/watch?v=" + youtube_id + "\n")
            else:
                f_new.write(link.strip() + "\n")

    f_old.close()
    f_new.close()

    # Replace the old .txt file with the new one
    os.rename("./" + txt_file + "_tmp", "./" + txt_file)


for item in os.listdir():
    if ".txt" in item:
        convert_links(item)
