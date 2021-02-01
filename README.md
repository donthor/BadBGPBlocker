# BadBGPBlocker

Now Featured on The Cisco Learning Network!

https://learningnetwork.cisco.com/s/question/0D53i00000xmv3F/blocking-bad-bgp-neighbors-with-python-with-patrick-rockholz

## What does this code do

This public repo contains python code that can be used to block one or more IPv4 subnets from BGP neighborships


## What does it solve

This code will generate Cisco IOS/IOS-XE CLI configuration to deny IPv4 prefixes from populating BGP routes by retreiving data from BGPView API. BGPView is a simple API allowing consumers to view all sort of analytics data about the current state and structure of the internet.
This code can be tested using the [IOS XE on CSR Latest Code AlwaysOn](https://devnetsandbox.cisco.com/RM/Diagram/Index/38ded1f0-16ce-43f2-8df5-43a40ebf752e?diagramType=Topology) DevNet Sandbox.


## Python Environment Setup

It is recommended that this code be used with Python 3.7.x or later.
It is highly recommended to leverage Python Virtual Environments (venv).

Follow these steps to create and activate a venv.
```
# OS X or Linux
virtualenv venv --python=python3.6
source venv/bin/activate
```

## Installation
The three files (BadBGPBlocker.py, BGPTemplate.j2 and env_ver.py) should be saved in the same folder.
Also the following python libraries should be installed
```
pip install -r requirements.txt
```
## Example Output
By running this script, you will be asked to input an IPv4 prefix that is the offender.
Once retrieved, you will be displayed the BGP AS number where the prefix origninated along with other prefixes associated with it.
You will then be prompted to choose to block only the originally inputed prefix or all prefixes associated with the ASN.

```
(workingdir) BadBGPBlocker% python BadBGPBlocker.py        
Please enter the offending IPv4 subnet: 192.160.10.0/24

The ASN this subnet originates is found to be: 25577

The other IPv4 prefixes associated with this ASN are:
185.229.20.0/23
195.210.54.0/23
91.212.108.0/24
195.135.208.0/22
109.104.96.0/19
185.174.224.0/24
91.206.118.0/24
185.5.88.0/22
185.55.252.0/24
5.133.184.0/21
179.63.32.0/20
91.206.118.0/23
193.93.84.0/22
193.105.51.0/24
62.69.143.0/24
83.142.64.0/21
194.50.54.0/24
82.197.64.0/19
31.3.208.0/20
179.63.0.0/20
192.160.10.0/24
37.58.24.0/21
85.159.88.0/21
91.206.119.0/24
185.229.22.0/23
84.45.0.0/17
193.105.172.0/24
81.27.64.0/19

Did you want to only block 192.160.10.0/24? or all IPv4 Prefixes?
("1" for one, "2" for all, or "q" to quit):2
What is the Prefix List name you want to use? deny-list
What is your BGP AS number? 65000
What is the BGP neighbor IP address? 10.1.1.1

BGP config to deploy:
ip prefix-list deny-list deny 185.229.20.0/23
ip prefix-list deny-list deny 195.210.54.0/23
ip prefix-list deny-list deny 91.212.108.0/24
ip prefix-list deny-list deny 195.135.208.0/22
ip prefix-list deny-list deny 109.104.96.0/19
ip prefix-list deny-list deny 185.174.224.0/24
ip prefix-list deny-list deny 91.206.118.0/24
ip prefix-list deny-list deny 185.5.88.0/22
ip prefix-list deny-list deny 185.55.252.0/24
ip prefix-list deny-list deny 5.133.184.0/21
ip prefix-list deny-list deny 179.63.32.0/20
ip prefix-list deny-list deny 91.206.118.0/23
ip prefix-list deny-list deny 193.93.84.0/22
ip prefix-list deny-list deny 193.105.51.0/24
ip prefix-list deny-list deny 62.69.143.0/24
ip prefix-list deny-list deny 83.142.64.0/21
ip prefix-list deny-list deny 194.50.54.0/24
ip prefix-list deny-list deny 82.197.64.0/19
ip prefix-list deny-list deny 31.3.208.0/20
ip prefix-list deny-list deny 179.63.0.0/20
ip prefix-list deny-list deny 192.160.10.0/24
ip prefix-list deny-list deny 37.58.24.0/21
ip prefix-list deny-list deny 85.159.88.0/21
ip prefix-list deny-list deny 91.206.119.0/24
ip prefix-list deny-list deny 185.229.22.0/23
ip prefix-list deny-list deny 84.45.0.0/17
ip prefix-list deny-list deny 193.105.172.0/24
ip prefix-list deny-list deny 81.27.64.0/19
ip prefix-list deny-list permit 0.0.0.0/0 le 32
router bgp 65000
 address-family ipv4 unicast
  neighbor 10.1.1.1 prefix-list deny-list in
```

## About Me
I am a Systems Architect with Cisco focusing on Automation and Programmability.

**<a href="https://www.linkedin.com/in/patrickrockholz/" rel="nofollow">LinkedIn</a> / <a href="https://twitter.com/patrickrockholz" rel="nofollow">Twitter</a>**
