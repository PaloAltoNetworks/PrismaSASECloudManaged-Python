from datetime import datetime
from . import saseApi

class securityServices:
	"""securityServices class"""

	def checkTokenStillValid(self):
		"""
		Checks to see if the token is still valid. 
		Returns true is still in 15minute window. 
		Returns false if not.
		"""
		rightNow = datetime.now()
		tokenValid = bool(rightNow < self.prismaAccessObject.saseToken['expiresOn'])
		return tokenValid

	def paSecurityRulesList(self, __folder="Shared", __position="pre"):
		"""List all security rules that are defined."""
		if self.checkTokenStillValid():
			paSecurityRules = saseApi.saseApi(self.prismaAccessObject.securityRulesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paSecurityRules.paList(__folder, __position, includePosition=True)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paSecurityRulesCreate(self, __securityRuleObject, __folder="Shared", __position="pre"):
		if self.checkTokenStillValid():
			paSecurityRules = saseApi.saseApi(self.prismaAccessObject.securityRulesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paSecurityRules.paCreate(__securityRuleObject, __folder, __position, includePosition=True)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paSecurityRulesEdit(self, __securityRuleObject, __folder="Shared", __position="pre"):
		if self.checkTokenStillValid():
			paSecurityRules = saseApi.saseApi(self.prismaAccessObject.securityRulesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paSecurityRules.paEdit(__securityRuleObject, __folder, __position, includePosition=True)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paSecurityRulesDelete(self, __securityRuleObject, __folder="Shared", __position="pre"):
		if self.checkTokenStillValid():
			paSecurityRules = saseApi.saseApi(self.prismaAccessObject.securityRulesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paSecurityRules.paDelete(__securityRuleObject, __folder, __position, includePosition=True)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAntiSpywareProfilesList(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paAntiSpywareProfiles = saseApi.saseApi(self.prismaAccessObject.antiSpywareProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAntiSpywareProfiles.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAntiSpywareProfilesCreate(self, __antiSpywareProfilesObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paAntiSpywareProfiles = saseApi.saseApi(self.prismaAccessObject.antiSpywareProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAntiSpywareProfiles.paCreate(__antiSpywareProfilesObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAntiSpywareProfilesEdit(self, __antiSpywareProfilesObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paAntiSpywareProfiles = saseApi.saseApi(self.prismaAccessObject.antiSpywareProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAntiSpywareProfiles.paEdit(__antiSpywareProfilesObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAntiSpywareProfilesDelete(self, __antiSpywareProfilesObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paAntiSpywareProfiles = saseApi.saseApi(self.prismaAccessObject.antiSpywareProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAntiSpywareProfiles.paDelete(__antiSpywareProfilesObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAntiSpywareSignaturesList(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paAntiSpywareSignatures = saseApi.saseApi(self.prismaAccessObject.antiSpywareSignaturesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAntiSpywareSignatures.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAntiSpywareSignaturesCreate(self, __antiSpywareSignaturesObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paAntiSpywareSignatures = saseApi.saseApi(self.prismaAccessObject.antiSpywareSignaturesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAntiSpywareSignatures.paCreate(__antiSpywareSignaturesObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAntiSpywareSignaturesEdit(self, __antiSpywareSignaturesObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paAntiSpywareSignatures = saseApi.saseApi(self.prismaAccessObject.antiSpywareSignaturesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAntiSpywareSignatures.paEdit(__antiSpywareSignaturesObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paAntiSpywareSignaturesDelete(self, __antiSpywareSignaturesObject, __folder="Shared"):
		if self.checkTokenStillValid():
			paAntiSpywareSignatures = saseApi.saseApi(self.prismaAccessObject.antiSpywareSignaturesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paAntiSpywareSignatures.paDelete(__antiSpywareSignaturesObject, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDnsSecurityProfilesList(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paDnsSecurityProfiles = saseApi.saseApi(self.prismaAccessObject.dnsSecurityProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDnsSecurityProfiles.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDnsSecurityProfilesCreate(self, __dnsSecurityProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paDnsSecurityProfiles = saseApi.saseApi(self.prismaAccessObject.dnsSecurityProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDnsSecurityProfiles.paCreate(__dnsSecurityProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDnsSecurityProfilesEdit(self, __dnsSecurityProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paDnsSecurityProfiles = saseApi.saseApi(self.prismaAccessObject.dnsSecurityProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDnsSecurityProfiles.paEdit(__dnsSecurityProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDnsSecurityProfilesDelete(self, __dnsSecurityProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paDnsSecurityProfiles = saseApi.saseApi(self.prismaAccessObject.dnsSecurityProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDnsSecurityProfiles.paDelete(__dnsSecurityProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDecryptionExclusionsList(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paDecryptionExclusions = saseApi.saseApi(self.prismaAccessObject.decryptionExclusionsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDecryptionExclusions.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDecryptionExclusionsCreate(self, __decryptionExclusions, __folder="Shared"):
		if self.checkTokenStillValid():
			paDecryptionExclusions = saseApi.saseApi(self.prismaAccessObject.decryptionExclusionsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDecryptionExclusions.paCreate(__decryptionExclusions, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDecryptionExclusionsEdit(self, __decryptionExclusions, __folder="Shared"):
		if self.checkTokenStillValid():
			paDecryptionExclusions = saseApi.saseApi(self.prismaAccessObject.decryptionExclusionsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDecryptionExclusions.paEdit(__decryptionExclusions, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDecryptionExclusionsDelete(self, __decryptionExclusions, __folder="Shared"):
		if self.checkTokenStillValid():
			paDecryptionExclusions = saseApi.saseApi(self.prismaAccessObject.decryptionExclusionsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDecryptionExclusions.paDelete(__decryptionExclusions, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDecryptionProfilesList(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paDecryptionProfiles = saseApi.saseApi(self.prismaAccessObject.decryptionProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDecryptionProfiles.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDecryptionProfilesCreate(self, __decryptionProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paDecryptionProfiles = saseApi.saseApi(self.prismaAccessObject.decryptionProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDecryptionProfiles.paCreate(__decryptionProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDecryptionProfilesEdit(self, __decryptionProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paDecryptionProfiles = saseApi.saseApi(self.prismaAccessObject.decryptionProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDecryptionProfiles.paEdit(__decryptionProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDecryptionProfilesDelete(self, __decryptionProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paDecryptionProfiles = saseApi.saseApi(self.prismaAccessObject.decryptionProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDecryptionProfiles.paDelete(__decryptionProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDecryptionRulesList(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paDecryptionRules = saseApi.saseApi(self.prismaAccessObject.decryptionRulesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDecryptionRules.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDecryptionRulesCreate(self, __decryptionRules, __folder="Shared"):
		if self.checkTokenStillValid():
			paDecryptionRules = saseApi.saseApi(self.prismaAccessObject.decryptionRulesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDecryptionRules.paCreate(__decryptionRules, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDecryptionRulesEdit(self, __decryptionRules, __folder="Shared"):
		if self.checkTokenStillValid():
			paDecryptionRules = saseApi.saseApi(self.prismaAccessObject.decryptionRulesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDecryptionRules.paEdit(__decryptionRules, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paDecryptionRulesDelete(self, __decryptionRules, __folder="Shared"):
		if self.checkTokenStillValid():
			paDecryptionRules = saseApi.saseApi(self.prismaAccessObject.decryptionRulesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paDecryptionRules.paDelete(__decryptionRules, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paFileBlockingProfilesList(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paFileBlockingProfiles = saseApi.saseApi(self.prismaAccessObject.fileBlockingProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paFileBlockingProfiles.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paFileBlockingProfilesCreate(self, __fileBlockingProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paFileBlockingProfiles = saseApi.saseApi(self.prismaAccessObject.fileBlockingProfilesUri, self.prismaAccessObjectsaseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paFileBlockingProfiles.paCreate(__fileBlockingProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paFileBlockingProfilesEdit(self, __fileBlockingProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paFileBlockingProfiles = saseApi.saseApi(self.prismaAccessObject.fileBlockingProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paFileBlockingProfiles.paEdit(__fileBlockingProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paFileBlockingProfilesDelete(self, __fileBlockingProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paFileBlockingProfiles = saseApi.saseApi(self.prismaAccessObject.fileBlockingProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paFileBlockingProfiles.paDelete(__fileBlockingProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paHttpHeaderProfilesList(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paHttpHeaderProfiles = saseApi.saseApi(self.prismaAccessObject.httpHeaderProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paHttpHeaderProfiles.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paHttpHeaderProfilesCreate(self, __httpHeaderProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paHttpHeaderProfiles = saseApi.saseApi(self.prismaAccessObject.httpHeaderProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paHttpHeaderProfiles.paCreate(__httpHeaderProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paHttpHeaderProfilesEdit(self, __httpHeaderProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paHttpHeaderProfiles = saseApi.saseApi(self.prismaAccessObject.httpHeaderProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paHttpHeaderProfiles.paEdit(__httpHeaderProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paHttpHeaderProfilesDelete(self, __httpHeaderProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paHttpHeaderProfiles = saseApi.saseApi(self.prismaAccessObject.httpHeaderProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paHttpHeaderProfiles.paDelete(__httpHeaderProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paProfileGroupsList(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paProfileGroups = saseApi.saseApi(self.prismaAccessObject.profileGroupsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paProfileGroups.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paProfileGroupsCreate(self, __profileGroups, __folder="Shared"):
		if self.checkTokenStillValid():
			paProfileGroups = saseApi.saseApi(self.prismaAccessObject.profileGroupsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paProfileGroups.paCreate(__profileGroups, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paProfileGroupsEdit(self, __profileGroups, __folder="Shared"):
		if self.checkTokenStillValid():
			paProfileGroups = saseApi.saseApi(self.prismaAccessObject.profileGroupsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paProfileGroups.paEdit(__profileGroups, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paProfileGroupsDelete(self, __profileGroups, __folder="Shared"):
		if self.checkTokenStillValid():
			paProfileGroups = saseApi.saseApi(self.prismaAccessObject.profileGroupsUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paProfileGroups.paDelete(__profileGroups, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paUrlAccessProfilesList(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paUrlAccessProfiles = saseApi.saseApi(self.prismaAccessObject.urlAccessProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paUrlAccessProfiles.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paUrlAccessProfilesCreate(self, __urlAccessProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paUrlAccessProfiles = saseApi.saseApi(self.prismaAccessObject.urlAccessProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paUrlAccessProfiles.paCreate(__urlAccessProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paUrlAccessProfilesEdit(self, __urlAccessProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paUrlAccessProfiles = saseApi.saseApi(self.prismaAccessObject.urlAccessProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paUrlAccessProfiles.paEdit(__urlAccessProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paUrlAccessProfilesDelete(self, __urlAccessProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paUrlAccessProfiles = saseApi.saseApi(self.prismaAccessObject.urlAccessProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paUrlAccessProfiles.paDelete(__urlAccessProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paVulnerabilityProtectProfilesList(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paVulnerabilityProtectProfiles = saseApi.saseApi(self.prismaAccessObject.vulnerabilityProtectProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paVulnerabilityProtectProfiles.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paVulnerabilityProtectProfilesCreate(self, __vulnerabilityProtectProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paVulnerabilityProtectProfiles = saseApi.saseApi(self.prismaAccessObject.vulnerabilityProtectProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paVulnerabilityProtectProfiles.paCreate(__vulnerabilityProtectProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paVulnerabilityProtectProfilesEdit(self, __vulnerabilityProtectProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paVulnerabilityProtectProfiles = saseApi.saseApi(self.prismaAccessObject.vulnerabilityProtectProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paVulnerabilityProtectProfiles.paEdit(__vulnerabilityProtectProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paVulnerabilityProtectProfilesDelete(self, __vulnerabilityProtectProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paVulnerabilityProtectProfiles = saseApi.saseApi(self.prismaAccessObject.vulnerabilityProtectProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paVulnerabilityProtectProfiles.paDelete(__vulnerabilityProtectProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paVulnerabilityProtectSignaturesList(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paVulnerabilityProtectSignatures = saseApi.saseApi(self.prismaAccessObject.vulnerabilityProtectSignaturesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paVulnerabilityProtectSignatures.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paVulnerabilityProtectSignaturesCreate(self, __vulnerabilityProtectSignatures, __folder="Shared"):
		if self.checkTokenStillValid():
			paVulnerabilityProtectSignatures = saseApi.saseApi(self.prismaAccessObject.vulnerabilityProtectSignaturesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paVulnerabilityProtectSignatures.paCreate(__vulnerabilityProtectSignatures, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paVulnerabilityProtectSignaturesEdit(self, __vulnerabilityProtectSignatures, __folder="Shared"):
		if self.checkTokenStillValid():
			paVulnerabilityProtectSignatures = saseApi.saseApi(self.prismaAccessObject.vulnerabilityProtectSignaturesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paVulnerabilityProtectSignatures.paEdit(__vulnerabilityProtectSignatures, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paVulnerabilityProtectSignaturesDelete(self, __vulnerabilityProtectSignatures, __folder="Shared"):
		if self.checkTokenStillValid():
			paVulnerabilityProtectSignatures = saseApi.saseApi(self.prismaAccessObject.vulnerabilityProtectSignaturesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paVulnerabilityProtectSignatures.paDelete(__vulnerabilityProtectSignatures, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paWildfireAntiVirusProfilesList(self, __folder="Shared"):
		if self.checkTokenStillValid():
			paWildfireAntiVirusProfiles = saseApi.saseApi(self.prismaAccessObject.wildfireAntiVirusProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paWildfireAntiVirusProfiles.paList(__folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paWildfireAntiVirusProfilesCreate(self, __wildfireAntiVirusProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paWildfireAntiVirusProfiles = saseApi.saseApi(self.prismaAccessObject.wildfireAntiVirusProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paWildfireAntiVirusProfiles.paCreate(__wildfireAntiVirusProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paWildfireAntiVirusProfilesEdit(self, __wildfireAntiVirusProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paWildfireAntiVirusProfiles = saseApi.saseApi(self.prismaAccessObject.wildfireAntiVirusProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paWildfireAntiVirusProfiles.paEdit(__wildfireAntiVirusProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def paWildfireAntiVirusProfilesDelete(self, __wildfireAntiVirusProfiles, __folder="Shared"):
		if self.checkTokenStillValid():
			paWildfireAntiVirusProfiles = saseApi.saseApi(self.prismaAccessObject.wildfireAntiVirusProfilesUri, self.prismaAccessObject.saseToken, self.prismaAccessObject.contentType, self.prismaAccessObject.saseAuthHeaders)
			paWildfireAntiVirusProfiles.paDelete(__wildfireAntiVirusProfiles, __folder)
		else:
			print("Please request new token and create new prismaAccess object.")

	def __init__(self, __prismaAccessObject):
		"""securityServices class initialization"""
		self.prismaAccessObject = __prismaAccessObject
