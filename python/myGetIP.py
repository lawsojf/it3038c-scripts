import socket, sys

def getHostnameByIP(h):
    getHostnameByIP(sys.argv[1])

    try:
        hostname = str(h)
        ip = socket.gethostbyname(hostname)
        
        print(hostname + ' has an IP of ' + ip)

    except:
        print("Oops, something is wrong with that host")
