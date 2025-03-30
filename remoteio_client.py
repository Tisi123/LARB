from remoteio import RemoteServer
from time import sleep
import os

if __name__ == "__main__":
    #server_ip = os.environ["REMOTEIO_ADDR"]
    server_ip = "192.168.178.74"
    server_port = 8509

    rs = RemoteServer(server_ip, server_port)

    