# coding: utf-8

import boto3
from volume import Volume

class Ec2(object):
    ''' Provide access to EC2 resource and client '''

    def __init__(self, **credentials):
        self._resource = boto3.resource('ec2', **credentials)

    def get_resource(self):
        return self._resource

    def get_client(self):
        return self._resource.meta.client

    def get_volumes(self, Filters):
        ec2 = self.get_resource()
        volumes = ec2.volumes.filter(Filters=Filters)
        return [Volume(self, v) for v in volumes]
