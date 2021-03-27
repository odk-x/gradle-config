#!/usr/bin/python3

import os, sys

TOOLS = ["services", "scan", "sensorsinterface", "sensorsframework", "survey", "tables", "submit", "androidlibrary", "androidcommon"]
VER_TEXT = "gradle.ext.gradleConfigVersion = "

# Get the new verison number
if len(sys.argv) < 2:
    print ("Please specify a new version number to assign")
    sys.exit(0)

VER_TEXT += sys.argv[1] + "\n"

# Retrieve the absolute path for the container folder
rootdir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

for name in os.listdir(rootdir):

    # Create the absolute path for the sub directory and verify it is valid
    dirPath = os.path.join(rootdir, name);
    if not os.path.isdir(dirPath):
        continue

    # Find each of the relevent directories and uptick the version
    if name in TOOLS:
        settingsPath = os.path.join(dirPath, "settings.gradle")

        if not os.path.isfile(settingsPath):
            print ("Failed to update: " + name)
            continue

        # Copy the file into memory, updating the line with the version number
        settingsFile = open(settingsPath, 'r')
        lines = settingsFile.readlines()
        lines[0] = VER_TEXT
        settingsFile.close()

        # Rewrite the file with the updated version number
        settingsFile = open(settingsPath, 'w')
        settingsFile.writelines(lines)
        settingsFile.close()

        # Keep track of which tools we've updated
        del TOOLS[TOOLS.index(name)]
        print ("Updated version for " + name)

# If we failed to update a tool, print a warning
for name in TOOLS:
    print ("Couldn't find: " + name + " dir to be updated")




