import requests

class addressGroups:
	def paAddressGroupsListAddressGroups(self, __folder="Shared"):
		"""
		This will list the address group objects from the __folder.
		Folder defaults to shared.
		"""
		__params = { "folder": __folder }
		__response = requests.get(url=self.saseAddressGroupUri, headers=self.saseAuthHeaders, params=__params)
		__response = __response.json()
		print(__response)
#		print("Tag Folder,Tag Name,Tag Color,Tag Comments")
#		for item in __response['data']:
#			if 'color' in item:
#				__itemColor = item['color']
#			else:
#				__itemColor = ''
#
#			if 'comments' in item:
#				__itemComments = item['comments']
#			else:
#				__itemComments = ''
#
#			print(f"{item['folder']},{item['name']},{__itemColor},{__itemComments}")
			
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

	def __init__(self, __saseApi, __saseToken, __saseContentType, __saseAuthHeaders):
		"""addressGroups Class Initilization"""
		self.saseApi = __saseApi
		self.saseToken = __saseToken
		self.saseContentType = __saseContentType
		self.saseAuthHeaders = __saseAuthHeaders
		self.saseAddressGroupUri = self.saseApi + "/sse/config/v1/address-groups"