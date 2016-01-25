#!/usr/bin/python3

import boto3
import json

if __name__ == '__main__':

    ec2_client = boto3.client('ec2')
    ec2_filter = [{'Name': 'tag:role', 'Values': ['ecs-cluster']}]
    instances=ec2_client.describe_tags(Filters=ec2_filter)

    #get only the instance_ids
    instance_ids = []
    for i in instances['Tags']:
        instance_ids.append(i['ResourceId'])

    #get the instance IDs
    result = ec2_client.describe_instances(InstanceIds=instance_ids)

    #turn them into DNS names
    dns_names = []
    for instance_list in result['Reservations']:
        for instance in instance_list['Instances']:
            dns_names.append(instance['PublicDnsName'])

    #output as formatted json string for Ansible
    output_dict = {"ecs-hosts": {"hosts": dns_names}}
    print(json.dumps(output_dict))
