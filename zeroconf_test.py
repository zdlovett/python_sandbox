import string
import time
import struct
import socket
import threading
import select
import traceback
from zeroconf import *

if __name__ == '__main__':
    host = socket.gethostbyname(socket.gethostname())
    print ("Multicast DNS Service Discovery for Python, version", __version__)
    r = Zeroconf()
    print ("1. Testing registration of a service...")
    desc = {'version':'0.10','desc':'A python simulator for the EV30 wifi interface'}
    info = ServiceInfo("_uart._tcp.local.", "ESP32_UART_Bridge._uart._tcp.local.", socket.inet_aton(host), 1234, 0, 0, desc)
    print ("   Registering service...")
    r.register_service(info)
    print ("   Registration done.")
    print ("2. Testing query of service information...")
    print ("   Getting ZOE service:", str(r.get_service_info("_http._tcp.local.", "ZOE._http._tcp.local.")))
    print( "   Query done.")
    print ("3. Testing query of own service...")
    print ("   Getting self:", str(r.get_service_info("_http._tcp.local.", "My Service Name._http._tcp.local.")))
    print ("   Query done.")
    print ("4. Testing unregister of service information...")
    r.unregister_service(info)
    print ("   Unregister done.")
    r.close()
