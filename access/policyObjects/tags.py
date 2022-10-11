import requests

class tags:
	"""tags class"""
	
	def paTagsListTags(self, __folder="Shared"):
		"""
		This will list the tags from the __folder.
		Folder defaults to shared.
		"""
		__params = { "folder": __folder }
		__response = requests.get(url=self.saseTagsUri, headers=self.saseAuthHeaders, params=__params)
		__response = __response.json()

		print("Tag Folder,Tag Name,Tag Color,Tag Comments")
		if 'data' in __response:
			for item in __response['data']:
				if 'color' in item:
					__itemColor = item['color']
				else:
					__itemColor = ''

				if 'comments' in item:
					__itemComments = item['comments']
				else:
					__itemComments = ''

				print(f"{item['folder']},{item['name']},{__itemColor},{__itemComments}")
		else:
			print("Error handling response")
			print(__response)

	def paTagCreate(self, __tagObject, __folder="Shared"):
		"""
		This will create a tags (by default in Shared)
		If your object requires tags, make sure the tag is created first.
		The comments field are optional.
		__tagObject needs to be in the format:
		{
			"name": "myFqdnObject",
			"color": "thisisahostname.com",
			"comments": "This is a FQDN Object",
		}
		"""
		__params = { "folder": __folder }
		__response = requests.post(url=self.saseTagsUri, headers=self.saseAuthHeaders, json=__tagObject, params=__params)
		__responseStatusCode = __response.status_code
		__response = __response.json()

		match __responseStatusCode:
			case 404:
				print(f"404 - An error occured while creating tag {__tagObject['name']} - {__response['_errors'][0]['details']['message']}")
			case 400:
				print("400 - Bad request. Malformed payload.")
			case 201:
				print(f"201 - Tag object {__tagObject['name']} created.")
			case _:
				print("Not sure how to interpret response.")
				print(f"Response Status Code - {__responseStatusCode}")
				print(f"json response = {__response}")

	def __init__(self, __saseApi, __saseToken, __saseContentType, __saseAuthHeaders):
		"""listLocations Class Initilization"""
		self.saseApi = __saseApi
		self.saseToken = __saseToken
		self.saseContentType = __saseContentType
		self.saseAuthHeaders = __saseAuthHeaders
		self.saseTagsUri = self.saseApi + "/sse/config/v1/tags"
