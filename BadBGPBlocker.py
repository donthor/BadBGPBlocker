import ipaddress
import json
import requests
from jinja2 import Environment, FileSystemLoader

asforprefix_baseurl = 'https://api.bgpview.io/prefix/'
prefixesforas_baseurl = 'http://stat.ripe.net/data/announced-prefixes/data.json?preferred_version=1.1&resource='
bad_subnet = ''
config = {}

def get_as():
  TheResponse = requests.get(asforprefix_baseurl + bad_subnet)
  data = json.loads(TheResponse.content)
  return data['data']['asns'][0]['asn']
  
def get_prefixes_per_asn(asn):
  myResponse = requests.get(prefixesforas_baseurl+asn)
  if(myResponse.ok):
    jData = json.loads(myResponse.content)
    prefix_list = []
    for data in jData['data']['prefixes']:
      if '.' in data['prefix']:  
          # prefix_list += f"IPv4 Prefix: {data['prefix']}\n"
          prefix_list.append(data['prefix'])
    return prefix_list
  else: myResponse.raise_for_status()

while True:
    bad_subnet = input ('Please enter the offending IPv4 subnet: ')
    verifyip = ipaddress.IPv4Network(bad_subnet)
    if verifyip.prefixlen <= 24 and verifyip.is_global:
      break
bad_asn = get_as()
print ()
print (f'The ASN this subnet originates is found to be: {bad_asn}') 
all_the_prefixes = get_prefixes_per_asn(str(bad_asn))
print ()
print ('The other IPv4 prefixes associated with this ASN are:')
print (*all_the_prefixes, sep = '\n')
print ()
while True:
  try:
    one_all_or_none = input (f'Did you want to only block {bad_subnet}? or all IPv4 Prefixes?\n("1" for one, "2" for all, or "q" to quit):')
    if one_all_or_none.lower() == 'q':
      break
    elif one_all_or_none == '1':
      config['prefixes'] = [bad_subnet]
      break
    elif one_all_or_none == '2':
      config['prefixes'] = all_the_prefixes
      break
  except Exception as e:
    print(e)

prefix_name = input('What is the Prefix List name you want to use? ')
config['prefix_list_name'] = prefix_name
bgp_as_num = input('What is your BGP AS number? ')
config['as_num'] = bgp_as_num
while True:
  try:
    bgp_neighbor_ip = input('What is the BGP neighbor IP address? ')
    if ipaddress.IPv4Network(bgp_neighbor_ip):
      break
  except Exception as e:
    print(e)
config['neigh_ip'] = bgp_neighbor_ip
env = Environment(loader = FileSystemLoader(''), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('BGPtemplate.j2')
# print(config)
print(template.render(config))

