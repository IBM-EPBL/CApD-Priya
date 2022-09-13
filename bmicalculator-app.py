from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def html():
        return render_template('hello.html')

@app.route('/cal',methods=['POST'])
def calculate():
    bmi=0
    if request.method == 'POST':
        w=request.form.get('weight')
        h=request.form.get('height')
        bmi=float(w)*float(h)
        return render_template('success.html',bmi=bmi)

if __name__=='__main__':
    app.run(debug=True)
