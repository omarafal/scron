import sys

#content = sys.stdin.read()

file = sys.argv[1]
time = sys.argv[2]

# read lines from file
with open(file, "r") as read_file:
    lines = read_file.read().split("\n")

# prepare commands and write them to files
with open("./c/cmds.tmp", "w") as f1, open("./c/current_cmds.scron", "a") as f2:
    for line in lines:
        # ignore empty lines:
        if line.strip() != "":
            #print(f"{line} >> ./logs/scron_commands.log\n")
            f1.write(f"{line} >> ./logs/scron_output.log 2>> ./logs/scron_error.log\n")

            # add commands to list of commands disregarding the logging part
            # used for -l option
            f2.write(f"{line}\n")
            
