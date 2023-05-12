import time, sys, json
import pingid

PROPERTIES_FILE = './pingid.properties'

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=False)

def get_user_details(userName):
  req_body = {
   'getSameDeviceUsers':'true',
   'userName': userName,
  }

  return pingid.call('rest/4/getuserdetails/do', req_body)  

# main logic
arguments = len(sys.argv) - 1
if arguments == 0:
  print('Usage: ' + __file__ + ' <userName>')
  exit()

userName = sys.argv[1]

response_body = get_user_details(userName)

status = response_body['responseBody']['errorId']

if status is 200:
  userDetails = response_body['responseBody']['userDetails']

  print('userName: {0}'.format(userDetails['userName']))
  print('email: {0}'.format(userDetails['email'] if userDetails['email'] is not None else ''))
  print('status: {0}'.format(userDetails['status'] if userDetails['status'] is not None else ''))
  print('deviceId: {0}'.format(str(userDetails['deviceDetails']['deviceId']) if userDetails['deviceDetails'] else 0))
  intLastLogin = int(userDetails['lastLogin']/1000 if userDetails['lastLogin'] is not None else 0)
  print('lastLogin: {0}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(intLastLogin))))

else:
  print('[!] Get User Details Request Failed.')
  
