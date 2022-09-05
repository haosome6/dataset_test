import os

for files in os.listdir('hmdb51'):
    foldername = files.split('.')[0]
    os.system('mkdir -p hmdb51/' + foldername)
    os.system('unrar e hmdb51/' + files + ' hmdb51/' + foldername)

os.system('rm hmdb51/*.rar')
