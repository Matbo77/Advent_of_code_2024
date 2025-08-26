


import os, os.path
import sys
import numpy as np


#pathtoinput = "C:\\Users\\matbo\Documents\\Programmation\\Python\\Advend_of_code"
#pathtoinput = "C:\Users\matbo\Documents\Programmation\Python\Advent_of_code"
#sys.path.append(pathtoinput)



# advent of code


# day 4 Part 1 and Part 2

# word search, XMAS

# This word search allows words to be horizontal, vertical, diagonal,
# written backwards, or even overlapping OTHER WORDS.



#1:  ....XXMAS.     # 1 + 1 diag
#2:  .SAMXMS...     # 1
#3:  ...S..A...     # 0
#4:  ..A.A.MS.X     # 1 + 1 diag
#5:  XMASAMX.MM     # 3
#6:  X.....XA.A     # 0  +  2 diag
#7:  S.S.S.S.SS     # 0
#8:  .A.A.A.A.A     # 0
#9:  ..M.M.M.MM     # 0
#10: .X.X.XMASX     # 2 + 6 diag

                 # = 8 + 10
                 # = 18


# Part 2 : it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

# M.S  M.M S.M S.S
# .A.  .A. .A. .A.
# M.S  S.S S.M M.M


test = 0

if test == 0:
    input_file = "input-4.txt"
else:
    input_file = "input-test-4.txt"
    #input_file = "input-test-4.1.txt"



Nl = sum(1 for _ in open(input_file)) #line number

patern = "XMAS"
backward_patern = "SAMX"

len_patern = len(patern)

total_number_patern = 0

matrix_words = []

matrix_characters = []

transpose_matrix_words = []

occurence_X = 0
list_pos_X = []

occurence_A = 0
list_pos_A = []

with open(input_file, 'r') as f: # read the file

    line_number = 0


    for line in f:

        line_number+= 1
        print("Line ",line_number)

        processed_line = line.split()[0]

        Nc = len(processed_line) #column number / characters



        number_patern = processed_line.count(patern)
        number_backward_patern = processed_line.count(backward_patern)


        total_number_patern = total_number_patern + number_patern + number_backward_patern



        # print(processed_line +"  "+str(Nc))
        # print("number patern:",number_patern)
        # print("number backward patern:",number_backward_patern)


        matrix_words.append(processed_line)
        processed_line_char = list(processed_line)
        matrix_characters.append(processed_line_char)

        occurence_X_line = processed_line_char.count("X")
        occurence_X += occurence_X_line

        k_X = 1
        column_number = -1
        while k_X <= occurence_X_line:

            column_number = processed_line.find("X",column_number+1)

            list_pos_X.append([line_number-1,column_number])

            k_X +=1

        # for Part 2
        occurence_A_line = processed_line_char.count("A")
        occurence_A += occurence_A_line

        k_A = 1
        column_number = -1
        while k_A <= occurence_A_line:

            column_number = processed_line.find("A",column_number+1)

            list_pos_A.append([line_number-1,column_number])

            k_A +=1





    f.close()

print("Total Number XMAS: ", total_number_patern )

transpose_matrix_char = np.transpose(matrix_characters)

for k in range(Nc):
    transpose_line_words = ''.join(transpose_matrix_char[k][:])

    number_patern = transpose_line_words.count(patern)
    number_backward_patern = transpose_line_words.count(backward_patern)

    total_number_patern = total_number_patern + number_patern + number_backward_patern

    transpose_matrix_words.append(transpose_line_words)

print("Total Number XMAS: ", total_number_patern )




# look for diagonal "XMAS"
#print("Occurence_x: ",occurence_X)

for k in range(occurence_X):

    pos_X = list_pos_X[k]

    l_X = pos_X[0]
    c_X = pos_X[1]



    conditions_diag = [1]*4

    possible_diag = [[1,1],[1,-1],[-1,-1],[-1,1]]

    # check for all possible diagonal
    for i in range(4):

        j = 1
        l_X_p = l_X
        c_X_p = c_X

        while j < len_patern and conditions_diag[i]==1:
            letter = patern[j]     # letter in patern

            l_X_p = l_X_p + possible_diag[i][0]
            c_X_p = c_X_p + possible_diag[i][1]

            if 0 <= l_X_p < Nl and 0 <= c_X_p < Nc:

                diag_letter = matrix_characters[l_X_p][c_X_p]

                if diag_letter == letter:

                    conditions_diag[i] = 1
                    j = j + 1
                else:
                    conditions_diag[i] = 0

            # diag_letter_2 = matrix_characters[l_X + 1,c_X - 1]
            # diag_letter_3 = matrix_characters[l_X - 1,c_X - 1]
            # diag_letter_4 = matrix_characters[l_X - 1,c_X + 1]
            else:
                conditions_diag[i] = 0

    patern_diag = sum(conditions_diag)
    total_number_patern = total_number_patern + patern_diag




#print(Nc)
print("Final Total Number XMAS: ", total_number_patern )
    # Result test Part 1 : 18
    # Result Part 1 : 2599


    #print("Total Number XMAS: ",sum_mult_do )



# Part 2: look for X-MAS shape
total_number_shape_XMAS = 0

for k in range(occurence_A):

    pos_A = list_pos_A[k]

    l_A = pos_A[0]
    c_A = pos_A[1]

    # eliminate A on the edge, no shape possible
    if l_A != 0 and l_A != Nl-1 and c_A != 0 and c_A != Nc-1:

        j = 0
        #possible_diag = [[1,1],[1,-1],[-1,-1],[-1,1]]
        condition_shape = 1

        while j<2 and condition_shape == 1:

            l_A_p = l_A + possible_diag[j][0]
            c_A_p = c_A + possible_diag[j][1]

            #if 0 <= l_A_p < Nl and 0 <= c_A_p < Nc:

            diag_letter = matrix_characters[l_A_p][c_A_p]

            if diag_letter == "M":

                l_A_p = l_A - possible_diag[j][0]
                c_A_p = c_A - possible_diag[j][1]

                diag_letter_opposite_diag = matrix_characters[l_A_p][c_A_p]

                if diag_letter_opposite_diag != "S":
                    condition_shape = 0

            elif diag_letter == "S":

                l_A_p = l_A - possible_diag[j][0]
                c_A_p = c_A - possible_diag[j][1]

                diag_letter_opposite_diag = matrix_characters[l_A_p][c_A_p]

                if diag_letter_opposite_diag != "M":
                    condition_shape = 0
            else:
                condition_shape = 0

            j += 1

        if condition_shape == 1:
            total_number_shape_XMAS +=1



print("Shape X-MAS: ",total_number_shape_XMAS)



# Result test Part 2 : 9
# Result Part 2 : 1948










