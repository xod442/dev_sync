
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

'''
from flask import Flask, request, render_template, abort, redirect, url_for
import pymongo
import os
from jinja2 import Environment, FileSystemLoader
from bson.json_util import dumps
from bson.json_util import loads
from utility.get_imc_hosts import get_imc_documents
from utility.get_cp_hosts import get_cp_documents
from utility.transfer_devs import transfer_devs
import ssl
import urllib3
import datetime




import subprocess
import logging
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#
app = Flask(__name__)

logging.basicConfig(filename="dev.log",
					format='%(asctime)s %(message)s',
					filemode='a')

# A dictionary of the mongo database credentials
config = {
    "username": "admin",
    "password": "siesta3",
    "server": "mongo",
}

# Setup database connetor
connector = "mongodb://{}:{}@{}".format(config["username"], config["password"], config["server"])
client = pymongo.MongoClient(connector)

#set mongo database
db = client["devsync"]

'''
#-------------------------------------------------------------------------------
Main Page
#-------------------------------------------------------------------------------
'''

@app.route("/", methods=('GET', 'POST'))
def login():
    # Get imc and clearpass documents and make selection lists for home screen
    imc_documents = get_imc_documents(db)
    imc_list = []
    for i in imc_documents:
        info = str(i[0]) + '-' + i[1]
        imc_list.append(info)


    cp_documents = get_cp_documents(db)
    cp_list = []
    for c in cp_documents:
        info = str(c[0]) + '-' + c[1]
        cp_list.append(info)



    message = "System Ready"
    return render_template('home.html', message=message, imc_list=imc_list, cp_list=cp_list)


'''
#-------------------------------------------------------------------------------
Home
#-------------------------------------------------------------------------------
'''

@app.route("/home/<string:message>", methods=('GET', 'POST'))
def home(message):

    # Get imc and clearpass documents and make selection lists for home screen
    imc_documents = get_imc_documents(db)
    imc_list = []
    for i in imc_documents:
        info = str(i[0]) + '-' + i[1]
        imc_list.append(info)


    cp_documents = get_cp_documents(db)
    cp_list = []
    for c in cp_documents:
        info = str(c[0]) + '-' + c[1]
        cp_list.append(info)


    return render_template('home.html', message=message, imc_list=imc_list, cp_list=cp_list)


'''
#-------------------------------------------------------------------------------
IMC Creds
#-------------------------------------------------------------------------------
'''
@app.route("/add_imc_creds", methods=('GET', 'POST'))
def add_imc_creds():

    return render_template('imc_creds.html')

@app.route("/add_imc_creds_post", methods=('GET', 'POST'))
def add_imc_creds_post():
    # Get count
    highest_record = db.imc_creds.find({}).sort("number", pymongo.DESCENDING).limit(1)
    count = loads(dumps(highest_record))
    if count == []:
        number = 1
    else:
        number = count[0]["number"] + 1

    entry = {
        "imc_name": request.form['imc_name'].replace("'", ""),
        "imc_ip": request.form['imc_ip'].replace("'", ""),
        "imc_user": request.form['imc_user'].replace("'", ""),
        "imc_password": request.form['imc_password'].replace("'", ""),
        "number": number
    }
    res = db.imc_creds.insert_one(entry)

    message = "IMC credentials for %s have been saved in the database" % (entry["imc_ip"])
    logging.warning(message)
    return render_template('home.html', message=message)

'''
#-------------------------------------------------------------------------------
Clearpass Creds
#-------------------------------------------------------------------------------
'''
@app.route("/add_cp_creds", methods=('GET', 'POST'))
def add_cp_creds():
    return render_template('cp_creds.html')

@app.route("/add_cp_creds_post", methods=('GET', 'POST'))
def add_cp_creds_post():
    # Get count
    highest_record = db.cp_creds.find({}).sort("number", pymongo.DESCENDING).limit(1)
    count = loads(dumps(highest_record))
    if count == []:
        number = 1
    else:
        number = count[0]["number"] + 1

    entry = {
        "cp_name": request.form['cp_name'].replace("'", ""),
        "cp_ip": request.form['cp_ip'].replace("'", ""),
        "cp_user": request.form['cp_user'].replace("'", ""),
        "cp_password": request.form['cp_password'].replace("'", ""),
        "number": number
    }
    res = db.cp_creds.insert_one(entry)

    message = "Clearpass credentials for %s have been saved in the database" % (entry["cp_ip"])
    logging.warning(message)
    return render_template('home.html', message=message)


'''
#-------------------------------------------------------------------------------
Transfer Devices
#-------------------------------------------------------------------------------
'''

@app.route("/transfer_warn", methods=('GET', 'POST'))
def transfer_warn():
    source = request.form['source']
    destination = request.form['destination']

    return render_template('transfer_warn.html', source=source, destination=destination)

@app.route("/transfer", methods=('GET', 'POST'))
def transfer():
    source = request.form['source']
    temp = source.split('-')
    number = temp[0]
    number = int(number)
    imc = db.imc_creds.find({"number":number})
    imc = loads(dumps(imc))
    imc_info = [imc[0]['imc_name'],
               imc[0]['imc_ip'],
               imc[0]['imc_user'],
               imc[0]['imc_password']]

    destination = request.form['destination']
    temp = destination.split('-')
    number = temp[0]
    number = int(number)
    cp = db.cp_creds.find({"number":number})
    cp = loads(dumps(cp))
    cp_info = [cp[0]['cp_name'],
               cp[0]['cp_ip'],
               cp[0]['cp_user'],
               cp[0]['cp_password']]

    #transfer_devs(imc_info,cp_info)

    message = "Devices have been transfered between %s and %s" % (imc_info[1], cp_info[1])
    logging.warning(message)

    return redirect(url_for('home', message=message))
