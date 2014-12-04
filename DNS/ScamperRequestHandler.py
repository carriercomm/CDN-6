import SocketServer

class ScamperRequestHandler(SocketServer.BaseRequestHandler):
  def handle(self):
    self.data = self.request.recv(1024)
    print "{} wrote:".format(self.client_address[0])
    print self.data