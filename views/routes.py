from flask import Flask, jsonify, request
from controllers.station_controller import StationController

app = Flask(__name__)

@app.route("/", methods = ["GET"])
#create a default function
def index():
	return "This is the MusicX API"

@app.route("/api/v1/stations/<name>", methods=["GET"]) #api version
def get_station(name):
	data = request.get_json()

	name = data.get("name")

	station = StationController.get_station(name)
	return station
	
@app.route('/api/v1/stations', methods=["POST"])
def create_station():
	data = data.get('name')
	address=data.get('address')	
	fm_band =data.get('fm_band')

	station_controller = StationController(name, address)
	station = station_controller.create_station(fm_band)
	return jsonify({
		"message":"station sucessfully created"
		})

@staticmethod
def get_stations():
	model = Station("","")

	stations = model.get_stations()

	if len(stations) ==0:
		return({
			"message":"sorry, no stations were found"
			})