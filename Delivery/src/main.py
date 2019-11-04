from flask import Flask, jsonify, request
import mysql.connector

db_host = "localhost"
db_port = "3306"
db_user = "delivery"
db_passwd = "delivery@2019!"
database = "restaurant"

db = mysql.connector.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    passwd=db_passwd,
    auth_plugin='mysql_native_password',
    database=database
)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
                post_data = request.get_json()
                return jsonify({'Data Received' :  post_data}), 201
        else:
                return jsonify({'sample_get': 'hello world!'})


@app.route('/content/names/<str: name>', methods=['GET'])
def search_name(name):
        if db.contains(name): #pseudo codigo
                return jsonify({
                        'name': name,
                        'id' : id
                 })
        else:
                return jsonify({
                        'Name not Found': name
                })


