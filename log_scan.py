#-------------------------------------------------------------------------------
# Name:        Log Reader 1.2
# Purpose:      Reads log files and determines if the process
#               documented by the log succeeded!
#               Supports files with .log extension.
#
# Author:      Nicholas Offer
#
# Created:     30/04/2015
# Copyright:   (c) Nicholas Offer 2015
#
# Changelist:   - 05/05/2015 - Added custom file path option. Input when program
#               is run from the command prompt. If no path is input, searches
#               current directory.
#               - 05/16/2015 - Updated comments
#               - 01/29/2016 - Fail keywords now read from text file
#-------------------------------------------------------------------------------
import string
import os
import sys
import re

# Searches for any instance of item in any string element of list1
# Returns True if item is found as a substring of an element of list1,
# False otherwise
def in_list(item, list1):
    for thing in list1:
        if (re.search(thing, item) is not None):
            return True

    return False

# Prints an error message and the given log that failed.
def fail_log(log_path):
    with open(log_path) as current_log:
        message = current_log.read()

    print("Process logged in {0} failed!".format(log_path))
    print("Log contents:\n-----")
    print(message)
    print("-----")

# Checks if any words in the last line of the given log indicate a failure.
# Runs fail_log if failed and prints a success message if not
def read_log(log_path):
    
    # Read the list of fail keywords
    fail_list = [];
    with open("fail_keywords.txt") as failFile:
        for word in failFile:
            # Cut the last character (newline)
            fail_list.append(word[:len(word)-1])

    with open(log_path) as logFile:
        fullLog = []
        for line in logFile:
            pass
        last_line = line

        for word in last_line.split(" "):
            word = word.lower()
            if (in_list(word, fail_list)):
                fail_log(log_path)
                logFile.close()
                return 1

        print "The process logged in {0} succeeded".format(log_path)
        logFile.close()
        return 0

# Returns the last extension on a given file name (string).
# Eg. get_extension(sample.txt.avi.jpg) returns ".jpg"
def get_extension(filename):
    index = 0
    for index, char in enumerate(reversed(filename)):
        if char == '.':
            break
    return (filename[(len(filename) - index - 1):])

# Looks in the given directory and checks the extension. If it's ".log", process
# the file.
def scan_files():
    f = []
    # If no path is input (eg, sys.argv is ["log_pro.py"]) use current directory
    try:
        directory = sys.argv[1]
    except IndexError:
        directory = "./"

    for (dirpath, dirnames, filenames) in os.walk(directory):
        f.extend(filenames)
        break
    
    numFails = 0
    for log_file in f:
        if (get_extension(log_file) == '.log'):
            numFails += read_log(log_file)
    print("Done scanning files. Found {0} failure{1}.".format(
       numFails,
       "" if numFails == 1 else "s"
    ))

scan_files()
