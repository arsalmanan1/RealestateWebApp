from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def registration():
    return render_template('formfetch.html')
app.route('/success', methods=['POST'])
def printdata():
    result = request.form
    return render_template('propertyresult.html',result=result)

app.run(debug=True)