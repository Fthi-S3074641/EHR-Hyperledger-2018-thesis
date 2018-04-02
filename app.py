from flask import Flask, render_template, request, redirect
from datetime import datetime
import requests
import json 
import random
import os



app = Flask(__name__)


def medExtract(myMedications):
    # sickness = ', '.join(element['medicineId'] for element in myMedications)
    sickness =  ''
    for element in myMedications:
        if element['medicineId'] != 'string':
            sickness = ', '.join([sickness, element['medicineId']])
    return sickness
        
def symExtract(myMedications):
    # sickness = ', '.join(element['medicineId'] for element in myMedications)
    sickness =  ', '.join(myMedications)
    # for element in myMedications:
        # if element != 'string':
            # sickness = ', '.join([,element, ' '])
    return sickness


app.jinja_env.globals.update(medExtract=medExtract) 
app.jinja_env.globals.update(symExtract=symExtract) 

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/Patient')
def listPatients():
    r = requests.get('http://localhost:3000/api/Patient')
    if r.json()== None or r.json()=={}:
        worked = {}
    else:
        worked = r.json()
    return render_template('patients.html', title="Patient", worked=worked)

@app.route('/Doctor')
def listDoctors():
    r = requests.get('http://localhost:3000/api/Doctor')
    if r.json()== None or r.json()=={}:
        worked = {}
    else:
        worked = r.json()
    return render_template('doctors.html', title="Doctor", worked=worked)

@app.route('/Nurse')
def listNurses():
    r = requests.get('http://localhost:3000/api/Nurse')
    if r.json()== None or r.json()=={}:
        worked = {}
    else:
        worked = r.json()
    return render_template('doctors.html', title="Nurse", worked=worked)

@app.route('/Medication')
def listMedications():
    r = requests.get('http://localhost:3000/api/Medication')
    if r.json()== None or r.json()=={}:
        worked = {}
    else:
        worked = r.json()
    return render_template('medications.html', title="Medication", worked=worked)


@app.route('/addSomeone/<who>', methods=['POST', 'GET'])
def addSomeone(who):
    id = request.form['personId'].encode('utf-8')
    name = request.form['name'].encode('utf-8').lower()
    person = str(who)

    if person == 'Medication':
        who_data = {
            '$class': 'org.acme.storage.'+person,
            'medicineId': id,
            'description': name
        }
    else:
        who_data = {
            '$class': 'org.acme.storage.'+person,
            'personId': id,
            'name': name
            }
    rpost = requests.post('http://localhost:3000/api/'+person, data=who_data)
    return redirect('/'+person)

@app.route('/giveMedication', methods=['POST'])
def giveMedication():
    patientId = request.form['patientId'].encode('utf-8')
    giverId = request.form['giverId'].encode('utf-8')
    given = request.form['given'].encode('utf-8')

    if request.form['submit'] == 'Give Medication':
        print(patientId + '  ' + giverId + '  ' + given)
        what_data = {
            '$class': 'org.acme.storage.giveMedication',
            'mypatient': patientId,
            'mydoctor': giverId,
            'mymedication': given,
            'when': datetime.now()
            }
        rpost = requests.post('http://localhost:3000/api/giveMedication', data=what_data)
    else:
        # request.form['submit'] == 'Add Symptoms':
        print(patientId + '  ' + giverId + '  ' + given)
        symp_data = {
            '$class': 'org.acme.storage.addSymptoms',
            'mypatient': patientId,
            'mynurse': giverId,
            'mysymptom': given,
            'when': datetime.now()
            }
        rpost = requests.post('http://localhost:3000/api/addSymptoms', data=symp_data)
    return redirect('/Patient')



port = int(os.getenv('PORT', 5000))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)