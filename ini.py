from selenium import * 
from selenium import webdriver 
from itertools import islice
import time
import random
import instaloader
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from instagrapi import Client
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
def follow():
    time.sleep(2)
    ier=webdriver.Firefox(executable_path='geckodriver.exe')
    ier.get("https://instagram.com/")

    iin=int(input("input x?=> "))
    number=iin
    vV32=open("acc.txt","r").readlines()
    b3=len(vV32)
    p=open("acc.txt","r").readlines()

    for ti in range(3):

        llo0=0
        try:
            for i in range(b3):
                ier.delete_all_cookies()
                u8s=open("acc.txt","r").readlines()
                m98=len(u8s)
                u2=0
                time.sleep(5)

                time.sleep(5)
                ier.get("https://instagram.com/")
                time.sleep(5)
                #print(ier.page_source)
                ye=vV32[i].split(":")
                open(f"user_in-OK/{ye[0]}OK.txt","a")
                print(ye)
                m1=open(f"user_in-OK/{ye[0]}OK.txt","r").readlines()
                #open(ye[0]+".txt","a+")
                try:
                    ier.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(ye[0])
                    ier.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(ye[1])
                    time.sleep(5)
                except:
                    continue
                gt=ier.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()#submit
                time.sleep(20)
                #f1=ier.find_element_by_xpath("//button[contains(text(),'Not Now')]") #now
                #if f1:
                #    f1.click()
                #time.sleep(5)
                time.sleep(5)
                ran=random.randint(8,12)    
                time.sleep(5)
                #ier.find_element_by_xpath("//div[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys("ali")#serch   Search

                        #ier.find_element_by_xpath("/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[2]/input").clear()
                time.sleep(5)
                ier.get("https://www.instagram.com/_alivand.tbriz/")#ali in serch      
                time.sleep(5)
                #ier.find_element_by_xpath("/html/body/div[1]/div/ div/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button").click()
                #ier.find_element_by_xpath("/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[2]/input").send_keys("mahdi")
                cunt=0
                p4=open(f"user_in-user/{ye[0]}.txt","r").readlines()
                #print("test ok ",p4)
                m3=len(p)
                m2=len(m1)  
                u2+=m2           
                hh7=number+m2   
                llo0+=1
                for acc in range(m2,hh7):
                    #profile = instaloader.Profile.from_username(loader.context,p4[acc])

                    #j51=profile.followers
                    #j52=profile.followees
                    #print(j51,"  ",j52)

                    try:
                        time.sleep(ran)
                        #serch
                        ier.find_element(By.CSS_SELECTOR, ".XTCLo").clear()
                        time.sleep(ran)
                        ier.find_element(By.CSS_SELECTOR, ".XTCLo").send_keys(p4[acc])#serch user JvDyy     //div[text()='38']"
                        lls=p4[acc]
                        time.sleep(ran)
                        #ier.find_element(By.XPATH, '//div[text()="Some text"]').click()#click in user
                        #f4=ier.find_elements_by_xpath('//img[alt(text(), "' + lls + '")]')#click serch 
                        f4=ier.find_element(By.CSS_SELECTOR, ".-qQT3")
                        if f4:
                            f4.click()
                    except:
                        continue
                    
                    time.sleep(4)

                    time.sleep(4)
                    print(f"""
    to i  n >> {ye[0]} <<
                    it followers(  )
                    rande=> {llo0}
                    i=acc> {i}
                    hh7==>(my {number} )+(m2 {m2} ) 
                    range{ti}
                        {acc} ==TT===> {m2} Ta {hh7}
                        =================> {cunt}
                        """)


                    try:
                        followers= ier.find_element_by_xpath('.//*[contains(text(), "followers")]/span').get_attribute("title")
                        o12=""
                        fw=followers.split(",")
                        h=len(fw)
                        for i33 in range(h):
                            o12+=fw[i33]
                        lp88=int(o12)


                    except:
                        pass

                    try:
                        print("------------>>",lp88)
                        if(35<lp88):
                            ppo=ier.find_element_by_xpath("//button[contains(.,'Follow')]")#follow
                            if ppo==False:
                                pass
                            else:
                                pass
                            if(ppo):
                                ppo.click()
                                time.sleep(5)
                                ou=open(f"user_in-OK/{ye[0]}OK.txt","a+")
                                ou.writelines(p4[acc])
                                #ou.writelines("\n")
                            else:
                                print(f"""
                                ============> shode
                                """)
                        else:
                            continue
                    except:
                        continue
                    cunt +=1
                    time.sleep(5)
                    print(cunt," ",p4[acc])

                    if(acc>=hh7):

                        break
                print(f"{iin} in {iin}")

                if(m98+1<=llo0):

                    break
        except:
            continue
        time.sleep(2400)            
        #time.sleep(60*30)
            #driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        """
        ier.find_element_by_xpath("//button[contains(.,'Follow')]")
        driver.find_element_by_xpath("//a[text()='Privacy Policy']")
        """ 
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
