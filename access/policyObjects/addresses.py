import requests

class addresses:
	"""addresses class"""

	def paAddressesListAddresses(self, __folder="Shared", __displayOutput=True):
		"""
		This will list the addresses from the folder.
		Folder defaults to shared.
		"""
		__params = { "folder": __folder }
		__response = requests.get(url=self.saseAddressesUri, headers=self.saseAuthHeaders, params=__params)
		__response = __response.json()

		if __displayOutput:
			print(__response)
		return __response

	def paAddressesCreate(self, __addressObject, __folder="Shared"):
		"""
		This will create an address object (by default in Shared)
		If your object requires addresss, make sure the address is created first.
		The descrption and address values are optional.
		__addressObject needs to be in the format:
		{
			"name": "myFqdnObject",
			"fqdn": "thisisahostname.com",
			"description": "This is a FQDN Object",
			"address": [ "ADEM" ]
		}
		or
		{
			"name": "myNetmaskObject",
			"ip_netmask": "192.168.100.0/24",
			"description": "This is an IP Netmask Object",
			"address": [ "ADEM" ]
		}
		or
		{
			"name": "myIpWildcardObject",
			"ip_wildcard": "10.20.1.0/0.0.248.255",
			"description": "This is an IP Wildcard Object",
			"address": [ "ADEM" ]
		}
		or
		{
			"name": "myIpRangeObject",
			"ip_range": "10.1.1.1-10.1.1.10",
			"description": "This is an IP Range Object",
			"address": [ "ADEM" ]
		}
		"""
		__params = { "folder": __folder }
		__response = requests.post(url=self.saseAddressesUri, headers=self.saseAuthHeaders, json=__addressObject, params=__params)
		__responseStatusCode = __response.status_code
		__response = __response.json()

		match __responseStatusCode:
			case 404:
				print(f"404 - An error occured while creating object {__addressObject['name']} - {__response['_errors'][0]['details']['message']} in folder {__folder}")
			case 400:
				print("400 - Bad request. Malformed payload.")
			case 201:
				print(f"201 - Address object {__addressObject['name']} created in folder {__folder}.")
			case _:
				print("Not sure how to interpret response.")
				print(f"Response Status Code - {__responseStatusCode}")
				print(f"json response = {__response}")

	def paAddressesEdit(self, __addressObject, __folder="Shared"):
		"""
		This will edit an existing address (by default in Shared)
		If your object requires address, make sure the address is created first.
		The comments field are optional.
		__addressObject needs to be in the format:
		{
			"name": "myAddressObject",
			"color": "Azure Blue",
			"comments": "This is a address object",
		}

		This will be completed in 2 parts:
		  1. First is to get the unique ID for the address.
		  2. Once we have the unique ID, we can change the information about it (except the unique ID)
		"""
		myAddressList = self.paAddressesListAddresses(__folder,False)
		myAddressId = ""
		if 'data' in myAddressList:
			# Let's go and find the address ID
			for item in myAddressList['data']:
				if item['name'] == __addressObject['name']:
					myAddressId = item['id']
					break

		if myAddressId != "":
			# We should now have the ID.
			__addressEditUri = self.saseAddressesUri + f"/{myAddressId}"
			__params = { "folder": __folder }
			__response = requests.put(url=__addressEditUri, headers=self.saseAuthHeaders, json=__addressObject, params=__params)
			__responseStatusCode = __response.status_code
			__response = __response.json()

			match __responseStatusCode:
				case 404:
					print(f"404 - An error occured while creating address {__addressObject['name']} - {__response['_errors'][0]['details']['message']} in folder {__folder}.")
				case 400:
					print("400 - Bad request. Malformed payload.")
				case 200:
					print(f"200 - Address object {__addressObject['name']} edited in folder {__folder}.")
				case _:
					print("Not sure how to interpret response.")
					print(f"Response Status Code - {__responseStatusCode}")
					print(f"json response = {__response}")
		else:
			print(f"Unable to find address ID in {__folder}.")

	def paAddressesDelete(self, __addressObject, __folder="Shared"):
		"""
		This will delete an existing address (by default in Shared)
		If your object requires addresss, make sure the address is created first.
		The comments field are optional.
		__addressObject needs to be in the format:
		{
			"name": "myAddressObject",
		}

		This will be completed in 2 parts:
		  1. First is to get the unique ID for the address.
		  2. Once we have the unique ID, we can delete the address
		"""
		myAddressList = self.paAddressesListAddresses(__folder,False)
		myAddressId = ""
		if 'data' in myAddressList:
			# Let's go and find the address ID
			for item in myAddressList['data']:
				if item['name'] == __addressObject['name'] and item['folder'] == __folder:
					myAddressId = item['id']
					break
		
		objectToDelete = {
			"id": f"{myAddressId}"
		}

		if myAddressId != "":
			# We should now have the ID.
			__addressDeleteUri = self.saseAddressesUri + f"/{myAddressId}"
			__params = { "folder": __folder }
			__response = requests.delete(url=__addressDeleteUri, headers=self.saseAuthHeaders, json=__addressObject, params=__params)
			__responseStatusCode = __response.status_code
			__response = __response.json()

			match __responseStatusCode:
				case 409:
					print(f"409 - Cannot delete address object being referenced {__response['_errors'][0]['details']['message']}")
				case 404:
					print(f"404 - An error occured while creating address {__addresssObject['name']} - {__response['_errors'][0]['details']['message']} in folder {__folder}.")
				case 400:
					print("400 - Bad request. Malformed payload.")
				case 200:
					print(f"200 - Address object {__addressObject['name']} deleted in folder {__folder}.")
				case _:
					print("Not sure how to interpret response.")
					print(f"Response Status Code - {__responseStatusCode}")
					print(f"json response = {__response}")
		else:
			print(f"Unable to find address ID in {__folder}.")

	def __init__(self, __saseApi, __saseToken, __saseContentType, __saseAuthHeaders):
		"""licenseTypes Class Initilization"""
		self.saseApi = __saseApi
		self.saseToken = __saseToken
		self.saseContentType = __saseContentType
		self.saseAuthHeaders = __saseAuthHeaders
		self.saseAddressesUri = self.saseApi + "/sse/config/v1/addresses"