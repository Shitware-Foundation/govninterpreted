import sys

if len(sys.argv) < 2:
    exit()
file = sys.argv[1]
with open(file) as _:
    code = _.read()

def Print(message):
    sys.stdout.write(str(message) + "\n")
    sys.stdout.flush()
def Input(message):
    sys.stdout.write(str(message))
    sys.stdout.flush()
    buffer = ""
    for i in sys.stdin:
        buffer += i
        if "\n" in i:
            break
    return buffer.strip()

lines = code.strip().split("\n")

VARIABLES = {"pashalko": "Hello"}

def MainParser(lines):
    global VARIABLES
    line = 0
    for i in lines:
        line += 1
        if i.startswith("print "):
            args = i[6:]
            if args not in VARIABLES:
                if not args.startswith('"') and not args.endswith('"'):
                    try:
                        Print(int(args))
                    except:
                        print(f'Error in line {line}! Variable not defined!')
                        exit(1)
                else:
                    args = args.replace('"', '')
                    Print(args)
            else:
                Print(VARIABLES[args])
        if i.startswith("let "):
            args = i[4:]
            try:
                args = args.split(" = ")
            except:
                print(f"Error in line {line}! Variables syntax: let variable = data/expression")
                exit(1)
            data0 = args[0]
            data1 = args[1]
            # If imm is variable
            if data1 in VARIABLES:
                VARIABLES[data0] = data1
                continue
            # If imm not is string
            if not data1.startswith('"') and not data1.endswith('"'):
                # If imm is integer
                try:
                    VARIABLES[data0] = int(data1)
                    continue
                except:
                    pass
                # If imm is expression
                try:
                    VARIABLES[data0] = eval(data1)
                    continue
                except:
                    pass
                # Imm is string.
            else:
                # Imm is string!
                VARIABLES[data0] = data1.replace('"', '')
        if i == "exit":
            exit(0)
        if i.startswith("input "):
            args = i[6:]
            try:
                args = args.split(" > ")
            except:
                print(f"Error in line {line}! Input syntax is: input \"Whats your name?: \" > var")
            welcome = args[0]
            var = args[1]
            if not welcome.startswith('"') and not welcome.endswith('"'):
                wlc = VARIABLES[welcome]
            else:
                wlc = welcome.replace('"', '')
            VARIABLES[var] = Input(wlc)
MainParser(lines)
