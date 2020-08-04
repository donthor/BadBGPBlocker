import ipaddress
import json
import requests

asforprefix_baseurl = 'https://api.bgpview.io/prefix/'
prefixesforas_baseurl = 'http://stat.ripe.net/data/announced-prefixes/data.json?preferred_version=1.1&resource='
checkip = True

def get_as(bad_subnet):
  TheResponse = requests.get(asforprefix_baseurl + bad_subnet)
  data = json.loads(TheResponse.content)
  return data['data']['asns'][0]['asn']
  
def get_prefixes_per_asn(asn):
  myResponse = requests.get(prefixesforas_baseurl+asn)
  if(myResponse.ok):
    jData = json.loads(myResponse.content)
    prefix_list = ''
    for data in jData['data']['prefixes']:
      if '.' in data['prefix']:  
          prefix_list += f"IPv4 Prefix: {data['prefix']}\n"
    return prefix_list
  else: myResponse.raise_for_status()

while checkip:
  bad_subnet = input ('Please enter the offending IPv4 subnet: ')
  verifyip = ipaddress.IPv4Network(bad_subnet)
  if verifyip.prefixlen <= 24 and verifyip.is_global:
    checkip = False
bad_asn = get_as(bad_subnet)
print (f'The ASN this subnet originates is found to be: {bad_asn}') 
all_the_prefixes = get_prefixes_per_asn(str(bad_asn))
print ('The other IPv4 prefixes associated with this ASN are:')
print (all_the_prefixes)
