import SocketServer
import json

class ScamperRequestHandler(SocketServer.BaseRequestHandler):
  def handle(self):
    self.data = self.request.recv(1024)
    data = json.loads(self.data)
    self.server.update_rtt(self.client_address[0], str(data['ip']), data['rtt'])