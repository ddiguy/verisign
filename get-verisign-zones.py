#!/usr/local/bin/python3.6
import time
from datetime import date
import datetime
import json
import requests
import sys
from os.path import expanduser
from itertools import groupby
# Ignoring SSL warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

"""
================================================================================
Purpose and usage
================================================================================
Written by Brian Bullard, https://github.com/ddiguy/

https://twitter.com/BrianBullard94

Purpose of script is to export domains from Verisign

This script assumes that you have created an API key.  If you haven't created
a key, then follow their instructions to do so.

Once the key is created, update these two variables:
1)  apikey
2)  account_id

You can see the documentation for their REST API:
https://mdns.verisign.com/rest/rest-doc/index.html

================================================================================
Variables
================================================================================
"""

def keyfunc(s):
    """
    Sorts sets based on numbers so that zones appear in order in output file
    Common usage is:
    sorted(my_set, key=keyfunc)
    """
    return [int(''.join(g)) if k else ''.join(g) for k, g in groupby('\0'+s, str.isdigit)]

# Date and time
today = datetime.date.today ()
tday = today.strftime ("%Y-%m-%d")

"""
Proxy settings
If you need to set a proxy, then change this line in the script:
    verify=False
to
    proxies=proxyDict, verify=False

You will also need to specify the proxy in these variables
"""
http_proxy = "http://proxy.example.com:8080"
https_proxy = "https://proxy.example.com:8080"
proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy
            }

# Login credentials
apikey = 'apikeyvalue'
account_id = 'accountidvalue'

# Verisign API
base_url = 'https://mdns.verisign.com/mdns-web/api/v1/accounts/' + account_id


# Output file
fileloc = expanduser('~') + '/'
zone_list_vs = fileloc + tday + '_verisign_zones.csv'

"""
================================================================================
Getting domains from Verisign
================================================================================
"""

# Create set to store zone names
VZ = set()
try:
    """
    Assuming you have 10,000 or less zones with Verisign
    They limit the return results to 500 per page.  Increase the
    enumerate number from 21 to allow you to export all zones.
    For example, if you have 15,000 zones change 21 to 31.
    """
    h = enumerate(range(1, 21), 1)
    for i in h:
        try:
            query =  base_url + '/zones?page='+str(i[1])+'&per_page=500'
            r = requests.get(query, 
                headers={'Authorization ':'Token ' + apikey,
                'Connection':'close', 'Accept':'application/json',
                'Content-Type':'application/json'},
                verify=False)
            rz = json.loads(r.text)
            w = rz['zones']
            for j in w:
                VZ.add(j['zone_name'])
        except Exception as e:
            pass
except Exception as e:
    print('Unable to get zones - '+str(e))
    sys.exit()

# Add results to output file
try:
    if len(VZ) > 0:
        with open(zone_list_vs, 'a') as f:
            print('Exported '+str(len(VZ))+' zones')
            a = sorted(VZ, key=keyfunc)
            for i in a:
                f.write(i+'\n')
except Exception as e:
    print('Problem getting zones.  Set is empty - '+str(e))

