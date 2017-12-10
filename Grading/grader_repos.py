'''
This script is intended to be used to help with grading in CS 891/892 [works with both python2 and python3]
It uses a file repos.txt that should contain lines with the name of the student followed by their gitlab repo url separated by a space 
Example: Rick_Sanchez git@rick.git

Script expects two arguments, the date the assignment is due (format example: Nov 8) and the name of the feedback branch (example: Assignment_137_Feedback)
Example of script usage: python grader_repos.py "Nov 8" "Assignment_3_Feedback"

This will create a folder named after the students in the current directory the script is invoked from and then use the git log to find the latest commit hash before 
the due time and checkout that commit and create a feedback brach for the student's work before the due time
P.S. The code is pretty ugly and hacky but gets the job done; will probably clean it up later 
'''

import sys
import os
import subprocess

# Ensure the right number of arguments were passed 
# Two strings passed as argumnents; date assignment is due and the assignment name 
# Example of usage python grader_repos.py "Nov 8" "Assignment_3"
if (len(sys.argv) != 3):
    print('Incorrect number of arguments; please pass in only two strings that contain the due date in the format : Month[3 letter] Date[1/2 digit] like Nov 12 and the assignment name')
    exit()

# Get the current working directory 
# Need to use subprocess to get the output result of running the command 
directory = subprocess.check_output(['pwd'])
# Decode the result using utf-8 since we get back a byte string 
directory = directory.decode("utf-8")
directory = directory.rstrip('\n')
assignment = sys.argv[2]

'''
Processes the lines read from the file containing the repos 
Creates a folder with the name of the student, clones their repo in it, 
and then checks out the latest commit on the due date since assignments 
are always due 23:59
'''
def process_line(line):
    line = line.rstrip('\n')
    parts = line.split(' ')
    # parts[0] contains name of student 
    # parts[1] contains gitlab url 
    os.system('mkdir ' + parts[0])
    # Get repo's name 
    repo_name = parts[1].split('/')[1].split('.')[0]
    command = 'cd ' + parts[0] + ' && ' + 'git clone ' + parts[1] + ' && cd ' + repo_name + ' && git log > log.txt' 
    os.system(command)
    # Go through the log and get the latest commit before the due data
    commit = ''
    month = sys.argv[1].split(' ')[0].lower()
    day = int(sys.argv[1].split(' ')[1])
    with open('./' + parts[0] + '/' + repo_name + '/log.txt') as log:
        for line in log:
            line = line.rstrip('\n')
            if ("commit" in line):
                commit = line.split(' ')[1]
            if ("Date" in line):
                line_parts = line.split(' ')
                commit_month = line_parts[4].lower()
                commit_day = line_parts[5]
                if (commit_month == month and int(commit_day) <= day):
                    break

    # Remove the log.txt file that was created 
    os.system('cd ' + parts[0] + ' && cd ' + repo_name + ' && rm log.txt')
    
    # Check out the latest commit before the due date 
    os.system('cd ' + parts[0] + ' && cd ' + repo_name + ' && git checkout ' + commit + ' && git checkout -b ' + assignment)
    
with open('repos.txt') as repos:
    for line in repos:
        process_line(line)