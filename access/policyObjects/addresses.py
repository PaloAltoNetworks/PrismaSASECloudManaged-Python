import requests

class addresses:
	"""addresses class"""

	def paAddressesListAddresses(self, __folder="Shared"):
		"""
		This will list the addresses from the folder.
		Folder defaults to shared.
		"""
		__params = { "folder": __folder }
		__response = requests.get(url=self.saseAddressesUri, headers=self.saseAuthHeaders, params=__params)
		__response = __response.json()

		print(__response)

	def paAddressesCreate(self, __addressObject, __folder="Shared"):
		"""
		This will create an address object (by default in Shared)
		If your object requires tags, make sure the tag is created first.
		The descrption and tag values are optional.
		__addressObject needs to be in the format:
		{
			"name": "myFqdnObject",
			"fqdn": "thisisahostname.com",
			"description": "This is a FQDN Object",
			"tag": [ "ADEM" ]
		}
		or
		{
			"name": "myNetmaskObject",
			"ip_netmask": "192.168.100.0/24",
			"description": "This is an IP Netmask Object",
			"tag": [ "ADEM" ]
		}
		or
		{
			"name": "myIpWildcardObject",
			"ip_wildcard": "10.20.1.0/0.0.248.255",
			"description": "This is an IP Wildcard Object",
			"tag": [ "ADEM" ]
		}
		or
		{
			"name": "myIpRangeObject",
			"ip_range": "10.1.1.1-10.1.1.10",
			"description": "This is an IP Range Object",
			"tag": [ "ADEM" ]
		}
		"""
		__params = { "folder": __folder }
		__response = requests.post(url=self.saseAddressesUri, headers=self.saseAuthHeaders, json=__addressObject, params=__params)
		__responseStatusCode = __response.status_code
		__response = __response.json()

		match __responseStatusCode:
			case 404:
				print(f"404 - An error occured while creating object {__addressObject['name']} - {__response['_errors'][0]['details']['message']}")
			case 400:
				print("400 - Bad request. Malformed payload.")
			case 201:
				print(f"201 - Address object {__addressObject['name']} created.")
			case _:
				print("Not sure how to interpret response.")
				print(f"Response Status Code - {__responseStatusCode}")
				print(f"json response = {__response}")


	def __init__(self, __saseApi, __saseToken, __saseContentType, __saseAuthHeaders):
		"""licenseTypes Class Initilization"""
		self.saseApi = __saseApi
		self.saseToken = __saseToken
		self.saseContentType = __saseContentType
		self.saseAuthHeaders = __saseAuthHeaders
		self.saseAddressesUri = self.saseApi + "/sse/config/v1/addresses"