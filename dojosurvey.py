"""
from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def yourname():

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    validation_failed = False

if len(session['name']) < 1: 
    flash("Name cannot be blank!") validation_failed=True 
if len(session['comment']) < 1:
    flash("Comment cannot be blank") validation_failed=True 
if len(session['comment'])> 120:
    flash("Comment cannot be longer than 120 characters!")
    validation_failed = True

if validation_failed == True:
    return redirect('/')
else:
    return render_template('results.html')

app.run(debug=True)

    """


from flask import Flask, render_template, redirect, request 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/results', methods=["POST"])
def results():
    return render_template('results.html',

    name = request.form['name'],
    location = request.form['location'],
    language = request.form['language'],
    comment = request.form['comment']

    )
app.run(debug=True)
