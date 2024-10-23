# Simple `cron`
`scron` is a command line tool built with the main target of easing the syntax of `cron`; making it more user-friendly and ready to use right from the terminal.\
It also adds logging for the commands scheduled and adds the ability to schedule multiple commands together to be executed at the same specified time.

The main syntax goes as follows (see some examples below):\
`scron -t "DAY MONTH @ DIGITAL_TIME PERIOD" -f FILE_NAME` or `-c COMMAND` where you can choose to either specify a bunch of commands in a file to be scheduled together or schedule one commands right away.

Run `scron -h` to view all available options.

### Timing formats
The dates follow an abbreviated form:

Months `Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec`

Days of the week `Sun Mon Tue Wed Thu Fri Sat`

Days of the month `1-31`

Time of the day `1-12`

Period of the time `am/pm`

`scron` is case insensitive; `am` is the same as `AM` the same as `Am` etc.

<mark>`scron` is not responsible for scheduled commands' syntax or date correctness (ex: 31 Sep which doesn't exist).</mark>

### Dependencies
- `crontab` for Debian-based or `cronie` for Arch-based machines.
- `python`

### Exit codes
Below are a few exit codes to identify what kind of problem `scron` might have run into.
#### Basic command syntax
`1`: Invalid option\
`2`: Incomplete command\
`4`: Missing arguments for an option\
`5`: Invalid command syntax

#### Cancel
`101`: Abort/Cancel

#### Error
`201`: Scheduled commands' error\
`202`: Time syntax error\
`203`: No file found\
`204`: No scheduled commands found\
`255`: Unknown error

### Examples

`scron -t "14 Sep @ 8:22 AM" -f "./commands.txt"` will the schedule the commands in the file to run on the 14th of September at 8:22 am.

`scron -c "echo 'Hello World' > /home/user/Desktop/output.txt" -t "Sat @ 9:00 pm"` will the schedule the echo command to output the text to the file every Saturday of every month at 9:00 pm.

#### Other few timing variants:

`Fri Oct`; every Friday of October\
`Aug`; the whole month of august
