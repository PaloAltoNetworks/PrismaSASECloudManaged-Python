from datetime import datetime
from . import saseApi

class policyObjects:
	"""Policy Objects Class"""
	def checkTokenStillValid(self):
		"""
		Checks to see if the token is still valid. 
		Returns true is still in 15minute window. 
		Returns false if not.
		"""
		rightNow = datetime.now()
		tokenValid = bool(rightNow < self.prismaAccessObject.saseToken['expiresOn'])
		return tokenValid

	def paAddressesListAddresses(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paAddresses = saseApi.saseApi(self.prismaAccessObject.addressesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAddresses.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAddressesCreate(self, __addressObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paAddresses = saseApi.saseApi(self.prismaAccessObject.addressesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAddresses.paCreate(__addressObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAddressesEdit(self, __addressObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paAddresses = saseApi.saseApi(self.prismaAccessObject.addressesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAddresses.paEdit(__addressObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAddressesDelete(self, __addressObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paAddresses = saseApi.saseApi(self.prismaAccessObject.addressesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAddresses.paDelete(__addressObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paTagsListTags(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paTag = saseApi.saseApi(self.prismaAccessObject.tagsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paTag.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paTagCreate(self, __tagObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paTag = saseApi.saseApi(self.prismaAccessObject.tagsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paTag.paCreate(__tagObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paTagEdit(self, __tagObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paTag = saseApi.saseApi(self.prismaAccessObject.tagsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paTag.paEdit(__tagObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paTagDelete(self, __tagObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paTag = saseApi.saseApi(self.prismaAccessObject.tagsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paTag.paDelete(__tagObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paLicenseTypesListTypes(self):
		if self.checkTokenStillValid():
			paLicenses = saseApi.saseApi(self.prismaAccessObject.licenseTypesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paLicenses.paList()
		else:
			print("Please request new token and create new prismaAccess object.")

	def paLocationsListLocations(self):
		"""List all the Prisma Access Locations"""
		if self.checkTokenStillValid():
			paLocations = saseApi.saseApi(self.prismaAccessObject.locationsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paLocations.paList()
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAddressGroupsListAddressGroups(self, __folder="Shared"):
		"""List all the address groups."""
		if self.checkTokenStillValid():
			paAddressGroup = saseApi.saseApi(self.prismaAccessObject.addressGroupsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAddressGroup.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAddressGroupsCreate(self, __addressGroupObject, __folder="Shared"):
		"""Create an address group object"""
		if self.checkTokenStillValid():
			paAddressGroup = saseApi.saseApi(self.prismaAccessObject.addressGroupsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAddressGroup.paCreate(__addressGroupObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAddressGroupsEdit(self, __addressGroupObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paAddressGroup = saseApi.saseApi(self.prismaAccessObject.addressGroupsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAddressGroup.paEdit(__addressGroupObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAddressGroupsDelete(self, __addressGroupObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paAddressGroup = saseApi.saseApi(self.prismaAccessObject.addressGroupsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAddressGroup.paDelete(__addressGroupObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paServicesListServices(self, __folder="Shared"):
		"""List all Service Objects that are defined."""
		if self.checkTokenStillValid():
			paServices = saseApi.saseApi(self.prismaAccessObject.servicesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paServices.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paServicesCreateService(self, __servicesObject, __folder="Shared"):
		"""Create an address group object"""
		if self.checkTokenStillValid():
			paServices = saseApi.saseApi(self.prismaAccessObject.servicesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paServices.paCreate(__servicesObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paServicesEditService(self, __servicesObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paServices = saseApi.saseApi(self.prismaAccessObject.servicesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paServices.paEdit(__servicesObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paServicesDeleteService(self, __servicesObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paServices = saseApi.saseApi(self.prismaAccessObject.servicesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paServices.paDelete(__servicesObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def __init__(self, __prismaAccessObject):
		"""Policy Objects class"""
		self.prismaAccessObject = __prismaAccessObject
