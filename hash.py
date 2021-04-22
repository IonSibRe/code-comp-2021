import os
import re
import tkinter as tk
from tkinter import filedialog
from os.path import isfile, join

root = tk.Tk()
root.withdraw()

# Get Folder
folder = filedialog.askdirectory()
allFiles = [file for file in os.listdir(folder) if isfile(join(folder, file))]

# Sort Alphabetically
allFiles.sort()

indexNum = 0

# Go though all files
for file in allFiles:
    f = open(f"{folder}\{file}", "r")

    hexSum = 0

    # For each character in file add to sum
    for line in f:
        for char in line:
            if (re.match("[a-fA-F0-9]", char)):
                if (char == "a" or char == "A"):
                    hexSum += 10
                elif (char == "b" or char == "B"):
                    hexSum += 11
                elif (char == "c" or char == "C"):
                    hexSum += 12
                elif (char == "d" or char == "D"):
                    hexSum += 13
                elif (char == "e" or char == "E"):
                    hexSum += 14
                elif (char == "f" or char == "F"):
                    hexSum += 15
                else:
                    hexSum += int(char)

    hexSum = str(hex(hexSum))[2:]

    finalSum = 0

    # Sum until you have a single digit number
    while(len(hexSum) > 1):
        for char in hexSum:
            finalSum += int(char, 16)
        hexSum = str(hex(finalSum))[2:]
        finalSum = 0

    indexNum += 1

    # Final Output
    print(f"{indexNum} {hexSum} {file}")

    f.close()
    
print("Finished")