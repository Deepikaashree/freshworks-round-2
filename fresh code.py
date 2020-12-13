import threading 
from threading import*
import time

dicti={} #dictionary 
def create(key,value,timeout=0):
    if key in dicti:
        print("already present") 
    else:
        if(key.isalpha()):
            if len(dicti)<(1024*1020*1024) and value<=(16*1024*1024): #constraints <1GB and Jasonobject <16KB 
                if timeout==0:
                    length=[value,timeout]
                else:
                    length=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input name(32chars)
                    dicti[key]=length
            else:
                print("limit exceeded")
        else:
            print("Invalid keyname")
def read(key):
    if key not in dicti:
        print("key does not exist in database")
    else:
        b=dicti[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                str1=str(key)+":"+str(b[0]) #to return the value"key_name:value"
                return str1
            else:
                print("key expired")
        else:
            str1=str(key)+":"+str(b[0])
            return str1
def delete(key):
    if key not in dicti:
        print("key does not exist in database")
    else:
        b=dicti[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del dicti[key]
                print("successfully deleted")
            else:
                print("keyexpired")
        else:
            del dicti[key]
            print("successfully deleted")
def modify(key,value):
    b=dicti[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dicti:
                print("key does not exist in database") 
            else:
                length=[]
                length.append(value)
                length.append(b[1])
                dicti[key]=length
        else:
            print("key expired") 
    else:
        if key not in dicti:
            print("key does not exist in database") 
        else:
            length=[]
            length.append(value)
            length.append(b[1])
            dicti[key]=length
