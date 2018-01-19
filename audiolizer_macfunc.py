def send_to_pd_mac(msg, port):
    IP="127.0.0.1"
    # PORT=5005
    addr=(IP, port)
    EOL=';\n'
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # for i in range(10):
    #     msg="list foo "+str(i)+" bar"
    #     sock.sendto(msg+EOL, addr)
    sock.sendto(msg+EOL, add)
