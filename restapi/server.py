from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify

db_connect = create_engine('sqlite:///measures.sqlite')
app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select * from area")  # This line performs query and returns json result
        return {'area': [ i for i in query.cursor.fetchall()]}  # Fetches first column that is Employee ID



class Location(Resource):
    def get(self, locationId):
        conn = db_connect.connect()
        query = conn.execute("select * from location where location_area = %d "  %int(locationId))
        result = {'name': [i for i in query.cursor]}
        return jsonify(result)


class Measuresment(Resource):
    def get(self, locationId):
        conn = db_connect.connect()
        query = conn.execute("select value from measurement where measurement_location = %d "  %int(locationId))
        result = {'value': [i[0] for i in query.cursor]}
        return jsonify(result)


class Measuresment(Resource):
    def get(self, locationId):
        conn = db_connect.connect()
        query = conn.execute("select * from measurement where measurement_location = %d "  %int(locationId))
        result = {'value': [i for i in query.cursor]}
        return jsonify(result)


class Categories(Resource):
    def get(self, areaId):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM category WHERE category_id IN (SELECT category_id   FROM category_area WHERE area_id = %d)" %int(areaId));
        result = {'value': [i for i in query.cursor]}
        return jsonify(result)





api.add_resource(Employees, '/area')  # Route_1
api.add_resource(Location, '/area/<locationId>/location') # Route_3
api.add_resource(Measuresment, '/location/<locationId>/measurement') # Route_3
api.add_resource(Categories, '/area/<areaId>/category') # Route_3

#http://127.0.0.1:5002/location/11/measurement





if __name__ == '__main__':
    app.run(port='5002')



#SELECT * FROM category WHERE category_id IN (SELECT category_id   FROM category_area WHERE area_id = 4);

