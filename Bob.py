from time import sleep
import random
import socket
def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def RandomPrim():
    n = 2000
    alist=[]
    for p in range(2, n+1):
        if is_prime(p):
            alist.append(p)
    r=  random.choice(alist)
    
    return r
def Bob_send(num):
    from_Alice=""
    host = "localhost"
    port = 42428
    #port2 = 42427
    backlog = 5
    size = 1024

    C_bob = socket.create_connection ( ( host, port ) )
    
    snum=str (num)
    buf = snum.encode ( "utf−8" )
    C_bob.sendall ( buf )

    C_bob.close ( )
    ###################
    sleep(0.1)
    s_bob = socket.socket (socket.AF_INET , socket.SOCK_STREAM)
    s_bob.bind ( ( host,port ) )
    s_bob.listen ( backlog )
    conn , clientaddress = s_bob.accept ( )
    data = conn.recv ( size )
    if data:
        datastring = data.decode ( "utf−8" )
        from_Alice = datastring

    conn.close ( )
    s_bob.close ( )
    return from_Alice
Alice_massage = Bob_send(0)
g = int (Alice_massage)
print "State = Alice send first part of puplic key = ",g
Alice_massage = Bob_send(0)
p= int (Alice_massage)
print "State = Alice send second part of puplic key = ", p
B= RandomPrim()
print "Bob private key is = ",B
Bmassage= g**B % p
Alice_massage = Bob_send(Bmassage)
Amassage = int (Alice_massage)
Bob_shard_KEY = Amassage ** B % p
print "Bob shared key is ",Bob_shard_KEY




