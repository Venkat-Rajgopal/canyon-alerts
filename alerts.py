import requests, json
import sys
import os
import re
from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
from email.mime.text import MIMEText
from pprint import pprint


f = open('creds.json')
creds = json.load(f)

url = 'https://www.canyon.com/en-de/gravel-bikes/adventure/grizl/grizl-cf-sl-6/2711.html?dwvar_2711_pv_rahmenfarbe=GY%2FBK'

# all urls to scrape
urls = { 'g7_sr' : 'https://www.canyon.com/en-de/gravel-bikes/all-road/grail/grail-7/2370.html?dwvar_2370_pv_rahmenfarbe=SR%2FBK',
         'g7_gn' : 'https://www.canyon.com/en-de/gravel-bikes/all-road/grail/grail-7/2370.html?dwvar_2370_pv_rahmenfarbe=GN%2FBK',
         'g6_sr' : 'https://www.canyon.com/en-de/gravel-bikes/all-road/grail/grail-6/2369.html?dwvar_2369_pv_rahmenfarbe=SR%2FBK',
         'g7_gn' : 'https://www.canyon.com/en-de/gravel-bikes/all-road/grail/grail-6/2369.html?dwvar_2369_pv_rahmenfarbe=GN%2FBK',
         '71by' : 'https://www.canyon.com/en-de/gravel-bikes/all-road/grail/grail-7-1by/2707.html?dwvar_2707_pv_rahmenfarbe=SR%2FBK',
        'Grizl_1' : 'https://www.canyon.com/en-de/gravel-bikes/adventure/grizl/grizl-cf-sl-6/2711.html?dwvar_2711_pv_rahmenfarbe=GN%2FBU',
        'Grizl_2' : 'https://www.canyon.com/en-de/gravel-bikes/adventure/grizl/grizl-cf-sl-6/2711.html?dwvar_2711_pv_rahmenfarbe=GY%2FBK'
}


r = requests.get(url)
s = re.search(r'window\.deptsfra=(.*);', r.text).group(1)
data = json.loads(s)

results = {i['value'] : i['availability']['shippingInfo'] for i in data['productDetail']['variationAttributes'][1]['values']}
pprint(results)

def get_results(url):
    r = requests.get(url)
    s = re.search(r'window\.deptsfra=(.*);', r.text).group(1)
    data = json.loads(s)
    results = {i['value'] : i['availability']['shippingInfo'] for i in data['productDetail']['variationAttributes'][1]['values']}
    pprint(results)

    return results


for key, value in urls.items():
    result = get_results(url=value)
    print(result)
    


text_subtype = 'plain'
SMTPserver = 'smtp.gmail.com'
destination = ['venkatramani.r@gmail.com']
sender = creds['my_email']

content="""\
Test message
"""

subject_1 = "Daily Stock Summary"
subject_2 = "Your Bike is now Available!"


try:
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = subject
    msg['From']    = sender # some SMTP servers will do this automatically, not all

    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(creds['my_email'], creds['my_pass'])
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        conn.quit()

except:
    sys.exit( "mail failed; %s" % "Didnt Work!" ) 
