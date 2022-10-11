import requests

class ikeGateways:
	def paIkeGatewaysListIkeGateways(self, __folder="Service Connections"):
		"""This will list the locations"""
		__params = { "folder": __folder }

		__response = requests.get(url=self.saseIkeGatewaysUri, headers=self.saseAuthHeaders, params=__params)
		__response = __response.json()

		for item in __response['data']:
			print(item)
		#	print(f"{item['value']},{item['display']},{item['continent']},{item['latitude']},{item['longitude']},{item['region']},{item['aggregate_region']}")

	def __init__(self, __saseApi, __saseToken, __saseContentType, __saseAuthHeaders):
		"""ikeGateways Class Initilization"""
		self.saseApi = __saseApi
		self.saseToken = __saseToken
		self.saseContentType = __saseContentType
		self.saseAuthHeaders = __saseAuthHeaders
		self.saseIkeGatewaysUri = self.saseApi + "/sse/config/v1/ike-gateways"