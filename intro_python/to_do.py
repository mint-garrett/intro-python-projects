import sys

#read file in
try: 
    to_do_txt = open("to_do.txt", "r")
    to_do_txt_lines = to_do_txt.readlines()
    to_do_txt.close()
except: 
    to_do_txt = open("to_do.txt", "w")
    to_do_txt.close()

if to_do_txt_lines and not to_do_txt_lines[-1].endswith("\n"):
    to_do_txt_lines[-1] += "\n"

#UI
print("\n------\nhello, and welcome to the txt to do list")
print("remove an item(rm)\nadd an item(add)\nprint to dos (print)")
print("to do file: to_do.txt\n-----")

##actual code
if len(sys.argv) < 2:
    sys.exit()

cmd_arg = sys.argv[1]
word_arg = " ".join(sys.argv[2:]) + "\n"

if cmd_arg == "add":
    print(f"adding {word_arg}")
    to_do_txt= open("to_do.txt", "w")
    to_do_txt_lines.append(word_arg)
    to_do_txt.writelines(to_do_txt_lines)
    to_do_txt.close()
elif cmd_arg == "print":
    to_do_txt = open("to_do.txt", "r")
    to_do_txt_lines = to_do_txt.readlines()
    for t in range(len(to_do_txt_lines)):
        print(to_do_txt_lines[t])
elif cmd_arg == "rm":
    print(f"removed {word_arg}")
    if word_arg in to_do_txt_lines:
        to_do_txt_lines.remove(word_arg)
        to_do_txt = open("to_do.txt", "w")
        to_do_txt.writelines(to_do_txt_lines)
        to_do_txt.close()
    else:
        print("that item was not found")
