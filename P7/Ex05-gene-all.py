import http.client
import json
import termcolor
from termcolor import *
from Seq1 import *
GENES = {'FRAT1':'ENSG00000165879', 'ADA':'ENSG00000196839',
         'FXN':'ENSG00000165060', 'RNU6_269P':'ENSG00000212379',
         'MIR633':'ENSG00000207552', 'TTTY4C':'ENSG00000228296',
         'RBMY2YP': 'ENSG00000227633', 'FGFR3':'ENSG00000068078',
         'KDR':'ENSG00000128052', 'ANK2':'ENSG00000145362'}
BASES= ["A","C","T","G"]
server = 'rest.ensembl.org'
endpoint = '/sequence/id/'

for item in GENES:
    parameters = GENES[item]+'?content-type=application/json'

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
    print(item)
    termcolor.cprint("Description: ","green", end="")
    print(f"{api_info['desc']}")

    seq= Seq(api_info['seq'])
    termcolor.cprint("Total length: ","green", end="")
    print(seq.len())
    for base in BASES:
        cbase= colored(base,'blue')
        percent = seq.count_base(base)/seq.len()*100
        print(f"{cbase}: {seq.count_base(base)} ({percent.__round__(2)}%)")

    termcolor.cprint("Most frequent base: ","green", end="")
    max= 0
    for item in seq.seq_count():
        if seq.seq_count()[item] > max:
            max= seq.seq_count()[item]
            Key= item
    print(Key)
