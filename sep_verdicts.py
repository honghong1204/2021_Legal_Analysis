import os

f3_2 = open('diff3_judge2.txt', 'w')
f3_3 = open('diff3_judge3.txt', 'w')

path1 = 'C:/Users/mm/Desktop/diff_3'
allFileList = os.listdir(path1)
for file in allFileList:
    file = os.path.join(path1, file)
    f = open(file, 'r', encoding="utf-8")
    firstline = f.readline()
    secondline = f.readline()
    for i in range(len(secondline)):
            if secondline[i] != "上" and secondline[i] != "台":
                continue
            if secondline[i] == "上" and secondline[i-1] != "台":
             f3_2.write(file+"\n")
            if secondline[i] == "上" and secondline[i-1] == "台":
             f3_3.write(file+"\n")
    f.close()

f2_2 = open('diff2_judge2.txt', 'w')
f2_3 = open('diff2_judge3.txt', 'w')

path2 = 'C:/Users/mm/Desktop/diff_2'
allFileList = os.listdir(path2)
for file in allFileList:
    file = os.path.join(path2, file)
    f = open(file, 'r', encoding="utf-8")
    firstline = f.readline()
    secondline = f.readline()
    for i in range(len(secondline)):
            if secondline[i] != "上" and secondline[i] != "台":
                continue
            if secondline[i] == "上" and secondline[i-1] != "台":
                f2_2.write(file+"\n")
            if secondline[i] == "上" and secondline[i-1] == "台":
                f2_3.write(file+"\n")
    f.close()

fc_2 = open('c_judge2.txt', 'w')
fc_3 = open('c_judge3.txt', 'w')

path3 = 'C:/Users/mm/Desktop/common'
allFileList = os.listdir(path3)
for file in allFileList:
    file = os.path.join(path3, file)
    f = open(file, 'r', encoding="utf-8")
    firstline = f.readline()
    secondline = f.readline()
    for i in range(len(secondline)):
            if secondline[i] != "上" and secondline[i] != "台":
                continue
            if secondline[i] == "上" and secondline[i-1] != "台":
                fc_2.write(file+"\n")
            if secondline[i] == "上" and secondline[i-1] == "台":
                fc_3.write(file+"\n")
    f.close()
