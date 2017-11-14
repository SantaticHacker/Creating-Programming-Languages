import ctypes
print("Cobol v1.0 Copyrighters will face the might of infinite jail time.")

command = input()

while command != "end program":
    if command[:8] == "console(" and command[-2:] == ");":
        print(command[8:-2])
    elif command[:4] == "web(" and command[-2:] == ");":
        message = command[4:-2]
        ctypes.windll.user32.MessageBoxW(0, message, "Enter Box", 1)
    elif command[2] == "+":
        print(int(command[0]) + int(command[4]))
    elif command[2] == "-":
        print(int(command[0]) - int(command[4]))
    elif command[2] == "/":
        print(int(command[0]) / int(command[4]))
    elif command[2] == "*":
        print(int(command[0]) * int(command[4]))
    elif command[:9] == "repeat { " and command[-3:] == " };":
        increment = 0
        while increment < int(command[9]):
            if command[11:19] == "console(" and command[-5:-3] == ");":
                print(command[19:-5])
                increment += 1
            elif command[11:15] == "web(" and command[-5:-3] == ");":
                message = command[15:-5]
                ctypes.windll.user32.MessageBoxW(0, message, "Enter Box", 1)
                increment += 1
            else:
                print(f"Error, {command} is not defined.")
    else:
        print(f"Error, {command} is not defined.")
    command = input()
