import boto3

client = boto3.client('ec2')
response_vpc = client.describe_vpcs()
for r in response_vpc['Vpcs']:
    if(r['IsDefault']):
        print('Default VPC: ',r['VpcId'])
        default_vpc = r['VpcId']

print('Instances with size m5.large: ')
response_ec2 = client.describe_instances(Filters=[
        {
            'Name': 'network-interface.vpc-id',
            'Values': [
                default_vpc,
            ]
        },{
            'Name': 'instance-type',
            'Values':['m5.large']
        }
    ])
for r in response_ec2['Reservations']:
    for i in r['Instances']:
        print(i['InstanceId'],end=' ')
        for t in i['Tags']:
            if(t['Key'] == 'Name'): print(t['Value'])
            else: print()
