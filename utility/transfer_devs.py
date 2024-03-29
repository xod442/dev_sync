'''
     _
    | |
  __| | _____   _____ _   _ _ __   ___
 / _` |/ _ \ \ / / __| | | | '_ \ / __|
| (_| |  __/\ V /\__ \ |_| | | | | (__
 \__,_|\___| \_/ |___/\__, |_| |_|\___|
             ______    __/ |
            |______|  |___/
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to
do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Note: A script to transfer device information from IMC to Clearpass

'''
from bson.json_util import dumps
from bson.json_util import loads
import time
import os
import requests
from pyarubaimc.auth import *
from pyarubaimc.device import *
from utility.nad_client import nadclient
from utility.cp import cp
import logging


#Script to get all logs from database
def transfer_devs(imc_info=None,cp_info=None,tacacs=None):

    device_counter = 0

    f = open("nadclient.xml","w")

    logging.basicConfig(filename="dev.log",
    					format='%(asctime)s %(message)s',
    					filemode='a')



    imc_ip = imc_info[1]
    imc_user = imc_info[2]
    imc_password = imc_info[3]


    # Configuring a connection to the VSD API

    auth = IMCAuth("https://", imc_ip, "8443", imc_user, imc_password)

    # IMC has a habit of denying the first request...try twice!
    # Get devices from IMC
    try:
        dev_list = get_all_devs( auth.creds, auth.url)
        assert type(dev_list) is list
    except:
        pass
    # Get real time alarms from IMC
    try:
        dev_list = get_all_devs( auth.creds, auth.url)
        assert type(dev_list) is list
    except:
        status = "Failure to communicate with IMC"


    for dev in dev_list:

        # Create a NadClient XML entry and write to file.
        # nad_client = nadclient(dev,tacacs)

        #logging.warning(nad_client)
        #logging.warning("\n")

        # f.write(nad_client)
        # f.write("\n")

        # Write the device to clearpass
        response = cp(cp_info,dev,tacacs)

        device_counter = device_counter + 1

    f.close

    status = "Fetched Devices from IMC and transfered to ClearPass"
        #for alarm in alarms:
    return status, device_counter
