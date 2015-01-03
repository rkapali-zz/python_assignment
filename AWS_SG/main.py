#!/usr/bin/python
#main.py
import boto.ec2
import ConfigParser

#load config file for aws credentials and cidr list
config_aws = ConfigParser.ConfigParser()
config_aws.read("aws.conf")
config_cidr = ConfigParser.ConfigParser()
config_cidr.read("cidr.conf")
sections_aws = config_aws.sections()
sections_cidr = config_cidr.sections()

#storing variables for the IP list and ports
for ip_client in sections_cidr:
	protocol = config_cidr.get(ip_client,'ip_protocol')
	fport = int(config_cidr.get(ip_client,'from_port'))
	tport = int(config_cidr.get(ip_client,'to_port'))
	ip = config_cidr.get(ip_client,'cidr_ip')
	print "\n List of %s entries "%ip_client[5:] 
	
	# getting aws key and id for all avaialble list of AWS accounts
	for accounts in sections_aws:
		keyid = config_aws.get(accounts, 'aws_access_key_id')
		key =  config_aws.get(accounts, 'aws_secret_access_key')

		#connection to respective AWS accounts in region "us-east-1"
		conn = boto.ec2.connect_to_region("us-east-1",aws_access_key_id=keyid,aws_secret_access_key=key)

		#getting the list of security groups in the given AWS account's given region
		sglist = conn.get_all_security_groups()	
		print "\n    AWS account : %s" %accounts
		
		#first revoking given entry then authorizing the given entry to the given AWS accounts SG in the given region
		for sg in sglist:
			try:
				sg.revoke(ip_protocol=protocol, from_port=fport, to_port=tport, cidr_ip=ip)
				sg.authorize(ip_protocol=protocol, from_port=fport, to_port=tport, cidr_ip=ip)
				print "from_port:%s to_port:%s for %s have been saved in SG named %s" %(fport,tport,ip,sg.name)

			#exception handler	
			except boto.exception.EC2ResponseError:
				print "port %s already exists in %s." %(fport,sg.name)
