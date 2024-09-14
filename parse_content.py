import sys
import set_cmds

#content = sys.stdin.read()

file_cmd = sys.argv[1]
time = sys.argv[2].lower()
directory = sys.argv[3]
try:
    is_cmd = sys.argv[4]
except:
    is_cmd = "no"


time_list =  ["*", "*", "*", "*", "*"]

days_list =  ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
months_list = ["" ,"jan", "feb", "mar", "apr", "may", "Jjun", "jul", "aug", "sep", "oct", "nov", "dec"]

# PARSE TIME
split_time = time.split("@")

if len(split_time) != 2:
    print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
    exit(200)

f_half = split_time[0]
s_half = split_time[1]

# parse first half
# split first half
splf_half = f_half.split()

if len(splf_half) == 1:
    # either a number (1-31) or day (Sun, Mon, Tue, Wed, Thu, Fri, Sat)
    if splf_half[0].isdigit():
        if int(splf_half[0]) in range(1, 32):
            #print("This is a number")
            time_list[2] = str(int(splf_half[0]))
    elif splf_half[0] in days_list:
        #print("This is a day of the week")
        time_list[4] = str(days_list.index(splf_half[0]))
    elif splf_half[0] in months_list:
        #print("This is a day of the month")
        time_list[3] = str(months_list.index(splf_half[0]))
    else:
        print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
        exit(200)

elif len(splf_half) == 2:
    # check first half
    # either a number (1-31) or day (Sun, Mon, Tue, Wed, Thu, Fri, Sat)
    if splf_half[0].isdigit():
        if int(splf_half[0]) in range(1, 32):
            #print("This is a number")
            time_list[2] = str(int(splf_half[0]))
    elif splf_half[0] in days_list:
        #print("This is a day of the week")
        time_list[4] = str(days_list.index(splf_half[0]))
    else:
        print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
        exit(200)

    # check second half
    if splf_half[1] in months_list:
        #print("This is a day of the month")
        time_list[3] = str(months_list.index(splf_half[1]))

    else:
        print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
        exit(200)


else:
    print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
    exit(200)

#print(f"{" ".join(time_list)}")

# parse second half
# split second half
spls_half = s_half.split()

if len(spls_half) != 2:
    print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
    exit(200)

# check for am or pm
if spls_half[1] != "am" and spls_half[1] != "pm":
    print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
    exit(200)

period = 0 if spls_half[1] == "am" else 12
clock = spls_half[0].split(":")

# check the time
if len(clock) != 2:
    print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
    exit(200)

hour = int(clock[0])
minute = int(clock[1])

if hour not in range(1, 13) or minute not in range(0, 60):
    print("[ERROR] Wrong timing format.\nExample usage: scron -t \"23 Jan @ 8:30 AM\" -f file.txt")
    exit(200)

time_list[0] = str(minute)

if hour == 12:
    if period == 0:
        time_list[1] = "0"
    else:
        print(period)
        time_list[1] = "12"
else:
    time_list[1] = str(hour + period)

set_cmds.set(file_cmd, " ".join(time_list), directory, is_cmd)

#print(f"Final form: {" ".join(time_list)}")
