import CGIHTTPServer
import SocketServer

PORT = 8080

Handler = CGIHTTPServer.CGIHTTPRequestHandler
Handler.cgi_directories = ["c", "/c", "c/", "/c/"]
print Handler.cgi_directories
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.server_name = "localhost"
httpd.server_port = PORT

httpd.serve_forever()
