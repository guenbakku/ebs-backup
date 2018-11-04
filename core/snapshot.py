# coding: utf-8

import time
import utils

class Snapshot(object):
    ''' Represent Snapshot class '''

    def __init__(self, volume, raw):
        ''' Instance constructor

        Agrs:
            obj: self
            obj: volume object
            obj: snapshot raw object (which was returned from boto3 api)

        Returns: void

        '''
        self._volume = volume
        self._raw = raw

    def get_id(self):
        return self._raw.id

    def is_expired(self):
        ''' Check if a snapshot has expired of not
        If keep_days < 0, the snapshot is kept permanently
        '''
        keep_days = self._volume.get_keep_days()
        keep_seconds = keep_days * 86400
        now = int(time.time())
        start_time = utils.utc2epoch(self._raw.start_time)
        is_expired = keep_seconds >= 0 and now - start_time > keep_seconds
        return is_expired

    def create_tags(self, Tags):
        ec2 = self._volume._ec2.get_resource()
        target_tag = self._volume._config['target_tag']
        ec2.create_tags(
            Resources=[self.get_id()],
            Tags=Tags
        )

    def delete(self):
        ec2 = self._volume._ec2.get_client()
        ec2.delete_snapshot(SnapshotId=self.get_id())