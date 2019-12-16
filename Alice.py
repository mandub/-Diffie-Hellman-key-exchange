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
def Alice_send(num):
    from_Bob=""
    host = "localhost"
    port = 42428
    #port2 = 42427
    backlog = 5
    size = 1024

    s_alice = socket.socket (socket.AF_INET , socket.SOCK_STREAM)

    s_alice.bind ( ( host,port ) )
    s_alice.listen ( backlog )
    conn , clientaddress = s_alice.accept ( )
    data = conn.recv ( size )
    if data:
        datastring = data.decode ( "utf−8" )
        from_Bob=datastring

    conn.close ( )
    s_alice.close ( )

    ################
    sleep(0.1)

    C_alice = socket.create_connection ( ( host, port ) )
    
    snum=str (num)
    buf = snum.encode ( "utf−8" )
    C_alice.sendall ( buf )
    C_alice.close ( )
    return from_Bob

g = RandomPrim()
Bob_massage = Alice_send(g)
if Bob_massage=="0":
    Bob_massage =" Bob recive the massage g First part of puplic key"
print "State =",Bob_massage
p=0
while (p < 1000):
    p = RandomPrim()



Bob_massage = Alice_send(p)
if Bob_massage=="0":
    Bob_massage =" Bob recive the massage p second part of puplic key"
print "State =",Bob_massage
# Alice private key 
A = RandomPrim()
print "Alice private key is = ",A
Amassage= g**A % p
Bob_massage = Alice_send(Amassage)
Bmassage = int (Bob_massage)
Alice_shard_KEY = Bmassage ** A % p
print "Alice shared key is ",Alice_shard_KEY





