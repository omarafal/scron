import sys

#content = sys.stdin.read()

file = sys.argv[1]
time = sys.argv[2].lower()

time_list =  ["*", "*", "*", "*", "*"]

days_list =  ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
months_list = ["" ,"jan", "feb", "mar", "apr", "may", "Jjun", "jul", "aug", "sep", "oct", "nov", "dec"]

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
splf_half = f_half.split()

if len(splf_half) == 1:
    # either a number (1-31) or day (Sun, Mon, Tue, Wed, Thu, Fri, Sat)
    if splf_half[0] in [str(x) for x in range(1, 32)]:
        #print("This is a number")
        time_list[2] = splf_half[0]
    elif splf_half[0] in days_list:
        #print("This is a day of the week")
        time_list[4] = str(days_list.index(splf_half[0]))
    elif splf_half[0] in months_list:
        #print("This is a day of the month")
        time_list[3] = str(months_list.index(splf_half[0]))
    else:
        print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
        exit()

elif len(splf_half) == 2:
    # check first half
    # either a number (1-31) or day (Sun, Mon, Tue, Wed, Thu, Fri, Sat)
    if splf_half[0] in [str(x) for x in range(1, 32)]:
        #print("This is a number")
        time_list[2] = splf_half[0]
    elif splf_half[0] in days_list:
        #print("This is a day of the week")
        time_list[4] = str(days_list.index(splf_half[0]))
    else:
        print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
        exit()

    # check second half
    if splf_half[1] in months_list:
        #print("This is a day of the month")
        time_list[3] = str(months_list.index(splf_half[1]))

    else:
        print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
        exit()


else:
    print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
    exit()

#print(f"{" ".join(time_list)}")

# parse second half
# split second half
spls_half = s_half.split()

if len(spls_half) != 2:
    print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
    exit()

# check for am or pm
if spls_half[1] != "am" and spls_half[1] != "pm":
    print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
    exit()

period = 0 if spls_half[1] == "am" else 12
clock = spls_half[0].split(":")

# check the time
if len(clock) != 2:
    print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
    exit()

hour = int(clock[0])
minute = int(clock[1])

if hour not in range(1, 13) or minute not in range(0, 60):
    print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
    exit()

time_list[0] = str(minute)

if hour == 12:
    if period == "am":
        time_list[1] = 0
    else:
        time_list[1] = 12
else:
    time_list[1] = str(hour + period)

print(f"Final form: {" ".join(time_list)}")
"""
# prepare commands and write them to files
with open("./c/cmds.tmp", "w") as f1, open("./c/current_cmds.scron", "a") as f2:
    # log dates
    f1.write("date >> ./logs/scron_output.log && date >> ./logs/scron_error.log\n")
    for line in lines:
        # ignore empty lines:
        if line.strip() != "":
            #print(f"{line} >> ./logs/scron_commands.log\n")
            f1.write(f"{" ".join(time_list)} {line} >> ./logs/scron_output.log 2>> ./logs/scron_error.log\n")

            # add commands to list of commands disregarding the logging part
            # used for -l option
            f2.write(f"{line}\n")
"""
