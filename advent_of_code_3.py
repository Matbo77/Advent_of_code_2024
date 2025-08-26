


import os, os.path
import sys
import numpy as np


#pathtoinput = "C:\\Users\\matbo\Documents\\Programmation\\Python\\Advend_of_code"
#pathtoinput = "C:\Users\matbo\Documents\Programmation\Python\Advent_of_code"
#sys.path.append(pathtoinput)



# advent of code


# day 3 Part 1 and Part 2
# memory (your puzzle input) is corrupted.
# All of the instructions have been jumbled up!


# Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

test = 0

if test==0:
    input_file = "input-3.txt"
else:
    #input_file = "input-test-3.txt"
    input_file = "input-test-3.1.txt"





sum_mult = 0
sum_mult_do = 0

Nl = sum(1 for _ in open(input_file)) #line number

start_patern = "mul("
len_patern = len(start_patern)
mid_patern = ","
end_patern = ")"


do_patern = "do()"
dont_patern = "don't()"



with open(input_file, 'r') as f: # read the file

    line_number = 0

    one_line = ""

    for line_i in f:

        # gather all file lines in one line
        one_line = one_line + line_i


#for line in f:
#line_number+= 1
#print("\n Line ",line_number)

    #processed_line = line.strip().split()

    Nc = len(one_line) #column number / characters

    list_index_do = []

    ## build list_index_do (considering don't)
    number_dont_patern = one_line.count(dont_patern)
    number_do_patern = one_line.count(do_patern)


    index_do_start = 0
    index_do_end = one_line.find(dont_patern, index_do_start+1) # also index don't start

    #list_index_do.append([i for i in range(index_do_start,index_do_end)])

    while index_do_end != -1 and  index_do_start != -1 :

        list_index_do.extend([i for i in range(index_do_start,index_do_end)])

        index_do_start = one_line.find(do_patern, index_do_end+1)
        index_do_end = one_line.find(dont_patern, index_do_start+1)

    if index_do_end == -1:
        list_index_do.extend([i for i in range(index_do_start,Nc)])
    #else: # index_do_start == -1

            #list_index_do.extend([i for i in range(index_do_start,Nc)])

    #print(one_line)
    print("List index do:",list_index_do)


    ## mult() detection
    number_start_patern = one_line.count(start_patern)

    #print(number_start_patern)

    i_patern_previous = -1 #index previous patern test

    for k in range(number_start_patern):

        i_f = one_line.find(start_patern, i_patern_previous+1)
        i_patern_previous = i_f


        if one_line[i_f+len_patern].isdigit():

            size_int_1 = 1

            while one_line[i_f+len_patern+size_int_1].isdigit():

                size_int_1+=1

            if one_line[i_f+len_patern+size_int_1] == mid_patern: # ","

                int_1 = int(one_line[i_f+len_patern:i_f+len_patern+size_int_1])


                i_mid = i_f + len_patern  + size_int_1


                if one_line[i_mid + 1].isdigit():

                    size_int_2 = 1

                    while one_line[i_mid + size_int_2 + 1].isdigit():

                        size_int_2+=1

                    if one_line[i_mid + size_int_2 + 1] == end_patern: # ")"


                        int_2 = int(one_line[i_mid+1:i_mid+1+size_int_2])

                        sum_mult = sum_mult + int_1*int_2


                        if i_f in list_index_do:

                            if test == 1:
                                print("Multiply",int_1,"by",int_2)

                            sum_mult_do = sum_mult_do + int_1*int_2

    print(one_line)
    print(Nc)
    print("number_start_patern:",number_start_patern)

    # intermediate result wit heach line increase
    #print("Sum mult: ",sum_mult )
    #print("Sum mult do: ",sum_mult_do )


    print("Sum mult: ",sum_mult )
    # Result test Part 1 : 161
    # Result Part 1 : 185797128


    print("Sum mult do: ",sum_mult_do )
    # Result test Part 2 : 48
    # Result Part 2 : 89798695


# Part 2 Answer 90284027 # too high
# Part 2 Answer 92974346 # too high



## Test

# print(line.find(start_patern,0,len(line)))
#
# i_f = line.find(start_patern,30)
# print(i_f)
# print(line[i_f:i_f+len_patern+1])
#
# i_r = line.rfind(start_patern)
# line[i_r:i_r+4]



#input


