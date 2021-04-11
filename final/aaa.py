from flask import Flask,request, url_for, redirect, render_template





app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    Expected_Answer = request.form['Expected_Answer']
    Students_Answer = request.form['Students_Answer']
    print(Expected_Answer)
    print(Students_Answer)
    return render_template("index.html",Students_Answer=Students_Answer,Expected_Answer=Expected_Answer)


    #return render_template('index.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")


if __name__ == '__main__':
    app.run()
