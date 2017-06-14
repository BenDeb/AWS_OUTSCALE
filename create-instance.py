#!/usr/local/bin/python3
import sys
import boto3

#fonction qui va créer des instances CentOS7, t2.medium
nombre = int(sys.argv[1])
nom_region = sys.argv[2]
regions = {'euw2' : 'eu-west-2', 'use2' : 'us-east-2'}


def createInstanceEU(nombre):
    ec2.create_instances(
        ImageId='ami-d4f6551d',
        MinCount=nombre,
        MaxCount=nombre,
        KeyName='ssh-test',
        InstanceType='t2.medium')

def createInstanceUS(nombre):
    ec2.create_instances(
        ImageId='ami-d4906a30',
        MinCount=nombre,
        MaxCount=nombre,
        KeyName='ssh-nj2',
        InstanceType='t2.medium')

if nom_region == 'euw2':
    ec2 = boto3.resource('ec2', region_name='eu-west-2')
    createInstanceEU(nombre)
elif nom_region == 'use2':
    ec2 = boto3.resource('ec2', region_name='us-east-2')
    createInstanceUS(nombre)
