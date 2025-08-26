import os, os.path
import sys
import numpy as np


#pathtoinput = "C:\\Users\\matbo\Documents\\Programmation\\Python\\Advend_of_code"
#pathtoinput = "C:\Users\matbo\Documents\Programmation\Python\Advent_of_code"
#sys.path.append(pathtoinput)



# advent of code


# day 2 Part 1 and Part 2


test = 0

if test==0:
    input_file = "input-2.txt"
else:
    input_file = "input-test-2.txt"


# A report only counts as SAFE if both of the following are true:

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three


lines = []
matrix_evolution_string = []
matrix_differences = []



Nl = sum(1 for _ in open(input_file))

with open(input_file, 'r') as f: # read the file

    #Nl = len(f.readlines())
    list_SAFE = [0]*Nl # 1 if SAFE, 0 otherwise


    # tolerate a single bad level (when we remove it)
    list_SAFE_tolerance = [0]*Nl  # 2nd part
    k=0

    for line in f:
        processed_line = line.strip().split()

        k=k+1
        lines.append(processed_line)

        Nc = len(processed_line);

        list_evolution = [int(processed_line[i]) for i in range(0,Nc)]

        differences = [list_evolution[i+1]-list_evolution[i] for i in range(0,Nc-1)]
        matrix_differences.append(differences)

        Ndiff = len(differences)

        matrix_evolution_string.append(processed_line)

        if all(val > 0 for val in differences) or all(val < 0 for val in differences):

            test_level_condition = [abs(val) <= 3 for val in differences]
            if all(test_level_condition):

                list_SAFE[k-1] = 1


        test_level_condition_int = [int(abs(val) <= 3) for val in differences]

        # By default
        list_SAFE_tolerance[k-1] = list_SAFE[k-1]

        # Test among UNSAFE
        if  list_SAFE[k-1] == 0:

            positive_diff = [int(val > 0) for val in differences]
            negative_diff = [int(val < 0) for val in differences]

            sum_positive_diff = sum(positive_diff)
            sum_negative_diff = sum(negative_diff)

            #print("SUM pos diff",sum_positive_diff)
            #print(sum_negative_diff)


            if sum(test_level_condition_int) == Ndiff:

                if sum_positive_diff == Ndiff-1:
            # for the strict monotonicity (increasing/deacreasing) condition,
            # if more than one error, UNSAFE even with the tolerance

                    j = [i for i in range(Ndiff) if differences[i] <= 0] #list of 1 element

                    j_unsafe = j[0] #unsafe element index


                elif sum_negative_diff == Ndiff-1:

                    j = [i for i in range(Ndiff) if differences[i] >= 0] #list of 1 element

                    j_unsafe = j[0] #unsafe element index



            # same for the level condition, if more than one error, UNSAFE even with the tolerance
            elif (sum_positive_diff >= Ndiff-1 or sum_negative_diff >= Ndiff-1) and sum(test_level_condition_int) >= Ndiff-2:

                    j = [i for i in range(Ndiff) if test_level_condition_int[i] == 0] #list of 1 element

                    j_unsafe = j[0] #unsafe element index


                    #print("UNSAFE evolution between",j_unsafe," and ",j_unsafe+1)

                    #j = np.where(test_level_condition_int == 0)


            # new list with one of the two possible UNSAFE elements removed
            new_list_evolution_1 = [list_evolution[i] for i in range(Nc) if i != j_unsafe]
            new_list_evolution_2 = [list_evolution[i] for i in range(Nc) if i != j_unsafe+1]


            new_differences_1 = [new_list_evolution_1[i+1]-new_list_evolution_1[i] for i in range(len(new_list_evolution_1)-1)]

            new_differences_2 = [new_list_evolution_2[i+1]-new_list_evolution_2[i] for i in range(len(new_list_evolution_2)-1)]


            new_test_level_condition_1 = [abs(val) <= 3 for val in new_differences_1]
            new_test_level_condition_2 = [abs(val) <= 3 for val in new_differences_2]


            if  (all(val > 0 for val in new_differences_1) or all(val < 0 for val in new_differences_1)) and  all(new_test_level_condition_1):

                list_SAFE_tolerance[k-1] = 1


            elif (all(val > 0 for val in new_differences_2) or all(val < 0 for val in new_differences_2)) and all(new_test_level_condition_2):

                list_SAFE_tolerance[k-1] = 1


if test==1:
    print(matrix_evolution_string)

print(sum(list_SAFE))
# Result Part 1 #639

print(sum(list_SAFE_tolerance))
# Result Part 2 #674

if test==1:
    print(list_SAFE_tolerance)





# Wrong Guesses

# Part 2
# not 673 # your answer is too low

# not 677 % answer is too high


#print([list_SAFE[i] - list_SAFE_tolerance[i] for i in range(Nl)])





