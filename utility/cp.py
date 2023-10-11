'''
     _
    | |
  __| | _____   _____ _   _ _ __   ___
 / _` |/ _ \ \ / / __| | | | '_ \ / __|
| (_| |  __/\ V /\__ \ |_| | | | | (__
 \__,_|\___| \_/ |___/\__, |_| |_|\___|
             ______    __/ |
            |______|  |___/

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0.

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "0.1.1"
__maintainer__ = "Rick Kauffman"
__status__ = "Alpha"

A script that writes network devices to clearpass

'''


from pyclearpass import *
import logging
import datetime

def cp(cp_info,dev,tacacs):


    logging.basicConfig(filename="devsync.log",
    					format='%(asctime)s %(message)s',
    					filemode='a')



    login = ClearPassAPILogin(server="https://"+cp_info[1]+":443/api",granttype="client_credentials",
    clientsecret=cp_info[3], clientid=cp_info[2], verify_ssl=False)

    # build tags
    if dev['sysDescription'] == "":
        dev['sysDescription'] = "No system description found in IMC"
    description = dev['sysDescription']

    when = str(datetime.datetime.now())
    when = when.replace(":",".")



    if dev['sysName'] == "":
        dev['sysName'] = str(when)
    name = dev['sysName']


    coa_port = "3799"
    radsec_enabled = "false"
    coa_capable = "true"

    vendor_name = "Unix"

    if dev['symbolId'] == "":
        dev['symbolId'] = "9999"
    vendor_id = dev['symbolId']

    tacacs_secret = tacacs
    radius_secret = "not-in-use"
    ip_address = dev['ip']

    network_device = {
           "description": description,
           "name": name,
           "radsec_enabled": "false",
           "ip_address": ip_address,
           "radius_secret": radius_secret,
           "tacacs_secret": tacacs_secret,
           "vendor_name": vendor_name,
           "vendor_id": vendor_id,
           "coa_capable": "true",
           "coa_port": "3799"
           }

    response = ApiPolicyElements.new_network_device(login,body=network_device)

    #logging.warning(network_device)
    #logging.warning("\n")

    #logging.warning(response)

    return response
