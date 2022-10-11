import requests

class listLocations:
	def paLocationsListLocations(self):
		"""This will list the locations"""
		__response = requests.get(url=self.saseLocationsUri, headers=self.saseAuthHeaders)
		__response = __response.json()

		print("value,display,continent,latitude,longitude,region,aggregate_region")

		for item in __response:
			print(f"{item['value']},{item['display']},{item['continent']},{item['latitude']},{item['longitude']},{item['region']},{item['aggregate_region']}")

	def __init__(self, __saseApi, __saseToken, __saseContentType, __saseAuthHeaders):
		"""listLocations Class Initilization"""
		self.saseApi = __saseApi
		self.saseToken = __saseToken
		self.saseContentType = __saseContentType
		self.saseAuthHeaders = __saseAuthHeaders
		self.saseLocationsUri = self.saseApi + "/sse/config/v1/locations"

