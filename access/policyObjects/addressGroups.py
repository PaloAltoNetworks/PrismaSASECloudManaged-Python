import requests

class addressGroups:
	def paAddressGroupsListAddressGroups(self, __folder="Shared", __displayOutput=True):
		"""
		This will list the address group objects from the __folder.
		Folder defaults to shared.
		"""
		__params = { "folder": __folder }
		__response = requests.get(url=self.saseAddressGroupUri, headers=self.saseAuthHeaders, params=__params)
		__response = __response.json()

		if __displayOutput:
#			print("Tag Folder,Tag Name,Tag Color,Tag Comments")
#			for item in __response['data']:
#				if 'color' in item:
#					__itemColor = item['color']
#				else:
#					__itemColor = ''
#	
#				if 'comments' in item:
#					__itemComments = item['comments']
#				else:
#					__itemComments = ''
#	
#				print(f"{item['folder']},{item['name']},{__itemColor},{__itemComments}")
			print(__response)
		return __response

	def paAddressGroupsCreate(self, __addressGroupObject, __folder="Shared"):
		"""
		This will create a address group objects (by default in Shared)
		If your object requires tags, make sure the tag is created first.
		The comments and tag fields are optional.
		__addressGroupObject needs to be in the format:
		{
			"name": "AddressGroupName",
			"static": ["AddressGroup1", "AddressGroup2"],
			"comments": "This is an address group object",
			"tag": ["myTag"]
		}
		"""
		__params = { "folder": __folder }
		__response = requests.post(url=self.saseAddressGroupUri, headers=self.saseAuthHeaders, json=__addressGroupObject, params=__params)
		__responseStatusCode = __response.status_code
		__response = __response.json()

		match __responseStatusCode:
			case 404:
				print(f"404 - An error occured while creating address group {__addressGroupObject['name']} - {__response['_errors'][0]['details']['message']}")
			case 400:
				print("400 - Bad request. Malformed payload.")
			case 201:
				print(f"201 - Tag object {__addressGroupObject['name']} created.")
			case _:
				print("Not sure how to interpret response.")
				print(f"Response Status Code - {__responseStatusCode}")
				print(f"json response = {__response}")

	def paAddressGroupsEdit(self, __addressGroupObject, __folder="Shared"):
		"""
		This will edit an existing address (by default in Shared)
		If your object requires address, make sure the address is created first.
		The comments field are optional.
		__addressGroupObject needs to be in the format:
		{
			"name": "myAddressGroupObject",
			"color": "Azure Blue",
			"comments": "This is a address object",
			"static": ["NewAddress1", "NewAddress2"]
		}

		This will be completed in 2 parts:
		  1. First is to get the unique ID for the address.
		  2. Once we have the unique ID, we can change the information about it (except the unique ID)
		"""
		myAddressGroupList = self.paAddressGroupsListAddressGroups(__folder,False)
		myAddressGroupId = ""
		if 'data' in myAddressGroupList:
			# Let's go and find the address ID
			for item in myAddressGroupList['data']:
				if item['name'] == __addressGroupObject['name']:
					myAddressGroupId = item['id']
					break

		if myAddressGroupId != "":
			# We should now have the ID.
			__addressGroupEditUri = self.saseAddressGroupUri + f"/{myAddressGroupId}"
			__params = { "folder": __folder }
			__response = requests.put(url=__addressGroupEditUri, headers=self.saseAuthHeaders, json=__addressGroupObject, params=__params)
			__responseStatusCode = __response.status_code
			__response = __response.json()

			match __responseStatusCode:
				case 404:
					print(f"404 - An error occured while creating address {__addressGroupObject['name']} - {__response['_errors'][0]['details']['message']}")
				case 400:
					print("400 - Bad request. Malformed payload.")
				case 200:
					print(f"200 - Address object {__addressGroupObject['name']} edited.")
				case _:
					print("Not sure how to interpret response.")
					print(f"Response Status Code - {__responseStatusCode}")
					print(f"json response = {__response}")
		else:
			print(f"Unable to find address ID in {__folder}.")

	def paAddressGroupsDelete(self, __addressGroupObject, __folder="Shared"):
		"""
		This will delete an existing address (by default in Shared)
		If your object requires addresss, make sure the address is created first.
		The comments field are optional.
		__addressObject needs to be in the format:
		{
			"name": "myAddressGroupObject",
		}

		This will be completed in 2 parts:
		  1. First is to get the unique ID for the address.
		  2. Once we have the unique ID, we can delete the address
		"""
		myAddressGroupList = self.paAddressGroupsListAddressGroups(__folder,False)
		myAddressGroupId = ""
		if 'data' in myAddressGroupList:
			# Let's go and find the address ID
			for item in myAddressGroupList['data']:
				if item['name'] == __addressGroupObject['name'] and item['folder'] == __folder:
					myAddressGroupId = item['id']
					break
		
		objectToDelete = {
			"id": f"{myAddressGroupId}"
		}

		if myAddressGroupId != "":
			# We should now have the ID.
			__addressGroupDeleteUri = self.saseAddressGroupUri + f"/{myAddressGroupId}"
			__params = { "folder": __folder }
			__response = requests.delete(url=__addressGroupDeleteUri, headers=self.saseAuthHeaders, json=__addressGroupObject, params=__params)
			__responseStatusCode = __response.status_code
			__response = __response.json()

			match __responseStatusCode:
				case 409:
					print(f"409 - Cannot delete address object being referenced {__response['_errors'][0]['details']['message']}")
				case 404:
					print(f"404 - An error occured while creating address {__addressGroupObject['name']} - {__response['_errors'][0]['details']['message']}")
				case 400:
					print("400 - Bad request. Malformed payload.")
				case 200:
					print(f"200 - Address object {__addressGroupObject['name']} deleted.")
				case _:
					print("Not sure how to interpret response.")
					print(f"Response Status Code - {__responseStatusCode}")
					print(f"json response = {__response}")
		else:
			print(f"Unable to find address ID in {__folder}.")

	def __init__(self, __saseApi, __saseToken, __saseContentType, __saseAuthHeaders):
		"""addressGroups Class Initilization"""
		self.saseApi = __saseApi
		self.saseToken = __saseToken
		self.saseContentType = __saseContentType
		self.saseAuthHeaders = __saseAuthHeaders
		self.saseAddressGroupUri = self.saseApi + "/sse/config/v1/address-groups"