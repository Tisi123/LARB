from remoteio import RemoteServer, Remote_AngularServo
from time import sleep
import os

if __name__ == "__main__":
    #server_ip = os.environ["REMOTEIO_ADDR"]

    # moving into a ssh-server implementation within a ROS2 network, so this file is redundant
    server_ip = ""
    server_port = 8509

    rs = RemoteServer(server_ip, server_port)

    rl=Remote_AngularServo(rs,21)
    print(rl.all)
    rl.max()
    sleep(4)
    rl.mid()
    print(rl.pulse_width)
    print(rl.max_pulse_width)
    
    sleep(4)
    rl.min()
    print(rl.is_active)
    sleep(4)
    rl.angle=rl.max_angle
    sleep(5)

    
