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

def unpair_user_device(deviceId, userName):
  req_body = {
     'deviceId': deviceId,
     'userName': userName,
     'clientData': ''
  }

  return pingid.call('rest/4/unpairdevice/do', req_body)

# main logic
arguments = len(sys.argv) - 1
if arguments == 0:
  print('Usage: ' + __file__ + ' <userName>')
  exit()

userName = sys.argv[1]

user_response_body = get_user_details(userName)

status = user_response_body['responseBody']['errorId']

if status is 200:
  #get user deviceId
  userDetails = user_response_body['responseBody']['userDetails']
  deviceId = userDetails['deviceDetails']['deviceId']

  device_response_body = unpair_user_device(deviceId, userName)
  
  status = device_response_body['responseBody']['errorId']

  if status is 200:
    print(userName + ' device unpaired succesfully!')
  else:
    print('[!]  Unpair Device Request Failed.')    

else:
  print('[!] Get User Details Request Failed.')