import requests
from datetime import datetime, timedelta
import json

class saseAuthentication:
	def prismaAccessAuthLoadToken(self):
		"""
		Loads the token information from authToken.json
		Format of file is as follows (the values are all fake data):
		{
			"tsg_id": "102389541",
			"client_id": "this.is.my.client.id@102389541.iam.panserviceaccount.com"
			"client_secret": "5667bc3-beda-810c-a015-123451ba514c"
		}
		"""
		__myToken = {}
		
		with open("authToken.json") as __jAuthToken:
			__myAuthToken = __jAuthToken.read()

		__myAuthTokenJson = json.loads(__myAuthToken)
		__auth_url = "https://auth.apps.paloaltonetworks.com/oauth2/access_token"
		__auth_headers = {'Content-Type': 'application/x-www-form-urlencoded',}
		__auth_data = 'grant_type=client_credentials&scope=tsg_id:' + __myAuthTokenJson["tsg_id"]
		__auth_info = (__myAuthTokenJson["client_id"], __myAuthTokenJson["client_secret"])
		__response = requests.post(url=__auth_url, headers=__auth_headers, data=__auth_data, auth=__auth_info)

		if __response.status_code == 200:
			__response = __response.json()
			__myToken["access_token"] = __response["access_token"]
			__myToken["expires_on"] = datetime.now() + timedelta(seconds=int(__response["expires_in"]))
			self.saseToken["bearerToken"] = __response["access_token"]
			self.saseToken["expiresOn"] = __myToken["expires_on"]
		else:
			print("Failed to generate auth token")

	def prismaAccessAuth(self,TSG_ID, CLIENT_ID, CLIENT_SECRET):
		"""
		This def returns a usable token for interacting with the SASE API
		This requires the TSG ID, client ID, and client secret.
		"""
		__myToken = {}
		__auth_url = "https://auth.apps.paloaltonetworks.com/oauth2/access_token"
		__auth_headers = {'Content-Type': 'application/x-www-form-urlencoded',}
		__auth_data = 'grant_type=client_credentials&scope=tsg_id:' + TSG_ID
		__auth_info = (CLIENT_ID, CLIENT_SECRET)
		__response = requests.post(url=__auth_url, headers=__auth_headers, data=__auth_data, auth=__auth_info)
		
		if __response.status_code == 200:
			__response = __response.json()
			__myToken["access_token"] = __response["access_token"]
			__myToken["expires_on"] = datetime.now() + timedelta(seconds=int(__response["expires_in"]))
			self.saseToken["bearerToken"] = __response["access_token"]
			self.saseToken["expiresOn"] = __myToken["expires_on"]
		else:
			print("Failed to generate auth token")

	def initClassVariables(self):
		"""Initialize class variables"""
		self.saseTsgId = None
		self.saseClientId = None
		self.clientSecret = None
		self.saseToken = {
			"bearerToken": "",
			"expiresOn": None
		}
		
	def __init__(self):
		"""Initialize the authentication module"""
		self.initClassVariables()