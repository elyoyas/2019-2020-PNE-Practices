import http.client
import json
import termcolor

server = 'rest.ensembl.org'
endpoint = '/info/ping'
parameters ='?content-type=application/json'


print()
print(f"Server: {server}")
print(f"URL: {server + endpoint + parameters}")

conn = http.client.HTTPConnection(server)

try:
    conn.request("GET", endpoint + parameters)

except ConnectionRefusedError:
    print("ERROR Connection declined:(")

response = conn.getresponse()
print(f"Response received!: {response.status} {response.reason}")

data_ = response.read().decode("utf-8")
api_info = json.loads(data_)
PING = api_info['ping']

if PING == 1:
    print("PING OK! The data base is running")