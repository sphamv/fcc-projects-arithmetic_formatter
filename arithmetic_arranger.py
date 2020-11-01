# function takes 2 arguments -> list of strings + boolean flag






# single space between operator and longest of the operands
# operator one same line as second operand
# four spaces between each problem
# dashes at the bottom of each problem

# pull out the list and split the strings
# check 
# 


def arithmetic_arranger(problems, solution):
    bol = solution

    # max 5 entries in list
    if len(arr) > 5: return "Error: Too many problems"

    for problem in problems:
        no1 = problem.split()[0]
        no2 = problem.split()[2]
        op = problem.split()[1]

        # operator only '+' or '-'
        if op not in ['+','-']: return 'Error: Operator must be '+' or '-''

        # max 4 digit numbers
        if len(no1)>4 | len(no2)>4: return "Error: Numbers cannot be more than four digits"
        
        # numbers only digits
        try: 
            no1 = int(no1)
            no2 = int(no2)
        except:
            return 'Error: Numbers must only contain digits.'



    return arranged_problems