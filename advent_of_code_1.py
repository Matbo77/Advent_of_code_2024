
import os, os.path
import sys
import numpy as np


pathtoinput = "C:\\Users\\matbo\Documents\\Programmation\\Python\\Advend_of_code"
#pathtoinput = "C:\Users\matbo\Documents\Programmation\Python\Advent_of_code"
#sys.path.append(pathtoinput)



# advent of code


# day 1


input_file = "input-1.txt"



lines = []
list_1 = []
list_2 = []
with open(input_file, 'r') as f: # read the file
    for line in f:
        processed_line = line.strip().split()

        lines.append(processed_line)
        list_1.append(int(processed_line[0]))
        list_2.append(int(processed_line[1]))



print(list_1)

N = len(list_1);

# print(N)

#sort_list_1 = sort(list_1)

list_1.sort()
list_2.sort()


dist_list = [abs(list_1[i]-list_2[i]) for i in range(0,N)]

sum_dist = sum(dist_list)

print(sum_dist)
# Result Part 1 # 1879048


similarity_score = 0
for elt in list_1:


    similarity_score += sum([elt*int(list_2[i]==elt) for i in range(0,N)])

print(similarity_score)
# Result Part 2 # 21024792

