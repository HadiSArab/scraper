from crypt import methods
from flask import Flask , request, redirect, url_for
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/salam')
def salam():
	return render_template('salam.html')
	
@app.route('/salam2')
def salam2():
	return render_template('salam2.html', name=request.args['name'] , age=request.args['age'])

# in this section i tried to use both methods GET and POST .
@app.route('/salam3', methods=['GET','POST'])
def salam3():
	# when use post method. use "form" instead of "args"

	if request.method =='POST':
		# create dictionary 
		emails = {}
		emails[request.form['name']] = request.form['email']
		# convert to json file and store in machin
		with open ('ali.json', 'w') as email_file:
			json.dump(emails, email_file)
		return render_template('salam3.html', name=request.form['name'] , email=request.form['email'] , subject=request.form['subject'] , comment=request.form['comment'])
		
	else:
		# if request not be POST method, automaticly redirect to url of home func.
		return redirect(url_for('home'))