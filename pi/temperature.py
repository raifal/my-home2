import json
import requests
import os

configFilePathWindows = "D:\\development\\hsm-config.json"
configFilePath = "/home/hsm/hsm-config.json"

if os.path.exists(configFilePathWindows):
    configFilePath = configFilePathWindows

with open(configFilePath, 'r') as config_file:
    config = json.load(config_file)

temperatureJson = { "client": config["client"], "hsm-data-type": "temperature", "temperatures": [ ] }

with open('/home/hsm/my-home2/pi/sensor_mapping.json', 'r') as sensor_mapping_file:
    sensor_mapping = json.load(sensor_mapping_file)

for sensor in sensor_mapping["sensorMapping"]:
    sensorTemperature = open(sensor["path"], 'r').readline()
    temperatureJson['temperatures'].append({"id": sensor["id"], "temperature": sensorTemperature.strip() })

jsonString = json.dumps(temperatureJson, indent=4)
#print(jsonString)

headers = {'Content-type': 'application/json', 'Accept': '*/*'}
r = requests.post(config["rest-api-server-url"] + "/temperature", data=json.dumps(temperatureJson), headers=headers)
