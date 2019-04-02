'''
by: tebespace (baguz steady)
python version 2.7.x
tools : checker yahoo mail

'''



import requests

print

o = raw_input('path list email: ')
emails = open(o)

for email in emails:
      url_ = "http://widhitools.000webhostapp.com/api/yahoo.php?email="+email.strip('\n'[0])
      r = requests.post(url=url_).json()
      print('email: '+email+' status: '+r['status'])

print
