import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, request, jsonify

app = Flask(__name__)

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'demo12-d4cf8',
})

db = firestore.client()


@app.route('/')
def hello_world():
    print(db)
    return "hello"


# @app.route('/insert')
# def add_data_one():
#      db = firestore.Client()
#      doc_ref = db.collection(u'users').document(u'all')
#      doc_ref.set({
#          u'username': u'siddesha',
#          u'password': u'123456',
#          u'born': 1987
#      })
#      return 'inserted'


# @app.route('/read')
# def get_collection():
#     db = firestore.Client()
#     # [START quickstart_get_collection]
#     users_ref = db.collection(u'users')
#     docs = users_ref.stream()
#
#     for doc in docs:
#         print(u'{} => {}'.format(doc.id, doc.to_dict()))
#     return 'reading data'


@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    rpassword = request.json['rpassword']
    users = {
        username:'username',
        password:'password',
        rpassword:'rpassword'

    }
    return users


@app.route('/send', methods=['POST'])
def send():
    db = firestore.Client()
    doc_ref = db.collection(u'users').document(u'all')
    user = request.json['username']
    pasw = request.json['password']
    passr = request.json['rpassword']
    if pasw == passr:
       resp = doc_ref.set({
         u'username': user,
         u'password': pasw,
    })
    else:
       return "Please Try again"
    if resp:
        return "Inserted"
    else:
        return "Try again"


@app.route('/valreg', methods=['POST'])
def valreg():
    db = firestore.Client()
    user = request.json['username']
    pasw = request.json['password']
    passr = request.json['rpassword']
    resp = db.collection(u'users').where(u'username', u'==', True).stream()
    for doc in resp:
     print(u'{} => {}'.format(doc.id, doc.to_dict()))
    if resp:
        return "Please retry with different username"
    else:
        # resp = doc_ref.set({
        #    u'username':user,
        #    u'password':pasw,
        # })
        if user == '0':
            return "Please Enter a Username "
        else:
            return "The username is accepted "
















































