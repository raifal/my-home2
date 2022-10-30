from flask import Flask, jsonify, request
import mysql.connector
from datetime import datetime
import os
import json

configFilePathWindows = "D:\\development\\hsm-config.json"
configFilePath = "/home/hsm/hsm-config.json"

if os.path.exists(configFilePathWindows):
    configFilePath = configFilePathWindows

with open(configFilePath, 'r') as config_file:
    config = json.load(config_file)

app = Flask(__name__)

@app.route('/temperature/<requestDate>', methods = ['GET'])
def getTemperatureData(requestDate):
    mydb = mysql.connector.connect( host=config["database-host"], user=config["database-user"], password=config["database-password"], database=config["database"])
    cursor = mydb.cursor(buffered=True , dictionary=True)

    values = []
    sql = "SELECT create_time, json FROM hsm_temperature where create_time >= %s AND create_time < %s + INTERVAL 1 DAY"
    val = ( requestDate, requestDate)
    cursor.execute(sql, val)
    myresult = cursor.fetchall()
    for row in myresult:
        item = {}
        item['date'] = datetime.strftime( row['create_time'], '%Y-%m-%d %H:%M:%S') 
        item['temperatures'] = (eval(row['json']))
        values.append(item)

    cursor.close()
    mydb.close()
    return json.dumps(values),200,{'content-type':'application/json'}

@app.route('/temperature', methods = ['POST'])
def postTemperatureData():
    print(request.json)
    now = datetime.now()
    nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
    nowDateOnly = now.strftime("%Y-%m-%d")
    mydb = mysql.connector.connect( host=config["database-host"], user=config["database-user"], password=config["database-password"], database=config["database"])
    cursor = mydb.cursor()

    sql = "INSERT INTO hsm_temperature (create_time, json) VALUES (%s, %s)"
    val = ( nowDateTime, json.dumps(request.json['temperatures']) )
    cursor.execute(sql, val)
    mydb.commit()

    cursor.close()
    mydb.close()
    return ""


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)