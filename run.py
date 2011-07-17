#!/usr/bin/python
import CGIHTTPServer
import SocketServer

PORT = 8080

Handler = CGIHTTPServer.CGIHTTPRequestHandler
Handler.cgi_directories = ["/c"]
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Serving at port", PORT
#change this if running on live website
httpd.server_name = "localhost"
httpd.server_port = PORT

httpd.serve_forever()
