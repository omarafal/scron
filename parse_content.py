import sys

#content = sys.stdin.read()

file = sys.argv[1]
time = sys.argv[2]

# read lines from file
with open(file, "r") as read_file:
    lines = read_file.read().split("\n")

# PARSE TIME
split_time = time.split("@")

if len(split_time) != 2:
    print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
    exit()

f_half = split_time[0]
s_half = split_time[1]

# parse first half
# split first half
splf_half = f_half.split(" ")

if len(splf_half) == 1:
    # either a number (1-31) or day (Sun, Mon, Tue, Wed, Thu, Fri, Sat)
   if splf_half[0] in range(1, 32):
       pass
   elif splf_half[0] in ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]:
       pass
   else:
       print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
       exit()


"""
# prepare commands and write them to files
with open("./c/cmds.tmp", "w") as f1, open("./c/current_cmds.scron", "a") as f2:
    # log dates
    f1.write("date >> ./logs/scron_output.log && date >> ./logs/scron_error.log\n")
    for line in lines:
        # ignore empty lines:
        if line.strip() != "":
            #print(f"{line} >> ./logs/scron_commands.log\n")
            f1.write(f"{line} >> ./logs/scron_output.log 2>> ./logs/scron_error.log\n")

            # add commands to list of commands disregarding the logging part
            # used for -l option
            f2.write(f"{line}\n")
   """         
