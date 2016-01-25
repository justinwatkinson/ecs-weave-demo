#!/usr/bin/python

import boto3

if __name__ == '__main__':

    ec2_client = boto3.client('ec2', region_name='us-west-2')
    ec2_filter = [{'Name': 'tag:role', 'Values': ['ecs-cluster']}]
    instances=ec2_client.describe_tags(Filters=ec2_filter)

    #get only the instance_ids
    instance_ids = []
    for i in instances['Tags']:
        instance_ids.append(i['ResourceId'])

    #get the instance IDs
    result = ec2_client.describe_instances(InstanceIds=instance_ids)

    #turn them into IP Addresses
    ipv4_addresses = []
    for instance_list in result['Reservations']:
        for instance in instance_list['Instances']:
            ipv4_addresses.append(instance['PrivateIpAddress'])

    #output as space-delimited String
    print(str(' '.join(ipv4_addresses)))
