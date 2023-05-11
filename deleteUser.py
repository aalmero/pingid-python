import pingid
import sys

PROPERTIES_FILE = './pingid.properties'

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=False)

def delete_user(userName):
    req_body = {
       'userName': userName,
      }    

    return pingid.call('rest/4/deleteuser/do', req_body)


# main logic
arguments = len(sys.argv) - 1
if arguments == 0:
  print('Usage: ' + __file__ + ' <userName>')
  exit()

userName = sys.argv[1]

print('Deleting {0}.'.format(userName))
response_body = delete_user(userName)

status = response_body['responseBody']['errorId']

if status not in [200]:
     print('[!] Delete User Details Request Failed.')