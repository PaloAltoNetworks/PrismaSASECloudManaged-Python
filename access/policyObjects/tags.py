import requests

class tags:
	"""tags class"""
	
	def paTagsListTags(self, __folder="Shared", __displayOutput=True):
		"""
		This will list the tags from the __folder.
		Folder defaults to shared.
		"""
		__params = { "folder": __folder }
		__response = requests.get(url=self.saseTagsUri, headers=self.saseAuthHeaders, params=__params)
		__response = __response.json()

		if __displayOutput:
			print("Tag Folder,Tag ID, Tag Name,Tag Color,Tag Comments")
			if 'data' in __response:
				for item in __response['data']:
					if 'color' in item:
						__itemColor = item['color']
					else:
						__itemColor = ""

					if 'comments' in item:
						__itemComments = item['comments']
					else:
						__itemComments = ""

					if 'id' in item:
						__itemId = item['id']
					else:
						__itemId = ""

					print(f"{item['folder']},{__itemId},{item['name']},{__itemColor},{__itemComments}")
			else:
				print("Error handling response")
				print(__response)

		return __response

	def paTagCreate(self, __tagObject, __folder="Shared"):
		"""
		This will create a tags (by default in Shared)
		If your object requires tags, make sure the tag is created first.
		The comments field are optional.
		__tagObject needs to be in the format:
		{
			"name": "myUniqueTag",
			"color": "Azure Blue",
			"comments": "This is a tag Object",
		}
		"""
		__params = { "folder": __folder }
		__response = requests.post(url=self.saseTagsUri, headers=self.saseAuthHeaders, json=__tagObject, params=__params)
		__responseStatusCode = __response.status_code
		__response = __response.json()

		match __responseStatusCode:
			case 404:
				print(f"404 - An error occured while editing tag {__tagObject['name']} - {__response['_errors'][0]['details']['message']} in folder {__folder}.")
			case 400:
				print("400 - Bad request. Malformed payload.")
			case 201:
				print(f"201 - Tag object {__tagObject['name']} created in folder {__folder}.")
			case _:
				print("Not sure how to interpret response.")
				print(f"Response Status Code - {__responseStatusCode}")
				print(f"json response = {__response}")

	def paTagEdit(self, __tagObject, __folder="Shared"):
		"""
		This will edit an existing tag (by default in Shared)
		If your object requires tags, make sure the tag is created first.
		The comments field are optional.
		__tagObject needs to be in the format:
		{
			"name": "myTagObject",
			"color": "Azure Blue",
			"comments": "This is a tag object",
		}

		This will be completed in 2 parts:
		  1. First is to get the unique ID for the tag.
		  2. Once we have the unique ID, we can change the information about it (except the unique ID)
		"""
		myTagList = self.paTagsListTags(__folder,False)
		myTagId = ""
		if 'data' in myTagList:
			# Let's go and find the tag ID
			for item in myTagList['data']:
				if item['name'] == __tagObject['name']:
					myTagId = item['id']
					break

		if myTagId != "":
			# We should now have the ID.
			__tagEditUri = self.saseTagsUri + f"/{myTagId}"
			__params = { "folder": __folder }
			__response = requests.put(url=__tagEditUri, headers=self.saseAuthHeaders, json=__tagObject, params=__params)
			__responseStatusCode = __response.status_code
			__response = __response.json()

			match __responseStatusCode:
				case 404:
					print(f"404 - An error occured while creating tag {__tagObject['name']} - {__response['_errors'][0]['details']['message']} in folder {__folder}.")
				case 400:
					print("400 - Bad request. Malformed payload.")
				case 200:
					print(f"200 - Tag object {__tagObject['name']} edited in folder {__folder}.")
				case _:
					print("Not sure how to interpret response.")
					print(f"Response Status Code - {__responseStatusCode}")
					print(f"json response = {__response}")
		else:
			print(f"Unable to find tag ID in {__folder}.")

	def paTagDelete(self, __tagObject, __folder="Shared"):
		"""
		This will delete an existing tag (by default in Shared)
		If your object requires tags, make sure the tag is created first.
		The comments field are optional.
		__tagObject needs to be in the format:
		{
			"name": "myTagObject",
		}

		This will be completed in 2 parts:
		  1. First is to get the unique ID for the tag.
		  2. Once we have the unique ID, we can delete the tag
		"""
		myTagList = self.paTagsListTags(__folder,False)
		myTagId = ""
		if 'data' in myTagList:
			# Let's go and find the tag ID
			for item in myTagList['data']:
				if item['name'] == __tagObject['name'] and item['folder'] == __folder:
					myTagId = item['id']
					break
		
		objectToDelete = {
			"id": f"{myTagId}"
		}

		if myTagId != "":
			# We should now have the ID.
			__tagDeleteUri = self.saseTagsUri + f"/{myTagId}"
			__params = { "folder": __folder }
			__response = requests.delete(url=__tagDeleteUri, headers=self.saseAuthHeaders, json=__tagObject, params=__params)
			__responseStatusCode = __response.status_code
			__response = __response.json()

			match __responseStatusCode:
				case 404:
					print(f"404 - An error occured while creating tag {__tagObject['name']} - {__response['_errors'][0]['details']['message']} in folder {__folder}.")
				case 400:
					print("400 - Bad request. Malformed payload.")
				case 200:
					print(f"200 - Tag object {__tagObject['name']} deleted in folder {__folder}.")
				case _:
					print("Not sure how to interpret response.")
					print(f"Response Status Code - {__responseStatusCode}")
					print(f"json response = {__response}")
		else:
			print(f"Unable to find tag ID in {__folder}.")


	def __init__(self, __saseApi, __saseToken, __saseContentType, __saseAuthHeaders):
		"""listLocations Class Initilization"""
		self.saseApi = __saseApi
		self.saseToken = __saseToken
		self.saseContentType = __saseContentType
		self.saseAuthHeaders = __saseAuthHeaders
		self.saseTagsUri = self.saseApi + "/sse/config/v1/tags"
