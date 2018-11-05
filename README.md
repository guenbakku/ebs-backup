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

## Comands

1. Execute

    ~~~
    python /path/to/main.py -r {REGION_NAME} -i {AWS_ACCESS_KEY_ID} -k {AWS_SECRET_ACCESS_KEY}
    ~~~

    Change default target tag's name with option `-t` or `--target-tag`

    ~~~
    python /path/to/main.py -t {CUSTOMIZED_TAG} -r {REGION_NAME} -i {AWS_ACCESS_KEY_ID} -k {AWS_SECRET_ACCESS_KEY}
    ~~~

2. Show help

    ~~~
    python /path/to/main.py -h
    ~~~

3. Show version info

    ~~~
    python /path/to/main.py -v
    ~~~
