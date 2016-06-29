from flask import Flask, render_template, request, redirect, url_for,flash, jsonify,make_response
from datetime import date,timedelta
app = Flask(__name__)

def convMonth(month,year):
	res=0
	for i in range(1,month):
		if(i==2):
			if(year%4==0):
				res += 29
			else:
				res += 28
		elif(i==1 or i==3 or i==5 or i==7 or i==8 or i ==10 or i==12):
			res += 31
		else:
			res += 30
			
	return res 	
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

@app.route('/')
def mainpage():
	return render_template('main.html')



        
@app.route('/<string:givdate>')
def TimeStamp(givdate):
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	m, d, y=0, 0, 0 
	um,ud,uy = 1,1,1970 
	if (givdate[0].isupper()):
		k=1
		for i in months:
			if (givdate[0:len(i)] == i):
				#Month Found
				m=k
				break
			k += 1
		if (m != 0):
			d = int(givdate[len(i)+1:len(i)+3])
			y = int(givdate[len(i)+5:len(i)+9])
			t = int((y - uy)/4)
			dy = y - uy
			dd = d-ud
			total = ((dy)*365 + convMonth(m,y) + dd+t)*24*60*60
			return jsonify({"unix":total,"natural":givdate})
		else:
			return jsonify({"unix":None,"natural":None})
	elif is_number(givdate):
		unix =timedelta(days=int(givdate)/(24*60*60))
		natural = date(1970,1, 1)+unix 
		res = months[int(natural.month)-1]+" "+str(int(natural.day))+", "+str(int(natural.year))
		return jsonify({"unix":givdate,"natural":res})
	
	return "Wow"
##if __name__ == '__main__':
app.secret_key = 'super_secret_key'
app.debug = True
##	app.run(host = '0.0.0.0', port = 5000)
