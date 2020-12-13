import code as x 
x.create("abcdef",25)
x.create("ski",70,3600) #create a key with key_name

x.read("abcdef") #returns the value of key_name
x.read("ski")
#returns the value of the respective key in Jasonobject 

x.create("abcdef",50)
x.modify("abcdef",55) #replaces the initial value of the respective key with new value 

 
x.delete("abcdef")
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t2.start()
t2.sleep()
