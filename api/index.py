from flask import Flask, render_template, request, redirect
import pandas as pd

dataset = pd.read_csv('cods.csv')
#print(dataset)
studentId = ''
retrieved=[]
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/home', methods=["GET", "POST"])
def index():
    global studentId  # Declare studentId as a global variable
    global retrieved
    if request.method == 'GET':
        return render_template('index.html', stuId=studentId,data=retrieved)
    else:
        studentId = request.form['studentId']        
        retrieved = (dataset[ dataset['Student_id'] == int(studentId )])
        print(retrieved)
        retrieved=retrieved.to_dict(orient='records')
        #print(retrieved)
        return redirect('/home')
@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        result_df = dataset[dataset['Email'] == email]
        retrieved_password = result_df.iloc[0]['password']
        if int(password)==retrieved_password:
            return redirect('/home')
        else:
            print("wrong password")
            return redirect('/')


