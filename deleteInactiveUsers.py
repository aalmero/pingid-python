#get org report - run job first
#for each user, check status 
#if not active, delete
#else  check  last login time
#if login time > x days, delete user

import time, sys, json
import pingid

PROPERTIES_FILE = './pingid.properties'
FILE_TYPE = 'JSON'

CURRENT_DATE_INT = int(time.time())
LAST_N_DAYS = 180
DAY_IN_SECS = 86400

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=False)

def get_organization_report():
    req_body = {
       'fileType':FILE_TYPE,
       'clientData': 'NONE',
    }
    return pingid.call('rest/4/getorgreport/do', req_body)

def delete_user(userName):
    req_body = {
       'userName': userName,
      }    

    return pingid.call('rest/4/deleteuser/do', req_body)

def get_user_details(userName):
    req_body = {
       'getSameDeviceUsers':'true',
       'userName': userName,
      }    

    return pingid.call('rest/4/getuserdetails/do', req_body)  

# main logic
user_data = json.loads(get_organization_report())
numberOfUsers = len(user_data['data'])
print('Found {0} users. '.format(numberOfUsers))

if(numberOfUsers) > 0:
    ctr = 0
    for userDetails in user_data['data']:
        status = userDetails['status'] if userDetails['status'] is not None else ''
        userName =userDetails['username']
        intLastTrxTime = int(userDetails['lastTrxTime']/1000 if userDetails['lastTrxTime'] is not None else 0)
        lastTrxTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(intLastTrxTime))
        
        if status != 'ACTIVE':
            ctr = ctr + 1
            print('Deleting {0} - status was {1}'.format(userName, status))
            #delete user bsed from status
            time.sleep(1)
            response_body = delete_user(userName)
            status = response_body['responseBody']['errorId']
            
            if status not in [200]:
                print('[!] Delete User Details Request Failed.')
        else:
            if intLastTrxTime < (CURRENT_DATE_INT - DAY_IN_SECS*LAST_N_DAYS): 
                ctr = ctr + 1
                #delete bsed from last transaction time
                print('Deleting {0} - last transaction time was {1}'.format(userName, lastTrxTime))
                time.sleep(1)
                response_body = delete_user(userName)
                status = response_body['responseBody']['errorId']
            
                if status not in [200]:
                     print('[!] Delete User Details Request Failed.')

    print('[i] {0} users deleted.'.format(ctr))    
