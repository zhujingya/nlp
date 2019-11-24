

import os

file_path = os.path.join("data", 'train.txt')
f = open(file_path, 'r', encoding='utf-8')

for line in f :
    line = line.replace("\n", "").split("\t")
    print(line,line[1])