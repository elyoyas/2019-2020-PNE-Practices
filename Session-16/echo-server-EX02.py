import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path.split('?')[0] in ['/']:
            contents = Path('form-EX02.html').read_text()

        # i did some extra work to allow spacing between words in the input
        elif self.path.split('?')[0] in ['/echo']:
            darth = self.path.split("?")[1]
            plagueis = darth[4:].split("&")[0]
            try:
                revan = darth[4:].split("&")[1]
                bane = ""
                for number in range(0, len(plagueis)):
                    if plagueis[number] == '+':
                        bane += ' '
                    else:
                        bane += plagueis[number].capitalize()
                easteregg = ""
            except IndexError:

                bane = ""
                for number in range(0, len(plagueis)):
                    if plagueis[number] == '+':
                        bane += ' '
                    else:
                        bane += plagueis[number]
                easteregg = "☭☭☭ we dont capitalize here ☭☭☭"

            contents = (f"""<!DOCTYPE html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title>INPUT PAGE</title>
                          </head>
                          <body>
                            <p>{bane}</p>
                            <p>{easteregg}</p>
                            <b>
                            <a href="/">return</a>
                            </form>
                          </body>
                        </html>""")

        else:
            contents = Path('ERROR.html').read_text()
        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()