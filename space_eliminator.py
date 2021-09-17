'''
I'm tired of have folks create files with spaces in them and I'm sure there are a couple folks
out there who feel the same way.
This simple Python3 script recursively goes through the folder provided as an argument and renames files it comes across by replacing spaces with dashes.

This script doesn't use os.walk as we want to ignore hidden directories such as .git.

Note: 
- Ignores files and directories beginning with '.' - don't want to be renaming files in the `.git` folder..
- The script doesn't play well with symbolic links so be careful with those while using this!
    - Currently I don't have use of symlinks so the overhead of adding support for this isn't worth it; might implement it later.

Usage: python3 space_eliminator.py <path-to-directory>
'''

import collections
import os
import sys


def main():
    if (len(sys.argv) != 2):
        print("Only root directory that needs to be cleansed is accepted")
        exit()

    # Let's do a DFS and go through all the directories
    # We don't need to keep track of visited directories as we are operating on a DAG (assuming we don't have symlinks)
    stack = collections.deque()
    stack.append(sys.argv[1])

    while stack:
        directory = stack.popleft()
        for f in os.listdir(directory):
            if not f.startswith("."):
                object_path = os.path.join(directory, f)
                if os.path.isfile(object_path):
                    if " " in f:
                        space_free_name = os.path.join(directory, f.replace(" ", "-"))
                        os.rename(object_path, space_free_name)
                        print("Renamed " + object_path + " to " + space_free_name)
                elif os.path.isdir(object_path):
                    stack.append(object_path)


if __name__ == "__main__":
    main()
