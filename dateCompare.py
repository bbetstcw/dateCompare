globalPath = "C:/Users/Administrator/Documents/GitHub/azure-content-pr/" 
mooncakePath = "C:/Users/Administrator/Documents/GitHub/azure-content-mooncake-pr/" 
import os.path
import re

dateReg = r"ms\.date\s*=\s*\"([^\"]*)\""

file = open("file.txt", "r")
fileList = [line.strip() for line in file.readlines()]
file.close()
l1 = len(fileList)
l2 = len(set(fileList))
if l1 != l2:
    print("contains duplicate file names")
    exit(-1)

for filename in fileList:
    if filename[:8] == "includes":
        if not os.path.isfile(mooncakePath + filename):
            print("Not exist: "+filename)
    else:
        file1 = open(mooncakePath + filename, "r", encoding="utf-8")
        mooncakeText = file1.read()
        file1.close()
        file2 = open(globalPath + filename, "r", encoding="utf-8")
        globalText = file2.read()
        file2.close()
        mooncakeDate = re.findall(dateReg, mooncakeText)
        globalDate = re.findall(dateReg, globalText)
        if mooncakeDate[0] != globalDate[0]:
            print("Not the same date: "+filename)

