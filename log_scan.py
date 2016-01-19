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
#-------------------------------------------------------------------------------
import string
import os
import sys

# Returns True if item is within list1, False otherwise
def in_list(item, list1):
    for thing in list1:
        if (item == thing):
            return True

    return False

# Prints an error message and the given log that failed.
def fail_log(log_path):
    with open(log_path) as current_log:
        message = current_log.read()

    print("Process failed! Log:")
    print(message)

# Checks if any words in the last line of the given log indicate a failure.
# Runs fail_log if failed and prints a success message if not
def read_logs(log_path):
    pass_list = ["success", "succeeded", "passed", "complete", "completed"
    , "finished"]

    fail_list = ["fail", "failed", "abort", "aborted", "error", "errors"]

    with open(log_path) as logFile:
        fullLog = []
        for line in logFile:
            pass
        last_line = line

        for word in last_line.split(" "):
            word = word.lower()
            if (in_list(word, fail_list)):
                fail_log(log_path)
            elif (in_list(word, pass_list)):
                print("The process succeeded.")

        logFile.close()

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

    for log_file in f:
        if (get_extension(log_file) == '.log'):
            read_logs(log_file)
    print("Done files.")

scan_files()
