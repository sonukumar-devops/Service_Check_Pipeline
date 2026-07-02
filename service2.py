from http.server import HTTPServer, BaseHTTPRequestHandler
import json   # importing the built in json module
import random


class MyJsonServer(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == '/health':
            print("Request received:", self.path)
            self.send_response(200)

            self.send_header('Content-type', 'application/json') # Telling browser about json data
            self.end_headers()         #tells browser that "I am done sending metadata headers. Next data will be actual content."
            
            random_value= random.random()
            print("Random Number:", random_value)
            if random_value > 0.4:
                status = "UP"
            else:
                status = "DOWN"
            data = {                     # creating a standard python dictionary
            "message": "You reached the health endpoint!",
            "status": status,
            "port": 5000
            }

            json_string = json.dumps(data)   #converting dictionary into a JSON String
            self.wfile.write(json_string.encode('utf-8'))  #using 'write file' stream to send data back to the browser.
        else:
            self.send_response(404)  #if user types anything else (like http://localhost:5000/goodbye), the if statement fails and jumps to else block.
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            error_data = {
                    "error": "Page not found"
                    }
            self.wfile.write(json.dumps(error_data).encode('utf-8'))

print("JSON server  starting on port 5000......")   # simply for debugging so we know the script didn't stuck somewhere in between

server = HTTPServer(('0.0.0.0', 5000), MyJsonServer)

'''this initializes the actual server machine. It tkaes two things: first is a tuple ('localhost', 5000) and second is our custom MyJsonServer class,
telling the server to use our custom "brain" logic to handle requests. '''

server.serve_forever()  # This starts an infinite loop. It keeps running forever, constantly listening for anyone tring to visit "http://localhost:5000"
