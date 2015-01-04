ReadMe.txt

Python_AWS_SG_Auditor

This python script authorizes a IP's and ports from a list to the AWS accounts in another list. 

Requirements:
- boto 2.34 
		to install boto "pip install boto"
- IAM user for required AWS account with the minimum user policy as the following:

		{
		  "Version": "2012-10-17",
		  "Statement": [
		    {
		      "Sid": "Stmt1420314080000",
		      "Effect": "Allow",
		      "Action": [
		        "ec2:AuthorizeSecurityGroupEgress",
		        "ec2:AuthorizeSecurityGroupIngress",
		        "ec2:CreateSecurityGroup",
		        "ec2:DescribeSecurityGroups",
		        "ec2:RevokeSecurityGroupEgress",
		        "ec2:RevokeSecurityGroupIngress"
		      ],
		      "Resource": [
		        "*"
		      ]
		    }
		  ]
}

How To use:
- Make the main.py executable with "chmod +X main.py"

- Create two files, aws.conf and cidr.conf in the same directory as the "main.py" file

- In the "aws.conf" file, add the profile name as section and make two entries the aws secret key and secret key id in the following way:

	[profile name-of-the-profile]
	aws_access_key_id = AKIAJT3GBDJDNWIDE6A
	aws_secret_access_key = LPO7Tw9UDG+Zrj7GbLr+HBK7qhnonc0ijqnankkas

- In the "cidr.conf", create the ip-client name as section (Note: the section sould start with the word "CIDR") then add the info regarding the CIDR needing access i.e protocol, from port, to port and cidr in the following way:
	
	[CIDR IP-client-name]
	ip_protocol = tcp
	from_port = 6969
	to_port = 6969
	cidr_ip = 182.91.56.123/32