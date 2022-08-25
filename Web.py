    
from flask import Flask, render_template, redirect, url_for, request
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://altissimo:altissimo@ac-1k1ioje-shard-00-00.tktjcey.mongodb.net:27017,ac-1k1ioje-shard-00-01.tktjcey.mongodb.net:27017,ac-1k1ioje-shard-00-02.tktjcey.mongodb.net:27017/?ssl=true&replicaSet=atlas-wn5rne-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client['Farmops']
inputPakan = db["input pakan"]
inputSuhu = db["input temperatur"]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/edit', methods=('GET','POST'))
def edit(): 
    for dataPakan in inputPakan.find().sort([('_id', -1)]).limit(1)  :
        jamPakan = dataPakan["jamPakan"]
        jamPakan2 = dataPakan["jamPakan2"]
        jamPakan3 = dataPakan["jamPakan3"]
 
    if request.method == "POST":
        pakan = request.form["jamPakan"]
        pakan2 = request.form["jamPakan2"]
        pakan3 = request.form["jamPakan3"]
        inputPakan.insert_one({"jamPakan":pakan, "jamPakan2":pakan2,"jamPakan3":pakan3})
        return redirect(url_for('edit'))
        
    return render_template("edit.html", jamPakan=jamPakan, jamPakan2=jamPakan2, jamPakan3=jamPakan3)

@app.route('/suhu', methods=('GET','POST'))
def suhu ():
    for dataSuhu in inputSuhu.find().sort([('_id', -1)]).limit(1):
        tempMax = dataSuhu["tempHi"]
        tempMin = dataSuhu["tempLo"]

    if request.method == "POST":
        tempHi = request.form["tempHi"]
        tempLo = request.form["tempLo"]
        inputSuhu.insert_one({"tempHi":tempHi, "tempLo":tempLo})
        return redirect(url_for('suhu'))
        
    return render_template("suhu.html", tempMax=tempMax, tempMin=tempMin)

if __name__ == '__main__':
    app.run(debug=True)

