import requests

class saseApi:
	"""saseApi class"""

	def paList(self, __folder="Shared", __position="pre", includePosition=False, __displayOutput=False):
		"""
		This will list the addresses from the folder.
		Folder defaults to shared.
		Position is included in params if includePosition=True. Position defaults to pre.
		"""
		__params = { "folder": __folder, "limit": self.saseLimit }
		if includePosition:
			__params["position"] = __position
		__response = requests.get(url=self.saseUri, headers=self.saseAuthHeaders, params=__params)
		__response = __response.json()

		if __response["total"] > self.saseLimit:
			# There are more than self.saseLimit (default: 200) objects retrieved. We need to get through the entire list.
			numRecords = 0

			while numRecords < __response["total"]:
				"""
				Perform all API queries until we've retrieved all objects.
				"""
				numRecords = len(__response["data"])

				# Update the offset to reflect the number of records already retrieved.
				__params2 = { "folder": __folder, "offset": numRecords, "limit": self.saseLimit }
				if includePosition:
					__params2["position"] = __position

				__response2 = requests.get(url=self.saseUri, headers=self.saseAuthHeaders, params=__params2)
				__response2 = __response2.json()

				if "data" in __response2:
					# Append the next batch of application objects to the original data object that we retrieved from __response.
					__response["data"] = [*__response["data"], *(__response2["data"])]

		if __displayOutput:
			# We need to display the output to stdout.
			print(__response)
		return __response

	def paCreate(self, __jsonObject, __folder="Shared", __position="pre", includePosition=False):
		"""
		This will create an object (by default in Shared)
		"""
		__params = { "folder": __folder }
		if includePosition:
			__params["position"] = __position
		__response = requests.post(url=self.saseUri, headers=self.saseAuthHeaders, json=__jsonObject, params=__params)
		__responseStatusCode = __response.status_code
		__response = __response.json()

		match __responseStatusCode:
			case 404:
				print(f"jsonobject = {__jsonObject}")
				print(f"response = {__response}")
				print(f"404 - An error occured while creating object {__jsonObject['name']} - {__response['_errors'][0]['details']['message']} in folder {__folder}")
			case 400:
				print("400 - Bad request. Malformed payload.")
			case 201:
				print(f"201 - Object {__jsonObject['name']} created in folder {__folder}.")
			case _:
				print("Not sure how to interpret response.")
				print(f"Response Status Code - {__responseStatusCode}")
				print(f"json response = {__response}")

	def paEdit(self, __jsonObject, __folder="Shared", __position="pre", includePosition=False):
		"""
		This will edit an existing object (by default in Shared)
		If your object references something external from it e.g. an address-group referencing an address object, make sure the address is created first.
		This will be completed in 2 parts:
		  1. First is to get the unique ID for the address.
		  2. Once we have the unique ID, we can change the information about it (except the unique ID)
		"""
		myList = self.paList(__folder, __position, True, False) if includePosition else self.paList(__folder, False, False)
		myObjectId = ""
		if 'data' in myList:
			# Let's go and find the object ID
			for item in myList['data']:
				if __folder != "Service Connections":
					if item['name'] == __jsonObject['name'] and item['folder'] == __folder:
						myObjectId = item['id']
						break
				else:
					if item['name'] == __jsonObject['name']:
						myObjectId = item['id']
						break

		if myObjectId != "":
			# We should now have the ID.
			__editUri = self.saseUri + f"/{myObjectId}"
			__params = { "folder": __folder }
			if includePosition:
				__params["position"] = __position
			__response = requests.put(url=__editUri, headers=self.saseAuthHeaders, json=__jsonObject, params=__params)
			__responseStatusCode = __response.status_code
			__response = __response.json()

			match __responseStatusCode:
				case 404:
					print(f"404 - An error occured while editing object {__jsonObject['name']} - {__response['_errors'][0]['details']['message']} in folder {__folder}.")
				case 400:
					print("400 - Bad request. Malformed payload.")
				case 200:
					print(f"200 - Object {__jsonObject['name']} edited in folder {__folder}.")
				case _:
					print("Not sure how to interpret response.")
					print(f"Response Status Code - {__responseStatusCode}")
					print(f"json response = {__response}")
		else:
			print(f"Unable to find object ID in {__folder}.")

	def paDelete(self, __jsonObject, __folder="Shared", __position="pre", includePosition=False):
		"""
		This will delete an existing object (by default in Shared)
		The comments field are optional.
		__jsonObject needs to be in the format:
		{
			"name": "myObjectName",
		}
		This will be completed in 2 parts:
		  1. First is to get the unique ID for the address.
		  2. Once we have the unique ID, we can delete the address
		"""
		myList = self.paList(__folder, __position, True, False) if includePosition else self.paList(__folder, False, False)
		myObjectId = ""
		if 'data' in myList:
			# Let's go and find the address ID
			for item in myList['data']:
				if (__folder != "Service Connections") or (__folder != "Remote Networks"):
					if item['name'] == __jsonObject['name'] and item['folder'] == __folder:
						myObjectId = item['id']
						break
				else:
					if item['name'] == __jsonObject['name']:
						myObjectId = item['id']
						break

		objectToDelete = {
			"id": f"{myObjectId}"
		}

		if myObjectId != "":
			# We should now have the ID.
			__deleteUri = self.saseUri + f"/{myObjectId}"
			__params = { "folder": __folder }
			if includePosition:
				__params["position"] = __position
			__response = requests.delete(url=__deleteUri, headers=self.saseAuthHeaders, json=__jsonObject, params=__params)
			__responseStatusCode = __response.status_code
			__response = __response.json()

			match __responseStatusCode:
				case 409:
					print(f"409 - Cannot delete object being referenced {__response['_errors'][0]['details']['message']}")
				case 404:
					print(f"404 - An error occured while creating object {__jsonObject['name']} - {__response['_errors'][0]['details']['message']} in folder {__folder}.")
				case 400:
					print("400 - Bad request. Malformed payload.")
				case 200:
					print(f"200 - Object {__jsonObject['name']} deleted in folder {__folder}.")
				case _:
					print("Not sure how to interpret response.")
					print(f"Response Status Code - {__responseStatusCode}")
					print(f"json response = {__response}")
		else:
			print(f"Unable to find object ID in {__folder}.")

	def __init__(self, __saseApi, __saseToken, __saseContentType, __saseAuthHeaders):
		"""saseApi Class Initilization"""
		self.saseUri = __saseApi
		self.saseToken = __saseToken
		self.saseContentType = __saseContentType
		self.saseAuthHeaders = __saseAuthHeaders
		self.saseLimit = 500
