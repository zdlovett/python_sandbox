import socket

host = "thermal_buck.local"
port = 8000

while(True):
    print(f"Attempting to connect to {host}:{port}...")
    connected = False
    try:
        sock = socket.create_connection((host, port))
        sock.settimeout(10)
        connected = True
    except socket.gaierror:
        print("Host not found...")
    except ConnectionRefusedError:
        print("Connection refused...")
    except TimeoutError:
        print("Connection attempt timed out...")

    while connected:
        try:
            incoming = sock.recv(1024)
        except socket.timeout:
            print("Connection timed out.")
            connected = False
        else:
            if len(incoming) != 0:
                print(incoming)
            else:
                print("Connection broken.")
                connected = False
