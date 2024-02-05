import requests

data = {"connector_id": 1, "id_tag": "100079"}

response = requests.post("http://test.tpterp.com:8082/remote_start")
