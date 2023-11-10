  
from threading import Thread
from multiprocessing import Process
from ImageConvert import *
from MVSDK import *
import struct
import time
import datetime
import numpy
import cv2
import gc
import os

from socket import *
from os.path import exists
import time
import sys
import shutil  
from glob import glob

def restart():
    print('Restart!')
    os.execl(sys.executable, sys.executable, *sys.argv)
    
 
def removeAllFile(root):
    if os.path.exists(root):
        shutil.rmtree(root)
    #    for file in os.scandir(root):
    #        try:
    #            os.remove(file.path)
    #            return 
    #        except Exception as e:
    #            shutil.rmtree(root)
    #else:
    #    return  

def send_pic(name):
    clientSock = socket(AF_INET, SOCK_STREAM)
    try:
        clientSock.connect(('202.31.34.154', 6300))
        time.sleep(0.03)
    except ConnectionRefusedError as e :
        print('Connect Error!')
        time.sleep(10)
        return

    print('Connect Sucess!')
    for i in range(1):
        filename = 'send.jpg'
        clientSock.sendall(filename.encode('utf-8'))
    t1= '/home/mic-710ai/_SEND/send.jpg'
    data_transferred = 0
    if not os.path.exists(t1):
        print('no file')
        restart()

    print('file %s Send Start!' %filename)
    print('Permission Check : ======== ',os.access(t1,os.F_OK))
    if os.access(t1,os.F_OK) == False:
        os.remove(t1)
    time.sleep(0.5)


    with open(t1, 'rb') as f:
        try:
            data = f.read(1024)
            print(data)
            i = 0
            while data: 
                i = i+1
                print(i, ": transferring")
                data_transferred += clientSock.send(data)
                data=f.read(1024)
                #time.sleep(0.001)
                            
        except Exception as ex:
            print(ex)
        print("Send Success! %s, Amount %d" %(t1, data_transferred))
        f.close()
        time.sleep(0.03)
        clientSock.close()
        gc.collect()
        os.remove(t1)
        print('--remove ',t1)

#def send_pic_01(name):
#    clientSock = socket(AF_INET, SOCK_STREAM)
#    try:
#        clientSock.connect(('202.31.34.166', 6001))
#        time.sleep(0.05)
#    except ConnectionRefusedError as e :
#        print('Connect Error!')
#        time.sleep(10)
#        return

 #   print('Connect Sucess!')
 #   for i in range(1):
 #       filename = 'send.jpg'
 #       clientSock.sendall(filename.encode('utf-8'))
 #   t1= '/home/mic-710ai/mic-710ai/Marking/share/Python/TEST/raw_list_01/send.jpg'
 #   data_transferred = 0
 #   if not os.path.exists(t1):
 #       print('no file')
 #       restart()
  #  print('Permission Check : ======== ',os.access(t1,os.F_OK))
#
 #   print('file %s Send Start!' %filename)
  #  time.sleep(0.5)
  #  if os.access(t1,os.F_OK) == False:
  #      os.remove(t1)
    

  #  with open(t1, 'rb') as f:
   #     try:
   #         data = f.read(1024)
   #         print(data)
   #         i = 0
   #         while data: 
   #             i = i+1
   #             print(i, ": transferring")
   #             data_transferred += clientSock.send(data)
   #             data=f.read(1024)
                #time.sleep(0.001)
                            
   #     except Exception as ex:
   #         print(ex)
   #     print("Send Success! %s, Amount %d" %(t2, data_transferred))
   #     f.close()
   #     time.sleep(0.1)
   #     clientSock.close()
        #time.sleep(3)
        ## 2
   #     gc.collect()
   #     os.remove(t1)
        #removeAllFile(t1)


if __name__ == "__main__":
    t1= '/home/mic-710ai/_SEND/send.jpg'
   # t2= '/home/mic-710ai/mic-710ai/Marking/share/Python/TEST/raw_list_01/send.jpg'
    name = 'send'
    while True:
        time.sleep(1)
        print('Waiting!')
        gc.collect()
        g1 = glob('/home/mic-710ai/_SEND/*.jpg')
        #g2 = glob('/home/mic-710ai/mic-710ai/Marking/share/Python/TEST/raw_list_01/*.jpg')

        print('g1 :',len(g1))
        #print('g2 :',len(g2))

        if len(g1)>0:
            if g1[0] != t1 :
                print ('file : ', g1[0])
            try:
                os.rename(g1[0], t1)
            except Exception as e:
                print(e)
                print('erorr')
                time.sleep(0.5)
                print('Restart!')
                restart()

        if os.path.exists(t1) > 0 :
            
            
            try:
                send_pic(name)
                continue
            except Exception as e:
                print(e)
                print('erorr')
                time.sleep(1)
                print('Restart!')
                restart()

        #if len(g2)>0:
        #    if g2[0] != t2 :
        #        print ('file : ', g2[0])
        #        try:
        #            g2 = glob('/home/mic-710ai/mic-710ai/Marking/share/Python/TEST/raw_list_01/*.jpg')
        #            if os.path.exists(t2) :
        #                pass
        #            else :
        #                os.rename(g2[0], t2)
        #        except Exception as e:
        #            print(e)
        #            print('erorr')
        #            time.sleep(0.5)
        #            print('Restart!')
        #            restart()

        #if os.path.exists(t2) :
        #    try:
        #        send_pic_01(name)
         #       continue
         #   except Exception as e:
         #       print(e)
          #      print('erorr')
          #      time.sleep(1)
          #      print('Restart!')
          #      restart()
