from flask import jsonify
from models import station

class StationController:
	"""docstring for StationController"""
	def __init__(self, name, address):
		name=self.name
		address=self.address

	@staticmethod
	#to call modules, we check if they are strings,int or...other
	def get_station(name):
		if not name or name.isspace():
			return jsonify({
					"message":"name is required"
			})
		if type(name) !=str: #validating 
			return jsonify({
				"message":"name should be a string"
			})	
	
		station = station.Station().get_station(name)
		if station is None:
			return jsonify({
				"message":"station was not found"
				}),200
			return jsonify({
				"message":"successful"
				
				})