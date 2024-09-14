import sys

def set(file_cmd, time, directory, is_cmd="no"):
    
    if is_cmd == "no":
        with open(file_cmd, "r") as read_file:
            lines = read_file.read().split("\n")
    
    elif is_cmd == "cmd":
        line = file_cmd

    # prepare commands and write them to files
    # write to temp files first
    with open(f"{directory}/commands/verbose_cmds.tmp", "w") as f1, open(f"{directory}/commands/short_cmds.tmp", "w") as f2:
        # log dates
        f1.write(f"{time} date +'[%a %I:%M:%S]' > >(tee -a {directory}/logs/scron_output.log) && date > >(tee -a {directory}/logs/scron_error.log)\n")
       
        if is_cmd == "no":
            for line in lines:
                # ignore empty lines:
                if line.strip() != "":
                    #print(f"{line} >> ./logs/scron_commands.log\n")
                    f1.write(f"{time} {line} > >(tee -a {directory}/logs/scron_output.log) 2> >(tee -a {directory}/logs/scron_error.log)\n")

                    # add commands to list of commands disregarding the logging part
                    # used for -l option
                    f2.write(f"{line}\n")
        
        elif is_cmd == "cmd":
            
            #print(f"{line} >> ./logs/scron_commands.log\n")
            f1.write(f"{time} {line} > >(tee -a {directory}/logs/scron_output.log) 2> >(tee -a {directory}/logs/scron_error.log)\n")

            # add commands to list of commands disregarding the logging part
            # used for -l option
            f2.write(f"{line}\n")
