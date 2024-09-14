# Simple `cron`

`scron` is not responsible for command syntax or date correctness (ex: 31 Sep which doesn't exist)

### Exit codes:
#### Basic command syntax
`1`: Invalid option\
`2`: Incomplete command\
`4`: Missing arguments for an option

#### Cancel
`101`: Abort/Cancel

#### Error
`201`: Scheduled commands' error\
`202`: Time syntax error\
`203`: No file found\
`204`: No scheduled commands found\
`255`: Unknown error

#### Examples
