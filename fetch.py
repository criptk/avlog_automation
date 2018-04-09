#!/usr/bin/python3

#
# Python 3 script to get data from AVLOG 
# Criptkeeper - criptk@gmail.com
#

import urllib.request
import argparse
import xlsxwriter
import sys
import json
import certifi
import ssl

def make_request_avlog(threat,country,industry,compSize,dtRange,countBy,topn):
    
    print("Entering make_request_avlog with threat: %d, country: %s, industry: %s, compSize: %s, dtRange: %d, countBy: %d and topn: %d" % (threat,country,industry,compSize,dtRange,countBy,topn))

    if dtRange == 1:
        if threat == 0:
            db = "av_last_24_hours"
        if threat == 1:
            db = "ips_last_24_hours"
        if threat == 4:
            db = "botnet_last_24_hours"

    if dtRange == 2:
        if threat == 0:
            db = "av_last_7_days"
        if threat == 1:
            db = "ips_last_7_days"
        if threat == 4:
            db = "botnet_last_7_days"
    
    if dtRange == 3:
        if threat == 0:
            db = "av_last_30_days"
        if threat == 1:
            db = "ips_last_30_days"
        if threat == 4:
            db = "botnet_last_30_days"

    towrite = open(db, "w+")
    # Creating SSL objects for handling the https and the authentication
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    context.load_verify_locations(certifi.where())
    httpsHandler = urllib.request.HTTPSHandler(context = context)

    # building the url the the parsed parameters 
    url_request_avlog = "https://x.x.x.x/index.php?module=topthreat&action=search&"
    url_request_avlog2 = url_request_avlog + "vnameType=" + str(vnameType) + "&country=" + str(country)  + "&industry=" + str(industry) + "&compSize=" + "&dtRange=" + str(Range) + "&countBy=" + str(countBy)  + "&topn=" + str(topn)

    manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    manager.add_password(None, 'https://x.x.x.x/', '<USERNAME>', '<PASSWORD>')
    authHandler = urllib.request.HTTPBasicAuthHandler(manager)

    opener = urllib.request.build_opener(httpsHandler, authHandler)

    # Used globally for all urllib.request requests.
    # If it doesn't fit your design, use opener directly.
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url_request_avlog2)
    response_body = response.read().decode('utf-8')

    json_data = json.loads(response_body)

    topthreat = json_data['topthreat']
    for value_dict in topthreat:
        towrite.write("{name}, {cnt}".format(**value_dict))
        towrite.write("\n")
    towrite.close()
    
parser = argparse.ArgumentParser()
parser.add_argument("threat", help = "virus ;  ips ;  botnet ; app", type=str)
parser.add_argument("timerange", help = "1 = 24 hours ; 2 = 7days ; 3 = 30 days ; 0 = all", type=int)
parser.add_argument("country",  help = "Enter country code in two letters", type=str)
parser.add_argument("industry", help = "Enter industry", type=str)
parser.add_argument("sort", help = "Sort by total volume = 0 , # devices = 1 ", type=int)
parser.add_argument("top", help = "How many records to show", type=int)
args = parser.parse_args()

# identifyes the type of threat 
vnameType = 0
# identifies the country, US, CA , TW , BR , or "" for ALL
country = args.country 
# industry Automotive, Government, "" for ALL
industry = args.industry 
# the timeframe , 24hours, 7 days or 30 days 
Range = 0
# volume / number of infected devices 
countBy = args.sort 
# how many threats to show 
topn = args.top 

# parsing commnad line arguments
if args.threat == "av" or args.threat == "virus":
    vnameType = 0
if args.threat == "ips":
    vnameType = 1 
if args.threat == "botnet":
    vnameType = 4 
if args.threat == "app":
    vnameType = 3 

if args.timerange == 0:
    Range = 0
    Range = 1 
    for i in range(1, 4):
        make_request_avlog(vnameType, "", "", "", Range, countBy, topn)
        Range = Range + 1
if args.timerange == 1:
    Range = 1
    make_request_avlog(vnameType, "", "", "", Range, countBy, topn)
if args.timerange == 2:
    Range = 2
    make_request_avlog(vnameType, "", "", "", Range, countBy, topn)
if args.timerange == 3:
    Range = 3
    make_request_avlog(vnameType, "", "", "", Range, countBy, topn)
