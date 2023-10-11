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

Written by Rick Kauffman
Github: https://github.com/xod442/zero.git

Note: A script to fetch clearpass documents from the mongoDB

'''
from bson.json_util import dumps
from bson.json_util import loads
#Script to get all logs from database
def nadclient(dev,tacacs):
    # build tags
    if dev['typeName'] == "":
        dev['typeName'] = "Not an SMNP Device"
    description = dev['typeName']
    if dev['sysName'] == "":
        dev['sysName'] = "No system name found imn IMC"
    name = dev['sysName']
    coaPort = "3799"
    radsecEnabled = "false"
    coaCapable = "true"
    if dev['symbolName'] == "":
        dev['symbolName'] = "Unix"
    vendorName = dev['symbolName']
    tacacsSecret = tacacs
    radiusSecret = ""
    ipAddress = dev['ip']

    outline = '<NadClient description="'+str(description)+'" name="'   \
                           +str(name)+'" coaPort="'          \
                           +str(coaPort)+'" radsecEnabled="'       \
                           +str(radsecEnabled)+'" coaCapable="' \
                           +str(coaCapable)+'" vendorName="'    \
                           +str(vendorName)+'" tacacsSecret="'    \
                           +str(tacacsSecret)+'" radiusSecret="'  \
                           +str(radiusSecret)+'" ipAddress="'  \
                           +str(ipAddress)+'"/>'

    return outline
