from pyclearpass import *
import logging



'''


username = "apiadmin"
password = "siesta3"

token="90e7f1102aeaa20c58ef63ee141a5bd0f41ed625"

# login = ClearPassAPILogin(server="http://10.132.0.195/api",granttype="password",password=password, username=username, verify_ssl=False)

# login = ClearPassAPILogin(server="https://10.132.0.195:443/api",api_token="90e7f1102aeaa20c58ef63ee141a5bd0f41ed625", verify_ssl=False)

clientid = "myapiclient"
clientsecret = "8gcHr8tFmI/pSRS762s2YzBCj53vMKHKH3QwGdi0uQ/9"


tron="tron"
tron_secret="ZBblcT72USw50Wcol9dS0p5oczcN/c1+zKq/sEKsJtFv"
'''
user = "apicreds"
api_secret = "xRb0z4ghL9ySUNcyTdigPZVF+HvVG0myZsP2IhfP8/0C"

login = ClearPassAPILogin(server="https://10.132.0.195:443/api",granttype="client_credentials",
clientsecret=api_secret, clientid=user, verify_ssl=False)

nad = {"name": "Glarn",
       "radsec_enabled": "false",
       "ip_address": "10.10.1.3",
       "radius_secret": "zsdfsdfsd",
       "tacacs_secret": "oiuxhfuhdf",
       "vendor_name": "Unix",
       "vendor_id": "10888",
       "coa_capable": "true",
       "coa_port": "3799"}

print(nad)

response = ApiPolicyElements.new_network_device(login,body=nad)
print(response)

'''
description="HPE 2520-8-PoE Switch"
name="HP 2520-8"
coaPort="3799"
radsecEnabled="false"
coaCapable="true"
vendorName="HP 2520-8"
tacacsSecret="dsrgsgsggsdd"
radiusSecret=""
ipAddress="10.132.0.62"
'''
