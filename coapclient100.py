from coapthon.client.helperclient import HelperClient

host = "192.168.1.100"
port = 5683
path ="light"

client = HelperClient(server=(host, port))
for i in range(50):
    response = client.post(path, "0")
    response = client.post(path, "1")
client.stop()
