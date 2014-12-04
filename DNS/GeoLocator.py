import urllib2
import json

class Locator():
  def find_coordinates(self, ip):
    response = urllib2.urlopen('http://ip-api.com/json/' + ip)
    return json.load(response)