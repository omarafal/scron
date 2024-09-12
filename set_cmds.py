import sys

def set(file, time):
    
    with open(file, "r") as read_file:
        lines = read_file.read().split("\n")

    # prepare commands and write them to files
    with open("./commands/verbose_cmds.scron", "w") as f1, open("./c/short_cmds.scron", "a") as f2:
        # log dates
        f1.write("date >> ./logs/scron_output.log && date >> ./logs/scron_error.log\n")
        
        for line in lines:
            # ignore empty lines:
            if line.strip() != "":
                #print(f"{line} >> ./logs/scron_commands.log\n")
                f1.write(f"{time} {line} >> ./logs/scron_output.log 2>> ./logs/scron_error.log\n")

                # add commands to list of commands disregarding the logging part
                # used for -l option
                f2.write(f"{line}\n")