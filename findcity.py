import ast
import time
#Existing Input file
inputfile=open("4sq_sampledata.json","r+")
tiput=inputfile.readlines()
#Write the data with city in a new file
newfile=open("4sq_new.json","w")

def in_NY(x,y):
    if (x >= -74.2590942382812 and x <= -73.7001647949219):
        if (y >= 40.4773979187012 and y <= 40.9175796508789):
            return True
    return False

#Define the polygon function
def point_in_poly(x,y,poly):
    n = len(poly)
    inside = False
    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y
    return inside
#Set the coordinates of NewYork
polygon = [(40.7697,-73.9735),(40.8500,-73.8667),(40.6500,-73.9500),(40.5822,-74.1409)]

for i in range(len(tiput)):
	print 'enter 1st check'+str(len(tiput))
	iput=tiput[i]
	iput=iput.strip()
	invdata=ast.literal_eval(iput)
	a=invdata['checkin']
	point_y=a['geolat']
	point_x=a['geolong']
	checkcord=in_NY(point_x,point_y)
	#checkcord=point_in_poly(point_x,point_y,polygon) #Calling the function
	if checkcord:
		a['city']='New York'
		newval={}
		newval['checkin']=a
		covstr=str(newval)
		newfile.write(covstr+'\n')
	else:
		a['city']='Others'
	#print results[0].locality

newfile.close()

