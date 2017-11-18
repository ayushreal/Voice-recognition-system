import speech_recognition as sr
import pafy
from lxml import html
import requests
import webbrowser
import os


def myfun(total, recvd, ratio, rate, eta):
    print ("Downloaded : "+ratio*100,'%')
mlist=[]
loopme=1
r = sr.Recognizer()
while(loopme==1):
    with sr.Microphone() as source:
        print ("A moment of silence")
        r.adjust_for_ambient_noise(source, duration = 1)
        print("Say something!")
        audio = r.listen(source)
        print("Trying to recognize audio")

    try:
        
        t=r.recognize_google(audio)
        print ("You just said " +t)
        if(t.find("download")!=-1):
            le=t.find("download")+len("download")+1
            t=t[le:]
            with sr.Microphone() as source:
                print ("A moment of silence")
                r.adjust_for_ambient_noise(source, duration = 1)
                print ("Do you want to download"+t)
                audio = r.listen(source)
                print("Trying to recognize audio")
                b=r.recognize_google(audio)
                if(b.find("yes")!=-1):                                              # Download youtube video
                    print ("Downloading ")+t
                    q='https://www.youtube.com/results?search_query='+t
                    page = requests.get(q)
                    tree = html.fromstring(page.content)
                    buyers = tree.xpath('//*[@id="results"]/ol[1]/li[1]/ol[1]/li[1]/div[1]')
                    a=buyers[0]
                    p=a.get("data-context-item-id")
                    v=pafy.new(p)
                    s=v.streams[2]
                    #s=v.getbest(preftype="mp4")                                  # Uncomment this for getting high quality video
                    s.download("D:\songs",quiet=True,callback=myfun)                #Change your download location here
                    print ("Finished downloading")
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
                os.system("start calc.exe")
                mlist.append("calc.exe")
            elif(t=="Notepad" or t=="notepad"):
                os.system("start notepad.exe")
                mlist.append("notepad.exe")
            elif(t=="Paint" or t=="paint"):
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
            
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        loopme=1
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))