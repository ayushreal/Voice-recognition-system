import pyttsx3;
import speech_recognition as sr
import pafy
from lxml import html
import requests
import webbrowser
import os
import time

print('Please enter your username.')
 
name=input()
 
username='Ayush'
 
if name == (username):
        print('Please wait')
        time.sleep(1.5)
        print('')
        print('Correct, please enter your password.')
 
password=input()
 
password1='15bcs1402'
 
if password == (password1):
        print('Please wait')
        time.sleep(1.5)
        print('')
        print('Correct, logging in.')
        time.sleep(1.5)
        print('Welcome '+username)
        time.sleep(3)


        engine = pyttsx3.init();
        def myfun(total, recvd, ratio, rate, eta):
            print ("Downloaded : "+ratio*100,'%')
        mlist=[]
        loopme=1
        r = sr.Recognizer()
        while(loopme==1):
            with sr.Microphone() as source:
                print ("Hello Ayush Srivastava")
                engine.say("Hello Ayush Srivastava");
                engine.runAndWait() ;
                r.adjust_for_ambient_noise(source, duration = 1)
                print("Sir please say something!")
                engine.say("Sir please say something");
                engine.runAndWait() ;
                audio = r.listen(source)
                print("Trying to recognize your voice")
                engine.say("Trying to recognize your voice");
                engine.runAndWait() ;

            try:
        
                t=r.recognize_google(audio)
                print ("You just said " +t)
                if(t.find("download")!=-1):
                    le=t.find("download")+len("download")+1
                    t=t[le:]
                    with sr.Microphone() as source:
                        print ("One moment sir")
                        engine.say("One moment sir");
                        engine.runAndWait() ;
                        r.adjust_for_ambient_noise(source, duration = 1)
                        print ("Sir do you want to download"+t)
                        engine.say("Sir do you want to download");
                        engine.runAndWait() ;
                        audio = r.listen(source)
                        print("Trying to recognize your voice")
                        engine.say("Trying to recognize your voice");
                        engine.runAndWait() 
                        b=r.recognize_google(audio)
                        if(b.find("yes")!=-1):                                              # Download youtube video
                            print ("Downloading ")
                            engine.say("Downloading");
                            engine.runAndWait() 
                            q='https://www.youtube.com/results?search_query='+t
                            page = requests.get(q)
                            tree = html.fromstring(page.content)
                            buyers = tree.xpath('//*[@id="results"]/ol[1]/li[1]/ol[1]/li[1]/div[1]')
                            a=buyers[0]
                            p=a.get("data-context-item-id")
                            v=pafy.new(p)
                            s=v.streams[2]
                            s=v.getbest(preftype="mp4")                                  
                            s.download("E:\Movies",quiet=True,callback=myfun)                #Change your download location here
                            print ("Finished downloading")
                                        
                                        
                elif(t.find("about yourself")!=-1): #about
                    print("I am Natasha created by Ayush Srivastava")
                    engine.say("I am Natasha created by Ayush Srivastava");
                    engine.runAndWait();
                    print("I am an Artificial Inteligence system, who can do most of the things you say")
                    engine.say("I am an Artificial Inteligence system, who can do most of the things you say");
                    engine.runAndWait();
                    print("That's all about me, anything else")
                    engine.say("That's all about me, anything else");
                    engine.runAndWait();
                        
                        
                elif(t.find("play")!=-1):                                                   #Play youtube video
                    le=t.find("play")+len("play")+1
                    t=t[le:]
                    print ("Playing"+t)
                    q='https://www.youtube.com/results?search_query='+t
                    page = requests.get(q)
                    tree = html.fromstring(page.content)
                    buyers = tree.xpath('//*[@id="results"]/ol[1]/li[1]/ol[1]/li[1]/div[1]')
                    a=buyers[0]
                    p=a.get("data-context-item-id")
                    webbrowser.open("https://www.youtube.com/watch?v="+p)
            
                elif(t.find("open")!=-1):                                                   # Open windows application
                    le=t.find("open")+len("open")+1
                    t=t[le:]
                    if(t=="calculator" or t=="Calculator"):
                        engine.say("Opening calculator");
                        engine.runAndWait() 
                        os.system("start calc.exe")
                        mlist.append("calc.exe")
                    elif(t=="Notepad" or t=="notepad"):
                        engine.say("Opening Notepad");
                        engine.runAndWait()
                        os.system("start notepad.exe")
                        mlist.append("notepad.exe")
                    elif(t=="Paint" or t=="paint"):
                        engine.say("Opening paint");
                        engine.runAndWait()
                        os.system("start mspaint.exe")
                        mlist.append("mspaint.exe")
                    elif((t.find("Chrome")!=-1) or (t.find("chrome")!=-1)):
                        os.system("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                        mlist.append("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chrome.exe")
            
                elif(t.find("close")!=-1):                                                  # Close windows application
                    le=t.find("close")+len("close")+1
                    t=t[le:]
                    try:
                        if(t=="calculator" or t=="Calculator"):
                            mlist.index("calc.exe")
                            os.system("taskkill /F /IM calc.exe")
                            mlist.remove("calc.exe")
                        elif(t=="Notepad" or t=="notepad"):
                            mlist.index("notepad.exe")
                            os.system("taskkill /F /IM notepad.exe")
                            mlist.remove("notepad.exe")
                        elif(t=="Paint" or t=="paint"):
                            mlist.index("mspaint.exe")
                            os.system("taskkill /F /IM mspaint.exe")
                            mlist.remove("mspaint.exe")
                
                        else:
                            loopme=0
                
                    except:
                            print ("Could not close the applicarion")               
                
                elif (t.find("Google")!=-1 ):                                            
                    le=t.find("Google")+len("Google")+1
                    t=t[le:]
                    webbrowser.open("https://www.google.co.in/search?q="+t)
                        
                elif(t.find("Tell me")!=-1):
                    le.t,find("Tell me")+len("Tell me")+1
                    t=t[le:]
                    webbrowser.open("https://www.google.co.in/search?q="+t+"wikipedia")
                    #engine.say(https://en.wikipedia.org/wiki/t);
                    #engine.runAndWait()
                        
            
            except sr.UnknownValueError:
                print("Sorry Sir I didnot understand what you said")
                loopme=1
            except sr.RequestError as e:
                print("Sorry Sir I couldnot found the request; {0}".format(e))

		
        if name != (username):
                print('Please wait')
                time.sleep(1.5)
                print('')
                print('Incorrected, closing program.')
                time.sleep(1.5)