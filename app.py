
from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send_message',methods=['POST'])
def send_message():
    name=request.form['name']
    email=request.form['email']
    message=request.form['msg']

    print(f"Name:{name},Email:{email},Message:{message}")

    return render_template('contact.html',success=f"Thank you {name}, your message has been recieved")

if __name__=='__main__':
    app.run(debug=True)