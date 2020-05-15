import http.server
import socketserver
import termcolor
from Seq1 import *
from pathlib import Path


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        termcolor.cprint(self.requestline, 'green')
        Swain = self.path.split("?")[0]

        if Swain in ['/']:
            contents = Path('Ex4.html').read_text()

        elif Swain in ['/ping']:
            contents = Path('PING.html').read_text()

        elif Swain in ['/get']:
            genelist = ["CACTACCCGTACAGGCACACTGGACACA", "ACGTCAGACACAGCTACGTCAGCTGACGCATA",
                        "ACGATGCACGACGTACCAGATGCACACGTTTAGC", "GATCAGAGATCACCATAGCACTTCAGCGGATCGAACAGTC", "AAACCCTTTGGGG"]
            Veigar= self.path.split("?")[1]
            Cait= Veigar.split("=")[1]
            contents =f""" <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <title>Sequence</title>
                            </head>
                            <h1 style="font-family:Arial">Sequence: {int(Cait)}</h1>
                            <body>
                            <br>
                            <p>{genelist[int(Cait)]}</p>
                            <br>
                            <a href="/">Return to main</a>
                            </body>
                            </html>"""
        elif Swain in ['/gene']:
            folder = "../Session-04/"
            seq = Seq("")
            Veigar = self.path.split("?")[1]
            Cait = Veigar.split("=")[1]
            file = folder + Cait + ".txt"
            ChoGath = str(seq.seq_read_fasta(file))
            contents=f""" <!DOCTYPE html>
                                        <html lang="en">
                                        <head>
                                            <meta charset="UTF-8">
                                            <title>Gene</title>
                                        </head>
                                        <h1 style="font-family:Arial">Gene: {Cait}</h1>
                                        <body>
                                        <br>
                                        <p>{ChoGath}</p>
                                        <br>
                                        <a href="/">Return to main</a>
                                        </body>
                                        </html>"""
        elif Swain in ['/operation']:
            sequence = str(self.path.split("?")[1].split("&")[0].split('=')[1])
            methd = str(self.path.split("&")[1].split('=')[1])
            seq= Seq(sequence)
            if methd == "Info":
                res=(f"SECUENCE:  {seq.__str__()} <br>Length:  {seq.len()}<br>")
                for element in seq.seq_count():
                    percent = seq.seq_count()[element]/seq.len()*100
                    res+=(f"<br>{element}: {seq.seq_count()[element]} ({percent}%)")
            elif methd == "Rev":
                res= seq.seq_reverse()
            else:
                res= seq.seq_complement()
            contents = f""" <!DOCTYPE html>
                                                <html lang="en">
                                                <head>
                                                    <meta charset="UTF-8">
                                                    <title>Gene</title>
                                                </head>
                                                <h2 style="font-family:Arial">Sequence:</h1>
                                                <body>
                                                <br>
                                                <p>{sequence}</p>
                                                <br>
                                                <h2 style="font-family:Arial">Operation:</h1>
                                                <p>{methd}</p>
                                                <br>
                                                <h2 style="font-family:Arial">Result</h1>
                                                <p>{res}</p>
                                                <br>
                                                <a href="/">Return to main</a>
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

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()