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

Note: A script to fetch imc documents from the mongoDB

'''
from bson.json_util import dumps
from bson.json_util import loads
#Script to get all logs from database
def get_imc_documents(db):
    imc = []
    get_imc = db.imc_creds.find({})
    json_imc = loads(dumps(get_imc))
    for imc_doc in json_imc:
        imc.append(imc_doc)

    # Make a list of IMC documents
    imc_list = []

    for i in imc:
        number = i['number']
        imc_name = i['imc_name']
        imc_ip = i['imc_ip']
        imc_user = i['imc_user']
        imc_password = i['imc_password']
        info = [number, imc_name, imc_ip, imc_user, imc_password]
        imc_list.append(info)
    return imc_list
