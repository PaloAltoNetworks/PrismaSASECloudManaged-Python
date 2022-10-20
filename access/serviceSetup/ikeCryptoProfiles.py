import requests

class ikeCryptoProfiles:
	"""
	ikeCryptoProfile class. 
	Use this class to list, create, edit, delete IKE crypto profiles
	"""
	def paIkeCryptoProfilesListIkeCryptoProfiles(self, __folder="Service Connections", __displayOutput=True):
		"""This will list the locations"""
		__params = { "folder": __folder }

		__response = requests.get(url=self.saseIkeCryptoProfilesUri, headers=self.saseAuthHeaders, params=__params)
		__response = __response.json()

		if __displayOutput:
			for item in __response['data']:
				print(item)
			#	print(f"{item['value']},{item['display']},{item['continent']},{item['latitude']},{item['longitude']},{item['region']},{item['aggregate_region']}")
		else:
			return __response

	def paIkeCryptoProfilesCreate(self, __ikeCryptoProfileObject, __folder="Shared"):
		"""
		This will create a IKE Crypto Profiles (by default in Shared)
		If your object requires tags, make sure the tag is created first.
		The comments field are optional.
		__ikeProfileObject needs to be in the format:
		{
		}
		"""
		__params = { "folder": __folder }
		__response = requests.post(url=self.saseIkeCryptoProfilesUri, headers=self.saseAuthHeaders, json=__ikeCryptoProfileObject, params=__params)
		__responseStatusCode = __response.status_code
		__response = __response.json()

		match __responseStatusCode:
			case 404:
				print(f"404 - An error occured while editing IKE Crypto Profile {__ikeCryptoProfileObject['name']} - {__response['_errors'][0]['details']['message']} in folder {__folder}.")
			case 400:
				print("400 - Bad request. Malformed payload.")
			case 201:
				print(f"201 - IKE Crypto Profile object {__ikeCryptoProfileObject['name']} created in folder {__folder}.")
			case _:
				print("Not sure how to interpret response.")
				print(f"Response Status Code - {__responseStatusCode}")
				print(f"json response = {__response}")

	def paIkeCryptoProfilesEdit(self, __ikeCryptoProfileObject, __folder="Shared"):
		"""
		This will edit an existing IKE Crypto Profile (by default in Shared)
		If your object requires tags, make sure the tag is created first.
		The comments field are optional.
		__ikeProfileObject needs to be in the format:
		{
		}

		This will be completed in 2 parts:
		  1. First is to get the unique ID for the IKE Crypto Profile.
		  2. Once we have the unique ID, we can change the information about it (except the unique ID)
		"""
		myIkeCryptoProfileList = self.paIkeCryptoProfilesListIkeCryptoProfiles(__folder,False)
		myIkeCryptoProfileId = ""
		if 'data' in myIkeCryptoProfileList:
			# Let's go and find the IKE Crypto Profile ID
			for item in myIkeCryptoProfileList['data']:
				if item['name'] == __ikeCryptoProfileObject['name']:
					myIkeCryptoProfileId = item['id']
					break

		if myIkeCryptoProfileId != "":
			# We should now have the ID.
			__ikeCryptoProfileEditUri = self.saseIkeCryptoProfilesUri + f"/{myIkeCryptoProfileId}"
			__params = { "folder": __folder }
			__response = requests.put(url=__ikeCryptoProfileEditUri, headers=self.saseAuthHeaders, json=__ikeCryptoProfileObject, params=__params)
			__responseStatusCode = __response.status_code
			__response = __response.json()

			match __responseStatusCode:
				case 404:
					print(f"404 - An error occured while Editing IKE Crypto Profile {__ikeCryptoProfileObject['name']} - {__response['_errors'][0]['details']['message']} in folder {__folder}.")
				case 400:
					print("400 - Bad request. Malformed payload.")
				case 200:
					print(f"200 - IKE Crypto Profile object {__ikeCryptoProfileObject['name']} edited in folder {__folder}.")
				case _:
					print("Not sure how to interpret response.")
					print(f"Response Status Code - {__responseStatusCode}")
					print(f"json response = {__response}")
		else:
			print(f"Unable to find IKE Crypto Profile ID in {__folder}.")

	def paIkeCryptoProfilesDelete(self, __ikeCryptoProfileObject, __folder="Shared"):
		"""
		This will delete an existing tag (by default in Shared)
		If your object requires tags, make sure the tag is created first.
		The comments field are optional.
		__ikeCryptoProfileObject needs to be in the format:
		{
			"name": "myIkeCryptoProfileObjectName",
		}

		This will be completed in 2 parts:
		  1. First is to get the unique ID for the IKE Crypto Profile.
		  2. Once we have the unique ID, we can change the information about it (except the unique ID)
		"""
		myIkeCryptoProfileList = self.paIkeCryptoProfilesListIkeCryptoProfiles(__folder,False)
		myIkeCryptoProfileId = ""
		if 'data' in myIkeCryptoProfileList:
			# Let's go and find the IKE Crypto Profile ID
			for item in myIkeCryptoProfileList['data']:
				if item['name'] == __ikeCryptoProfileObject['name']:
					myIkeCryptoProfileId = item['id']
					break
		
		objectToDelete = {
			"id": f"{myIkeCryptoProfileId}"
		}

		if myIkeCryptoProfileId != "":
			# We should now have the ID.
			__ikeCryptoDeleteUri = self.saseIkeCryptoProfilesUri + f"/{myIkeCryptoProfileId}"
			__params = { "folder": __folder }
			__response = requests.delete(url=__ikeCryptoDeleteUri, headers=self.saseAuthHeaders, json=__ikeCryptoProfileObject, params=__params)
			__responseStatusCode = __response.status_code
			__response = __response.json()

			match __responseStatusCode:
				case 404:
					print(f"404 - An error occured while creating tag {__ikeCryptoProfileObject['name']} - {__response['_errors'][0]['details']['message']} in folder {__folder}.")
				case 400:
					print("400 - Bad request. Malformed payload.")
				case 200:
					print(f"200 - IKE Crypto Profile object {__ikeCryptoProfileObject['name']} deleted in folder {__folder}.")
				case _:
					print("Not sure how to interpret response.")
					print(f"Response Status Code - {__responseStatusCode}")
					print(f"json response = {__response}")
		else:
			print(f"Unable to find IKE Crypto Profile ID in {__folder}.")

	def __init__(self, __saseApi, __saseToken, __saseContentType, __saseAuthHeaders):
		"""ikeCryptoProfiles Class Initilization"""
		self.saseApi = __saseApi
		self.saseToken = __saseToken
		self.saseContentType = __saseContentType
		self.saseAuthHeaders = __saseAuthHeaders
		self.saseIkeCryptoProfilesUri = self.saseApi + "/sse/config/v1/ike-crypto-profiles"