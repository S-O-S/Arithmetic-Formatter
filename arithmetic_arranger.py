def arithmetic_arranger(problems, show_result=None):

# If second argument is not passed as such we are setting the default value False to it
    if show_result is None:
        show_result = False

# Situations that will return an error:
    # If there are too many problems supplied to the function. 
    # The limit is five, anything more will return: Error: Too many problems.

    if len(problems) > 5:
        return "Error: Too many problems."

    # Rules:
    # The appropriate operators the function will accept are addition and subtraction. 
    # Multiplication and division will return an error. 
    # Other operators not mentioned in this bullet point will not need to be tested. 
    # The error returned will be: Error: Operator must be '+' or '-'.
    
    # First we are seperating all operator and operand
    operators = []
    for expr in problems:
        op1, sbl, op2 = expr.split()
        operators.append([op1.strip() , op2.strip(), sbl.strip()])

    # Now operator check
    for x in operators:
        if x[2] not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

    # Each number (operand) should only contain digits. 
    # Otherwise, the function will return: Error: Numbers must only contain digits.
    for x in operators:
        if not (x[0].isdecimal() and x[1].isdecimal()):
            return "Error: Numbers must only contain digits."

    # Each operand (aka number on each side of the operator) has a max of four digits in width.
    # Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
    for x in operators:
        if len(x[0]) > 4 or len(x[1]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # If the user supplied the correct format of problems, the conversion you return will follow these rules:
        # There should be a single space between the operator and the longest of the two operands, 
        #       the operator will be on the same line as the second operand, 
        #       both operands will be in the same order as provided 
        #       (the first will be the top one and the second will be the bottom.
        # 
        # Numbers should be right-aligned.
        # There should be four spaces between each problem.
        # There should be dashes at the bottom of each problem. 
        # The dashes should run along the entire length of each problem individually. 
        #       (The example above shows what this should look like.)

    # saving max no. of character among operators
    max_len_operator = [ max(len(x[0]), len(x[1])) for x in operators]
    
    # calculating space for top row and generating each element with space,
    # finally concatenting each element with 4 space.
    # i.e. Formating the first row
    space_top_row = [ ( max_len_operator[i] - len(operators[i][0])+ 2) for i in range(len(operators))]
    top_row = [ " " * space_top_row[i] + operators[i][0] for i in range(len(operators))]
    top_row_string = "    ".join(top_row)
    
    # Similarly, formating the second row
    space_second_row = [ ( max_len_operator[i] - len(operators[i][1])+ 1) for i in range(len(operators))]
    second_row = [ operators[i][2] + " " * space_second_row[i] + operators[i][1] for i in range(len(operators))]
    second_row_string = "    ".join(second_row)
    
    # Similarly, formating the third row / dash row
    no_dash_repeated = [ x + 2 for x in max_len_operator]
    dash_row = ["-" * x for x in no_dash_repeated]
    dash_row_string = "    ".join(dash_row)

    # calculating the result 
    result = [ str(eval(x)) for x in problems ]

    # Similarly, formating the result row
    space_result_row = [ max_len_operator[i] + 2 - len(result[i]) for i in range(len(operators))]
    result_row = [ " " * space_result_row[i] + str(result[i]) for i in range(len(operators))]
    result_row_string = "    ".join(result_row) 

    # Concatenating the first 2 row and saving it to arranged_problems
    # In case of True passed as second parameter. we will update arranged_problem and
    # cancatenate the dash_row_string and result_row_string in adsition.

    arranged_problems = "\n".join((top_row_string, second_row_string, dash_row_string))
    if show_result :
        arranged_problems = "\n".join((top_row_string, second_row_string, dash_row_string, result_row_string))
    return arranged_problems