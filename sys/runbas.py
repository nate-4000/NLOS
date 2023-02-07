def runbas(code):
    code = code.split("\n")
    variables = {}
    i = 0
    while i < len(code):
        line = code[i].split()
        if line[0] == "jmp":
            i = int(line[1]) - 1
        elif line[0] == "var":
            variables[line[1]] = None
        elif line[0] == "io":
            print(variables[line[1]])
        elif line[0] == "ios":
            print(" ".join(line[1:]))
        elif line[0] == "set":
            variables[line[1]] = eval(line[2])
        elif line[0] == "jif":
            var1 = variables[line[1]]
            var2 = variables[line[3]]
            if (line[2] == "<" and var1 < var2) or (line[2] == ">" and var1 > var2) or (line[2] == "=" and var1 == var2):
                i = int(line[4]) - 1
        elif line[0] == "in":
            variables[line[1]] = int(input("Enter a number: "))
        i += 1
