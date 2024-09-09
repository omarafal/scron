import sys

content = sys.stdin.read()

lines = content.split("\n")

with open("./c/cmds.tmp", "w") as f1, open("./c/current_cmds.scron", "a") as f2:
    for line in lines:
        # ignore empty lines:
        if line.strip() != "":
            #print(f"{line} >> ./logs/scron_commands.log\n")
            f1.write(f"{line} >> ./logs/scron_output.log 2>> ./logs/scron_error.log\n")

            # add commands to list of commands disregarding the logging part
            # used for -l option
            f2.write(f"{line}\n")
