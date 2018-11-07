# ebsant

Take snapshot of AWS EC2's volume

## Set target volumes

The script will take snapshot of volumes which have specific tag (default is `ebsant`).

The value of this tag is the integer declares the number of days to keep old snapshots in. If negative number is set, old snapshots will be kept permanently.

![](./docs/img/set-target-tag.png)

## Set write permission of log directory

Don't forget to set write permission of log directory (`./logs`) to the user who executes the script

~~~
$ chmod 777 /path/to/logs
~~~

## Commands

~~~
python /path/to/main.py {option} {value}
~~~

### Options

|Option|Required|Default value|Description|
|---|---|---|---|
|`-r`, `--region`|Yes|-|AWS region code|
|`-i`, `--id`|Yes|-|IAM user's AWS_ACCESS_KEY_ID|
|`-k`, `--key`|Yes|-|IAM user's AWS_SECRET_ACCESS_KEY|
|`-t`, `--target-tag`|No|'ebsant'|Target tag's name|
|`-l`, `--log`|No|'/{path_to_source}/logs/log.txt'|Path to log file|
|`-h`, `--help`|No|-|Show help|
|`-v`|No|-|Show credit info|