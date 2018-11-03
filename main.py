# coding: utf-8

#
# ebsant - Take snapshot of AWS EC2's volume
#

import argparse
from core.ec2 import Ec2
from core.volume import Volume
from core.snapshot import Snapshot
from pprint import pprint

CREDIT = 'ebsant 0.1.0'

def input():
    ''' Get input from command line. '''
    parser = argparse.ArgumentParser(description="ebsant - Take snapshot of AWS EC2's volume.")
    parser.add_argument('-r', '--region', dest='region_name', action='store', required=True, help='Region name')
    parser.add_argument('-i', '--id', dest='aws_access_key_id', action='store', required=True, help='Aws access key id')
    parser.add_argument('-k', '--key', dest='aws_secret_access_key', action='store', required=True, help='Aws secret access key')
    parser.add_argument('-v', action='version', version=CREDIT)
    return parser.parse_args()

# Here we go
args = input()

Volume._config['target_tag'] = 'ebsant'

ec2 = Ec2(**vars(args))
volumes = ec2.get_volumes(
    Filters=[
        {'Name': 'tag-key', 'Values': [Volume._config['target_tag']]}
    ]
)

for volume in volumes:
    # Delete expired snapshots
    snapshots = volume.get_snapshots(
        Filters=[
            {'Name': 'volume-id', 'Values': [volume.get_id()]},
            {'Name': 'status', 'Values': ['completed']},
            {'Name': 'tag-key', 'Values': [volume.get_config('target_tag')]}
        ]
    )
    for snapshot in snapshots:
        if snapshot.is_expired():
            snapshot.delete()
            print('Deleted snapshot: %s' % snapshot.get_id())

    # Take new snapshot
    snapshot = volume.take_snapshot()
    snapshot.create_tags([
        {'Key': 'Name', 'Value': volume.get_name()},
        {'Key': volume.get_config('target_tag'), 'Value': 'snapshot'}
    ])
    print('Took snapshot of volume: %s' % volume.get_id())
