def arithmetic_arranger(*args):
    problems=args[0]
    # check if input of problems has the correct format
    if len(problems[0].split()) != 3:
        return "Error: Please enter a problem in the form 'x + y'"

    # max 5 entries in list
    if len(problems) > 5: return "Error: Too many problems."

    operator1 = []
    operator2 = []
    operand = []
    solutions = []

    for problem in problems:
        no1 = problem.split()[0]
        no2 = problem.split()[2]
        op = problem.split()[1]

        # operator only '+' or '-'
        if op not in ['+','-']: return "Error: Operator must be '+' or '-'."

        # max 4 digit numbers
        if len(no1) > 4 or len(no2)>4: return "Error: Numbers cannot be more than four digits."
        
        # numbers only digits
        try: 
            no1 = int(no1)
            no2 = int(no2)
        except:
            return 'Error: Numbers must only contain digits.'

        operator1.append(no1)
        operator2.append(no2)
        operand.append(op)
        
        #calculate solutions and put into solutions list
    for i in range (0,len(problems)):
        if(operand[i] == "+"):
            solutions.append(operator1[i] + operator2[i])
        else: 
            solutions.append(operator1[i] - operator2[i])
        
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for i in range(0, len(problems)):
        if operator1[i] > operator2[i]:
            line1 += (" " * 2) + str(operator1[i]) + (" " * 4)
            line2 += operand[i] + " " + " " * (len(str(operator1[i])) - len(str(operator2[i]))) + str(operator2[i]) + (" " * 4)
            line3 += "-" * (len(str(operator1[i]))+2) + (" " * 4)

            if len(str(solutions[i])) > len(str(operator1[i])):
                line4 += " " * (len(str(solutions[i])) - len(str(operator1[i]))) + str(solutions[i]) + (" " * 4)
            elif len(str(solutions[i])) < len(str(operator1[i])):
                line4 += " " * (len(str(operator1[i])) - len(str(solutions[i]))) + str(solutions[i]) + (" " * 4)
            else:
                line4 += " " * 2 + str(solutions[i]) + (" " * 4)

        else:
            line1 += " " * 2 + " "*(len(str(operator2[i])) - len(str(operator1[i]))) + str(operator1[i]) + (" " * 4)
            line2 += operand[i] + " " + str(operator2[i]) + (" " * 4)
            line3 += "-" * (len(str(operator2[i]))+2) + (" " * 4)

            if len(str(solutions[i])) > len(str(operator2[i])):
                line4 += " " * (len(str(solutions[i])) - len(str(operator2[i]))) + str(solutions[i]) + (" " * 4)
            elif len(str(solutions[i])) < len(str(operator2[i])):
                line4 += " " * (len(str(operator2[i])) - len(str(solutions[i]))) + str(solutions[i]) + (" " * 4)
            else:
                line4 += " " * 2 + str(solutions[i]) + (" " * 4)

    try:
        if args[1]==True:
            return line1[:len(line1)-4] + '\n' + line2[:len(line2)-4] + '\n' + line3[:len(line3)-4] + '\n' + line4[:len(line4)-4]
    except:
        return line1[:len(line1)-4] + '\n' + line2[:len(line2)-4] + '\n' + line3[:len(line3)-4]

