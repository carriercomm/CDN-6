import SocketServer

class DNSServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
  pass