#!/usr/bin/python2
import sys
import json

print "date,venue-id,venue-name,mayor-type,user-gender,geolat,geolong,timezone,pc-id,pc-fullname,pc-nodename,pc-iconurl"
for line in sys.stdin:
    try:
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
        dout.append(dline['primarycategory'].get('id','-'))
        dout.append(dline['primarycategory'].get('fullpathname','-'))
        dout.append(dline['primarycategory'].get('nodename','-'))
        dout.append(dline['primarycategory'].get('iconurl','-'))
        print '"'+'","'.join(dout)+'"'
    except:
        # Skip this line, something is broken
        print >> sys.stderr, line,

