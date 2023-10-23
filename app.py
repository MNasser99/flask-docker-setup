from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
import mysql.connector

app = Flask("Flask Docker")
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('password', type=str, required=True)

# function to save to db
def SavetoDB(args):
    connection = mysql.connector.connect(host='mysql', database='flask_db', user='flask_user', password='password', port=3306)
    if connection.is_connected():
        sql_select_Query = f"INSERT INTO users (username, password) VALUES ('{args['username']}', '{args['password']}')"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        connection.commit()

        # Closing the connection.
        cursor.close()
        connection.close()

class History(Resource):
    def get(self):
        return "Hello World!"
    
    def post(self):
        args = parser.parse_args()
        SavetoDB(args)


# Example curl to test the post request:
# curl -X POST http://localhost:5000/ -H "Content-Type: application/json" -d '{"username":"MNasser", "password":"123456789"}'
api.add_resource(History, '/')

if __name__=='__main__':
   app.run()