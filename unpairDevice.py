import time, sys, json
import pingid

PROPERTIES_FILE = './pingid.properties'

def get_user_details(driver, params):
  return driver.call('rest/4/getuserdetails/do', params)  


# main logic
arguments = len(sys.argv) - 1
if arguments == 0:
  print('Usage: ' + __file__ + ' <userName>')
  exit()

userName = sys.argv[1]

user_req_body = {
   'getSameDeviceUsers':'true',
   'userName': userName,
  }

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=False)
#user_response_body = pingid.call('rest/4/getuserdetails/do', user_req_body)
user_response_body = get_user_details(pingid, user_req_body)

status = user_response_body['responseBody']['errorId']

if status is 200:
  #get user deviceId
  userDetails = user_response_body['responseBody']['userDetails']
  deviceId = userDetails['deviceDetails']['deviceId']

  device_req_body = {
     'deviceId': deviceId,
     'userName': userName,
     'clientData': ''
    }

  device_response_body = pingid.call('rest/4/unpairdevice/do', device_req_body)

  status = device_response_body['responseBody']['errorId']

  if status is 200:
    print(userName + ' device unpaired succesfully!')
  else:
    print('[!]  Unpair Device Request Failed.')    

else:
  print('[!] Get User Details Request Failed.')