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

	def paApplicationFiltersListApplicationFilters(self, __folder="Shared"):
		"""List all Application Filters that are defined."""
		if self.checkTokenStillValid():
			paApplicationFilters = saseApi.saseApi(self.prismaAccessObject.applicationFiltersUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paApplicationFilters.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paApplicationFiltersCreate(self, __ApplicationFiltersObject, __folder="Shared"):
		"""Create an Application Filter object"""
		if self.checkTokenStillValid():
			paApplicationFilters = saseApi.saseApi(self.prismaAccessObject.applicationFiltersUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paApplicationFilters.paCreate(__ApplicationFiltersObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paApplicationFiltersEdit(self, __ApplicationFiltersObject, __folder="Shared"):
		"""Edit an Application Filter object"""
		if self.checkTokenStillValid():
			paApplicationFilters = saseApi.saseApi(self.prismaAccessObject.applicationFiltersUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paApplicationFilters.paEdit(__ApplicationFiltersObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paApplicationFiltersDelete(self, __ApplicationFiltersObject, __folder="Shared"):
		"""Delete an Application Filter object"""
		if self.checkTokenStillValid():
			paApplicationFilters = saseApi.saseApi(self.prismaAccessObject.applicationFiltersUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paApplicationFilters.paDelete(__ApplicationFiltersObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paApplicationGroupsListApplicationGroups(self, __folder="Shared"):
		"""List all Application Groups that are defined."""
		if self.checkTokenStillValid():
			paApplicationGroups = saseApi.saseApi(self.prismaAccessObject.applicationGroupsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paApplicationGroups.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paApplicationGroupsCreate(self, __ApplicationGroupsObject, __folder="Shared"):
		"""Create an Application Groups object"""
		if self.checkTokenStillValid():
			paApplicationGroups = saseApi.saseApi(self.prismaAccessObject.applicationGroupsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paApplicationGroups.paCreate(__ApplicationGroupsObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paApplicationGroupsEdit(self, __ApplicationGroupsObject, __folder="Shared"):
		"""Edit an Application Groups object"""
		if self.checkTokenStillValid():
			paApplicationGroups = saseApi.saseApi(self.prismaAccessObject.applicationGroupsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paApplicationGroups.paEdit(__ApplicationGroupsObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paApplicationGroupsDelete(self, __ApplicationGroupsObject, __folder="Shared"):
		"""Delete an Application Groups object"""
		if self.checkTokenStillValid():
			paApplicationGroups = saseApi.saseApi(self.prismaAccessObject.applicationGroupsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paApplicationGroups.paDelete(__ApplicationGroupsObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paApplicationsListApplications(self, __folder="Shared"):
		"""List all Applications that are defined."""
		if self.checkTokenStillValid():
			paApplications = saseApi.saseApi(self.prismaAccessObject.applicationsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paApplications.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paApplicationsCreate(self, __ApplicationsObject, __folder="Shared"):
		"""Create an Applications object"""
		if self.checkTokenStillValid():
			paApplications = saseApi.saseApi(self.prismaAccessObject.applicationsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paApplications.paCreate(__ApplicationsObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paApplicationsEdit(self, __ApplicationsObject, __folder="Shared"):
		"""Edit an Applications object"""
		if self.checkTokenStillValid():
			paApplications = saseApi.saseApi(self.prismaAccessObject.applicationsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paApplications.paEdit(__ApplicationsObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paApplicationsDelete(self, __ApplicationsObject, __folder="Shared"):
		"""Delete an Applications object"""
		if self.checkTokenStillValid():
			paApplications = saseApi.saseApi(self.prismaAccessObject.applicationsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paApplications.paDelete(__ApplicationsObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paSchedulesListSchedules(self, __folder="Shared"):
		"""List all Schedules that are defined."""
		if self.checkTokenStillValid():
			paSchedules = saseApi.saseApi(self.prismaAccessObject.schedulesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paSchedules.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paSchedulesCreate(self, __SchedulesObject, __folder="Shared"):
		"""Create an Schedules object"""
		if self.checkTokenStillValid():
			paSchedules = saseApi.saseApi(self.prismaAccessObject.schedulesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paSchedules.paCreate(__SchedulesObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paSchedulesEdit(self, __SchedulesObject, __folder="Shared"):
		"""Edit an Schedules object"""
		if self.checkTokenStillValid():
			paSchedules = saseApi.saseApi(self.prismaAccessObject.schedulesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paSchedules.paEdit(__SchedulesObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paSchedulesDelete(self, __SchedulesObject, __folder="Shared"):
		"""Delete an Schedules object"""
		if self.checkTokenStillValid():
			paSchedules = saseApi.saseApi(self.prismaAccessObject.schedulesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paSchedules.paDelete(__SchedulesObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def __init__(self, __prismaAccessObject):
		"""Policy Objects class"""
		self.prismaAccessObject = __prismaAccessObject
