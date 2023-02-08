"""
NBasic interpreter.

Basically asm, but not as cool.

Add a bytecode compiler later?
"""

import gas

tn = gas.get("sys/names.json")

def runbas(code):
    code = code.split("\n")
    vars = {}
    i = 0
    while i < len(code):
        line = code[i].split()
        if len(line) == 0:
            i+=1
            continue
        if line[0] == "jmp":
            try:
                jump_to = int(line[1]) - 1
                if jump_to < 0 or jump_to >= len(code):
                    raise ValueError("Jump target out of range")
                i = jump_to
            except ValueError as e:
                print(f"Error: {e}")
                return
        if line[0] == "vjm":
            try:
                jump_to = vars[line[1]] - 1
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
            vars[line[1]] = None
        elif line[0] == "iov":
            if len(line) < 2:
                print("Error: Invalid IO command")
                return
            if line[1] not in vars:
                print(f"Error: Undefined variable '{line[1]}'")
                return
            print(vars[line[1]])
        elif line[0] == "ios":
            print(" ".join(line[1:]))
        elif line[0] == "jif":
            if len(line) < 5:
                print("Error: Invalid jif command")
                return
            if line[1] not in vars or line[3] not in vars:
                print(f"Error: Undefined variable in jif command")
                return
            var1 = vars[line[1]]
            var2 = vars[line[3]]
            try:
                jump_to = int(line[4]) - 1
                if jump_to < 0 or jump_to >= len(code):
                    raise ValueError("Jump target out of range")
                if (line[2] == "<" and var1 < var2) or (line[2] == ">" and var1 > var2) or (line[2] == "=" and var1 == var2):
                    i = jump_to
            except ValueError as e:
                print(f"Error: {e}")
                return
        elif line[0] == "inn":
            if len(line) < 2:
                print("Error: Invalid input command")
                return
            var_name = line[1]
            while True:
                try:
                    vars[var_name] = int(input("Enter a number: "))
                    break
                except ValueError:
                    print("Invalid input, enter a number.")
        elif line[0] == "set":
            if len(line) < 3:
                print("Error: Invalid set command")
                return
            if line[1] not in vars:
                vars[line[1]] = None
            try:
                vars[line[1]] = int(line[2])
            except ValueError:
                print(f"Error: {line[2]} is not a valid integer")
                return
        elif line[0] == "cpy":
            if len(line) < 3:
                print("Error: Invalid cpy command")
                return
            if line[1] not in vars or line[2] not in vars:
                print(f"Error: Undefined variable in cpy command")
                return
            vars[line[2]] = vars[line[1]]
        elif line[0] == "add":
            if len(line) < 3:
                print("Error: Invalid add command")
                return
            if line[1] not in vars:
                print(f"Error: Undefined variable '{line[1]}'")
                return
            try:
                vars[line[1]] += int(line[2])
            except ValueError:
                print(f"Error: {line[2]} is not a valid integer")
                return
        elif line[0] == "sbt":
            if len(line) < 3:
                print("Error: Invalid sbt command")
                return
            if line[1] not in vars:
                print(f"Error: Undefined variable '{line[1]}'")
                return
            try:
                vars[line[1]] -= int(line[2])
            except ValueError:
                print(f"Error: {line[2]} is not a valid integer")
                return
        elif line[0] == "mlt":
            if len(line) < 3:
                print("Error: Invalid mlt command")
                return
            if line[1] not in vars:
                print(f"Error: Undefined variable '{line[1]}'")
                return
            try:
                vars[line[1]] *= int(line[2])
            except ValueError:
                print(f"Error: {line[2]} is not a valid integer")
                return
        elif line[0] == "div":
            if len(line) < 3:
                print("Error: Invalid div command")
                return
            if line[1] not in vars:
                print(f"Error: Undefined variable '{line[1]}'")
                return
            try:
                vars[line[1]] //= int(line[2])
            except ValueError:
                print(f"Error: {line[2]} is not a valid integer")
                return
        elif line[0] == "inc":
            if len(line) < 2:
                print("Error: Invalid add command")
                return
            if line[1] not in vars:
                print(f"Error: Undefined variable '{line[1]}'")
                return
            vars[line[1]] += 1
        elif line[0] == "vad":
            if len(line) < 3:
                print("Error: Invalid vad command")
                return
            if line[1] not in vars:
                print(f"Error: Undefined variable '{line[1]}'")
                return
            if line[2] not in vars:
                print(f"Error: Undefined variable '{line[2]}'")
                return
            vars[line[1]] += vars[line[2]]
        elif line[0] == "vsb":
            if len(line) < 3:
                print("Error: Invalid vsb command")
                return
            if line[1] not in vars:
                print(f"Error: Undefined variable '{line[1]}'")
                return
            if line[2] not in vars:
                print(f"Error: Undefined variable '{line[2]}'")
                return
            vars[line[1]] -= vars[line[2]]
        elif line[0] == "vml":
            if len(line) < 3:
                print("Error: Invalid vml command")
                return
            if line[1] not in vars:
                print(f"Error: Undefined variable '{line[1]}'")
                return
            if line[2] not in vars:
                print(f"Error: Undefined variable '{line[2]}'")
                return
            vars[line[1]] *= vars[line[2]]
        elif line[0] == "vdi":
            if len(line) < 3:
                print("Error: Invalid vdi command")
                return
            if line[1] not in vars:
                print(f"Error: Undefined variable '{line[1]}'")
                return
            if line[2] not in vars:
                print(f"Error: Undefined variable '{line[2]}'")
                return
            vars[line[1]] //= vars[line[2]]
        elif line[0] == "end":
            return
        i += 1



def run(f):
    try:
        fi = open(f, "r")
    except FileNotFoundError:
        print(tn[404])
        return
    code = fi.readlines()
    return runbas(code)


if __name__ == "__main__":
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    code = ""
    for s in contents:
        code += s + "\n"
    runbas(code)