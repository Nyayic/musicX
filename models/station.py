#create list stations
stations = []
class Station:
	"""docstring for Station"""
	def __init__(self, name, address):
		name=self.name
		address=self.address

	"""create a function to get station"""
	@staticmethod
	def get_station():
		return stations

	def create_station(self, fm_band):
			station = dict(
				name = self.name,
				address = self.address,
				fm_band = self.fm_band

				)

			station.append(station) #to add an item to the list
			return station   #return the station you created

	@staticmethod
	def get_station(name):
			
		for station in stations:
				if station["name"] == name:
						return station
				else:
					return None			
		