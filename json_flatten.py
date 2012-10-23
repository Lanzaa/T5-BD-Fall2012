import ast
import time
import sys
import json

print "date,venue-id,venue-name,mayor-type,user-gender,geolat,geolong,timezone,pc-id,pc-fullname,pc-nodename,pc-iconurl"
for line in sys.stdin:
    dline = json.loads(line)['checkin']
    dout = []
    dout.append(str(dline['created']))
    dout.append(dline['venue']['id'])
    dout.append(dline['venue']['name'])
    dout.append(dline['mayor']['type'])
    dout.append(dline['user']['gender'])
    dout.append(str(dline['geolat']))
    dout.append(str(dline['geolong']))
    dout.append(dline['timezone'])
    dout.append(dline['primarycategory']['id'])
    dout.append(dline['primarycategory']['fullpathname'])
    dout.append(dline['primarycategory']['nodename'])
    dout.append(dline['primarycategory']['iconurl'])
    print '"'+'","'.join(dout)+'"'

