import socket
from IPy import IP


def scan(ip_add):
    converted_ip = ip_change(ip_add)
    print('\n' + ' [*_* scanning target] ' + ip_add)
    for port in range(1, 100):
        port_scan(converted_ip, port)


def ip_change(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)


def port_scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))

    except:
        pass
    # print('[-] Port '+str(port)+' is closed')

def strip(target):
    #target = input('[+] Enter target/s to scan: ')
    if ',' in target:
        for ip_add in target.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(target)
