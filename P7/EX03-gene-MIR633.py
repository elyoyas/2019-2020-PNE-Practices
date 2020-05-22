import http.client
import json
import termcolor


gene = ['MIR633','ENSG00000207552']
server = 'rest.ensembl.org'
endpoint = '/sequence/id/'
parameters ='ENSG00000207552?content-type=application/json'
IDENTIFIER = "ENSG00000207552"

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

termcolor.cprint("Gene: ","green", end="")
print(gene[0])
termcolor.cprint("Description: ","green", end="")
print(f"{api_info['desc']}")
termcolor.cprint("Bases: ","green", end="")
print(f"{api_info['seq']}")