def runbas(code):
    code = code.split("\n")
    variables = {}
    i = 0
    while i < len(code):
        line = code[i].split()
        if line[0] == "jmp":
            try:
                jump_to = int(line[1]) - 1
                if jump_to < 0 or jump_to >= len(code):
                    raise ValueError("Jump target out of range")
                i = jump_to
            except ValueError as e:
                print(f"Error: {e}")
                return
        elif line[0] == "var":
            if len(line) < 2:
                print("Error: Invalid variable declaration")
                return
            variables[line[1]] = None
        elif line[0] == "io":
            if len(line) < 2:
                print("Error: Invalid IO command")
                return
            if line[1] not in variables:
                print(f"Error: Undefined variable '{line[1]}'")
                return
            print(variables[line[1]])
        elif line[0] == "ios":
            print(" ".join(line[1:]))
        elif line[0] == "set":
            if len(line) < 3:
                print("Error: Invalid set command")
                return
            if line[1] not in variables:
                print(f"Error: Undefined variable '{line[1]}'")
                return
            try:
                variables[line[1]] = eval(line[2])
            except Exception as e:
                print(f"Error: {e}")
                return
        elif line[0] == "jif":
            if len(line) < 5:
                print("Error: Invalid jif command")
                return
            if line[1] not in variables or line[3] not in variables:
                print(f"Error: Undefined variable in jif command")
                return
            var1 = variables[line[1]]
            var2 = variables[line[3]]
            try:
                jump_to = int(line[4]) - 1
                if jump_to < 0 or jump_to >= len(code):
                    raise ValueError("Jump target out of range")
                if (line[2] == "<" and var1 < var2) or (line[2] == ">" and var1 > var2) or (line[2] == "=" and var1 == var2):
                    i = jump_to
            except ValueError as e:
                print(f"Error: {e}")
                return
        elif line[0] == "in":
            if len(line) < 2:
                print("Error: Invalid input command")
                return
            variables[line[1]] = int(input("Enter a number: "))
        i += 1
