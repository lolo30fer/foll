from itertools import islice
import time
import random
import instaloader
import os

def un_follow():
    opp=int(input("number un > [1,2,3,4,5,6,7,8...] >"))
	
    cl = Client()
    acc=open("acc.txt","r").readlines()
    count_acc=int(len(acc))
    print("len acc=> ",count_acc)
    opre4=0
    
    for lk in range(5):
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        m=0
        opre4+=1
        #time.sleep(20)
        for i,g56 in zip(acc,range(count_acc)):
            
            x=i.split(":")
            print(m,")",i,")  user =----------->",x[0],"       passWD =--------------->",x[1])
            username=x[0]
            password=x[1]
            try:
                cl.login(username,password)
            except:
                continue
            count=0
            followers = cl.user_following(cl.user_id)
            for user_id in followers.keys():
                time.sleep(15)
                try:
                    print(" - ",user_id)
                    cl.user_unfollow(user_id)
                    count+=1
                except:
                    cl.logout()
                    break
                if(count>=opp):
                    cl.logout()
                    
                    break
                print(f"""
                      lk- range5 > {lk}
                      number => {count}
                      {count_acc}< if==sleep(run) >{opre4}
                      g56 {opre4}
                      """)
                hgr4=count_acc-1
            if(hgr4==g56):
                cl.logout()
                ran2=random.randint(2300,2500)  
                print(ran2) 
                time.sleep(ran2) 
                break
            m+=1
#follow()
un_follow()
