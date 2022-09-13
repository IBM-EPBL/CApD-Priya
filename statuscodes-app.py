from flask import Flask,redirect,url_for,render_template,request,abort

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=['GET'])
def login():
    if request.method=='GET' and request.args.get('uname')=='admin':
        return redirect(url_for('success'))  
    else:
        abort(401)

@app.route('/success')
def success():
    return 'logged in succesfully'


if __name__=='__main__':
    app.run(debug=True)
