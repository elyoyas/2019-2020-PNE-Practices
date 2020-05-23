import http.server
import socketserver
import termcolor
import json
from pathlib import Path

srvr = "rest.ensembl.org"
PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
conn = http.client.HTTPConnection(srvr)


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        argum = self.path.split("?")[0]

        # MAIN SITE
        if self.path == "/":
            # EACH MODULE IS IMPLEMENTED SEPARATELY FROM DIFFERENT FILES
            components = ['listSpecies.html', 'Karyotype.html', 'chromosomeLength.html']
            contents = Path('main.html').read_text()
            for i in components:
                contents += Path(i).read_text()
        # BASIC LEVEL ENDPOINTS
        elif argum == "/listSpecies":
            parameters = "content-type=application/json"
            plagueis = self.path.split("?")[1]
            ext = '/info/species?'
            api_info = contact(ext, parameters)
            total_list = "COMMON NOMENCLATURE|||TAXONOMIC NOMENCLATURE<br><br>"
            msg = plagueis.split("=")[1]
            try:
                n = 0
                if msg == "":
                    for i in api_info["species"]:
                        total_list += f'|{i["display_name"]}_______________{i["name"]}|<br>'
                elif int(msg) <= 0:
                    total_list = "Perhaps you should try a number bigger than 0"
                else:
                    for i in api_info["species"]:
                        if n < int(msg):
                            n += 1
                            total_list += f'|{i["display_name"]}_______________{i["name"]}|<br>'

                contents = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>SPECIES LIST</title>
    </head>
    <center>
    <h1 style="font-family:arial;font-size:55px;background-color: #38a3a5" >AVAILABLE SPECIES LIST</h1>
    <p style="font-family:arial;background-color: #c7f9cc"> click <a href="/">here</a> to return to the main site</p>
    <body style="background-color:#57cc99;font-family:arial">
    <p>  {total_list} </p>
    <p style="font-family:arial;background-color: #c7f9cc"> click <a href="/">here</a> to return to the main site</p>
    </center>
    </body>
    </html>"""
            except ValueError:
                print("Unexpected value requested:", msg)
                contents = Path('ERROR.html').read_text()

        elif argum == "/Karyotype":
            parameters = "content-type=application/json"
            plagueis = self.path.split("?")[1]
            darth = plagueis.split("=")[1]
            ext = '/info/assembly/'
            try:

                kartman=""
                double= False
                for n in range(0, len(darth)):
                    if darth[n]== "+":
                        kartman += "%20"
                        double= True
                    else:
                        kartman += darth[n]
                api_info = contact(ext + kartman + '?', parameters)
                corleone = api_info["karyotype"]
                heisenberg = "CHROMOSOME NAMES LIST<br><br>"
                chapo = kartman.capitalize()
                #allow for double words in input
                if double:
                    doom=str(chapo.split("%20")[0]+" "+chapo.split("%20")[1])
                else:
                    doom=chapo
                for Vito in corleone:
                    heisenberg += Vito
                    heisenberg += "<br>"
                if heisenberg=="CHROMOSOME NAMES LIST<br><br>":
                    heisenberg="Eventhough this animal is in our data, we do not have its karyotype"
                contents = f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{doom}'s Karyotipe</title>
        </head>
        <center>
        <h1 style="font-family:arial;font-size:55px;background-color: #38a3a5" >
        {doom}'s karyotype</h1>
        <p style="font-family:arial;background-color: #c7f9cc"> click <a href="/">here</a> to return to main site</p>
        <body style="background-color:#57cc99;font-family:arial">
        <p>  {heisenberg} </p>
        <p style="font-family:arial;background-color: #c7f9cc"> click <a href="/">here</a> to return to main site</p>
        </center>
        </body>
        </html>"""
            except KeyError:
                # this site offers a list of animals in case you input a wrong one
                plagueis = self.path.split("?")[1]
                darth = plagueis.split("=")[1]
                contents = f"""<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <title>Not available</title>
                        </head>
                        <center>
                        <h1 style="font-family:arial;font-size:55px;background-color: #38a3a5" >Not available</h1>
                        <p style="font-family:arial;background-color: #c7f9cc"> 
                        click <a href="/">here</a> to return to the main site</p>
                        <body style="background-color:#57cc99;font-family:arial">
                        <p>  " {darth} " is not part of our database´s animals </p>
                        <a href="/listSpecies?msg=">For more information on the available animals click here</a>
                        <p style="font-family:arial;background-color: #c7f9cc"> 
                        click <a href="/">here</a> to return to the main site</p>
                        </center>
                        </body>
                        </html>"""
        elif argum == "/ChromosomeLength":
            parameters = "content-type=application/json"
            plagueis = self.path.split("?")[1]
            species = plagueis.split("&")[0].split("=")[1]
            kartman=""
            double= False
            for n in range(0, len(species)):
                if species[n] == "+":
                    kartman += "%20"
                    double = True
                else:
                    kartman += species[n]
            chromosome = plagueis.split("&")[1].split("=")[1]
            ext = '/info/assembly/'
            try:
                api_info = contact(ext + kartman +"/"+chromosome+ '?', parameters)
                corleone = api_info["length"]
                if double:
                    doom=str(kartman.split("%20")[0]+" "+kartman.split("%20")[1])
                else:
                    doom= species
                contents= f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>CHROMOSOME LENGTH</title>
        </head>
        <center>
        <h1 style="font-family:arial;font-size:55px;background-color: #38a3a5" >
        CHROMOSOME LENGTH</h1>
        <p style="font-family:arial;background-color: #c7f9cc"> click <a href="/">here</a> to return to main site</p>
        <body style="background-color:#57cc99;font-family:arial">
        <p> The length of the {doom} chromosome {chromosome} is: <br><br> {corleone}</p>
        <p style="font-family:arial;background-color: #c7f9cc"> click <a href="/">here</a> to return to main site</p>
        </center>
        </body>
        </html>"""
            except KeyError:
                contents= Path('ERROR.html').read_text()+f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SPECIES LIST</title>
</head>
<center>
<body style="background-color:#57cc99;font-family:arial">
<p>  having trouble? <br><a href="/Karyotype?msg={kartman}">Check if your animal is in our database</a><br>
</center>
</body>
</html>"""

        else:
            contents = Path('ERROR.html').read_text()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()
        self.wfile.write(contents.encode())
        return


def contact(endpoint, parameters):
    conn.request("GET", endpoint + parameters)
    rsponse = conn.getresponse()
    data_ = rsponse.read().decode("utf-8")
    a = json.loads(data_)
    return a


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
