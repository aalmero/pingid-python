import time, sys, json
import pingid

PROPERTIES_FILE = './pingid.properties'

def get_user_details(driver, userName):
  req_body = {
   'getSameDeviceUsers':'true',
   'userName': userName,
  }

  return driver.call('rest/4/getuserdetails/do', req_body)  

# main logic
arguments = len(sys.argv) - 1
if arguments == 0:
  print('Usage: ' + __file__ + ' <userName>')
  exit()

userName = sys.argv[1]

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=False)

response_body = get_user_details(pingid, userName)

status = response_body['responseBody']['errorId']

if status is 200:
  userDetails = response_body['responseBody']['userDetails']

  print('userName: ' + userDetails['userName'])
  print('email: ' + userDetails['email'])
  print('status: ' + userDetails['status'])
  print('deviceId: ' + str(userDetails['deviceDetails']['deviceId']))
  intLastLogin = int(userDetails['lastLogin']/1000)
  print('lastLogin: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(intLastLogin)))

else:
  print('[!] Get User Details Request Failed.')
  
