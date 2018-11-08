# coding: utf-8

#
# ebsant - Take snapshot of AWS EC2's volume
#

import sys
import argparse
import logging.config
import config
from logging import getLogger
from core.ec2 import Ec2
from core.volume import Volume

CREDIT = 'ebsant 0.4.1'

def input():
    ''' Get input from command line. '''
    parser = argparse.ArgumentParser(description="ebsant - Take snapshot of AWS EC2's volume.")
    parser.add_argument('-r', '--region', dest='region_name', action='store', required=True, help='Region name')
    parser.add_argument('-i', '--id', dest='aws_access_key_id', action='store', required=True, help='Aws access key id')
    parser.add_argument('-k', '--key', dest='aws_secret_access_key', action='store', required=True, help='Aws secret access key')
    parser.add_argument('-t', '--target-tag', dest='target_tag', action='store', help='Target tag')
    parser.add_argument('-l', '--log', dest='log_path', action='store', help='Log file path')
    parser.add_argument('-v', action='version', version=CREDIT)
    return parser.parse_args()

# Here we go
args = input()

if args.target_tag is not None:
    Volume._config['target_tag'] = args.target_tag

if args.log_path is not None:
    if 'file' in config.logging['handlers']:
        config.logging['handlers']['file']['filename'] = args.log_path

logging.config.dictConfig(config.logging)
logger = getLogger('%s.%s' % (args.region_name, Volume._config['target_tag']))
logger.info('START')

try:
    ec2 = Ec2(
        region_name=args.region_name,
        aws_access_key_id=args.aws_access_key_id,
        aws_secret_access_key=args.aws_secret_access_key,
    )
    volumes = ec2.get_volumes(
        Filters=[
            {'Name': 'tag-key', 'Values': [Volume._config['target_tag']]}
        ]
    )

    for volume in volumes:
        # Delete expired snapshots
        snapshots = volume.get_snapshots()
        for snapshot in snapshots:
            if snapshot.is_expired():
                snapshot.delete()
                logger.info('Deleted snapshot: %s' % snapshot.get_id())

        # Create new snapshot
        snapshot = volume.create_snapshot()
        logger.info('Took snapshot of volume: %s' % volume.get_id())

    logger.info('STOP')
except Exception as e:
    logger.exception(str(e).decode('utf-8'))
    sys.exit(-1)
