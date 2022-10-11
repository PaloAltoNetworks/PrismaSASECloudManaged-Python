import requests

class licenseTypes:
	"""licenseTypes Class"""

	def paLicenseTypesListTypes(self):
		"""This will list the license types"""
		__response = requests.get(url=self.saseLicenseUri, headers=self.saseAuthHeaders)
		__response = __response.json()

		print(__response)

	def __init__(self, __saseApi, __saseToken, __saseContentType, __saseAuthHeaders):
		"""licenseTypes Class Initilization"""
		self.saseApi = __saseApi
		self.saseToken = __saseToken
		self.saseContentType = __saseContentType
		self.saseAuthHeaders = __saseAuthHeaders
		self.saseLicenseUri = self.saseApi + "/sse/config/v1/license-types"

