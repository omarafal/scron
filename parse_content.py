import sys

content = sys.stdin.read()

lines = content.split("\n")

with open("cmds.tmp", "w") as f:
    for line in lines:
        # ignore empty lines:
        if line.strip() != "":
            #print(f"{line} >> ./logs/scron_commands.log\n")
            f.write(f"{line} >> ./logs/scron_output.log 2>> ./logs/scron_error.log\n")
