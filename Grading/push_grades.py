'''
This script is intended to be used to help with grading in CS 891/892 [works with both python2 and python3]
It uses a file repos.txt that should contain lines with the name of the student followed by their gitlab repo url separated by a space 
Example: Rick_Sanchez git@rick.git

Script expects two arguments, the name of the feedback branch (example: Assignment_137_Feedback)[same name as used with grader_repos.py] and a commit message 
Example of script usage: python push_grades.py "Assignment_3_Feedback" "Assignment 3 feedback and grade" 

This is meant to be used in conjunction with grader_repos.py and pushes out the grader's commits to the students' repos 
Please make sure this script is in the directory in which grader_repos.py was invoked 
P.S. The code is pretty ugly and hacky but gets the job done; will probably clean it up later 
'''

import sys
import os

# Ensure the right number of arguments were passed 
# Two strings - Feedback branch name and commit message 
# Example of usage python push_grades.py "Assignment_3_Feedback" "Assignment 3 feedback and grade" 
if (len(sys.argv) != 3):
    print("Incorrect number of arguments; please pass in two strings that contain the feedback branch's name and the commit message")
    exit()

assignment_branch = sys.argv[1]
commit_message = sys.argv[2]

git_add = "git add ."
git_commit = 'git commit -m "' + commit_message + '"'
git_push = 'git push origin ' + assignment_branch

'''
Processes the lines read from the file containing the repos 
Pushes out the commits that the grader has on the feedback branch for every student repo
'''
def process_line(line):
    line = line.rstrip('\n')
    parts = line.split(' ')
    # parts[0] contains name of student 
    # parts[1] contains gitlab url 
    
    command = 'cd ' + parts[0] + ' && ' + git_add + ' && ' + git_commit + ' && ' + git_push
    os.system(command)
    
with open('repos.txt') as repos:
    for line in repos:
        process_line(line)