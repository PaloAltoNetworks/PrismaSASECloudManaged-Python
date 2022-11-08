class prismaAccess:
	"""
	Prisma Access class that is used for getting/making changes to Prisma Access Cloud Managed.
	"""
	def initApiUri(self):
		"""Initialize all the Prisma Access API's."""
		__configV1 = "/sse/config/v1/"

		# As support for each element becomes available, uncomment appropriate uri line.

		# Certificate Management
		#self.certificateProfilesUri = self.saseApi + __configV1 + "certificate-profiles"
		#self.certificatesUri = self.saseApi + __configV1 + "certificates"
		#self.ocspResponderUri = self.saseApi + __configV1 + "ocsp-responder"
		#self.scepProfilesUri = self.saseApi + __configV1 + "scep-profiles"
		#self.tlsServiceProfilesUri = self.saseApi + __configV1 + "tls-service-profiles"
		#self.trustedCertificateAuthoritiesUri = self.saseApi + __configV1 + "trusted-certificate-authorities"

		# Configuration Management
		#self.configurationManagementUri = self.saseApi + __configV1 + "config-versions"

		# Identity Services
		#self.authenticationPortalsUri = self.saseApi + __configV1 + "authentication-portals"
		#self.authenticationProfilesUri = self.saseApi + __configV1 + "authentication-profiles"
		#self.authenticationRulesUri = self.saseApi + __configV1 + "authentication-rules"
		#self.authenticationSequencesUri = self.saseApi + __configV1 + "authentication-sequences"
		#self.kerberosServerProfilesUri = self.saseApi + __configV1 + "kerberos-server-profiles"
		#self.ldapServerProfilesUri = self.saseApi + __configV1 + "ldap-server-profiles"
		#self.localUsersUri = self.saseApi + __configV1 + "local-users"
		#self.mfaServersUri = self.saseApi + __configV1 + "mfa-servers"
		#self.radiusServerProfilesUri = self.saseApi + __configV1 + "radius-server-profiles"
		#self.samlServerProfilesUri = self.saseApi + __configV1 + "saml-server-profiles"
		#self.tacacsServerProfilesUri = self.saseApi + __configV1 + "tacacs-server-profiles"

		# Policy Objects
		self.addressGroupsUri = self.saseApi + __configV1 + "address-groups"
		self.addressesUri = self.saseApi + __configV1 + "addresses"
		#self.applicationFiltersUri = self.saseApi + __configV1 + "application-filters"
		#self.applicationGroupsUri = self.saseApi + __configV1 + "application-groups"
		#self.applicationOverrideRulesUri = self.saseApi + __configV1 + "app-override-rules"
		#self.applicationsUri = self.saseApi + __configV1 + "applications"
		#self.autoTagActionsUri = self.saseApi + __configV1 + "auto-tag-actions"
		#self.dynamicUserGroupsUri = self.saseApi + __configV1 + "dynamic-user-groups"
		#self.externalDynamicListsUri = self.saseApi + __configV1 + "external-dynamic-lists"
		#self.hipObjectsUri = self.saseApi + __configV1 + "hip-objects"
		#self.hipProfilesUri = self.saseApi + __configV1 + "hip-profiles"
		#self.quarantinedDevicesUri = self.saseApi + __configV1 + "quarantined-devices"
		#self.regionsUri = self.saseApi + __configV1 + "regions"
		#self.schedulesUri = self.saseApi + __configV1 + "schedules"
		#self.serviceGroupsUri = self.saseApi + __configV1 + "service-groups"
		#self.servicesUri = self.saseApi + __configV1 + "services"
		self.tagsUri = self.saseApi + __configV1 + "tags"
		#self.urlCategoriesUri = self.saseApi + __configV1 + "url-categories"
		#self.urlFilteringCategoriesUri = self.saseApi + __configV1 + "url-filtering-categories"

		# Service Setup
		#self.bandwidthAllocationsUri = self.saseApi + __configV1 + "bandwidth-allocations"
		self.ikeCryptoProfilesUri = self.saseApi + __configV1 + "ike-crypto-profiles"
		self.ikeGatewaysUri = self.saseApi + __configV1 + "ike-gateways"
		self.ipsecCryptoProfilesUri = self.saseApi + __configV1 + "ipsec-crypto-profiles"
		self.ipsecTunnelsUri = self.saseApi + __configV1 + "ipsec-tunnels"
		#self.infrastructureSettingsUri = self.saseApi + __configV1 + "shared-infrastructure-settings"
		#self.internalDnsServersUri = self.saseApi + __configV1 + "internal-dns-servers"
		self.licenseTypesUri = self.saseApi + __configV1 + "license-types"
		self.locationsUri = self.saseApi + __configV1 + "locations"
		#self.qosPolicyRulesUri = self.saseApi + __configV1 + "qos-policy-rules"
		#self.qosProfilesUri = self.saseApi + __configV1 + "qos-profiles"
		self.remoteNetworksUri = self.saseApi + __configV1 + "remote-networks"
		self.serviceConnectionsUri = self.saseApi + __configV1 + "service-connections"
		#self.trafficSteeringUri = self.saseApi + __configV1 + "traffic-steering"

		# Security Services
		#self.antiSpywareProfilesUri = self.saseApi + __configV1 + "anti-spyware-profiles"
		#self.antiSpywareSignaturesUri = self.saseApi + __configV1 + "anti-spyware-signatures"
		#self.dnsSecurityProfilesUri = self.saseApi + __configV1 + "dns-security-profiles"
		#self.decryptionExclusionsUri = self.saseApi + __configV1 + "decryption-exclusions"
		#self.decryptionProfilesUri = self.saseApi + __configV1 + "decryption-profiles"
		#self.decryptionRulesUri = self.saseApi + __configV1 + "decryption-rules"
		#self.fileBlockingProfilesUri = self.saseApi + __configV1 + "file-blocking-profiles"
		#self.httpHeaderProfilesUri = self.saseApi + __configV1 + "http-header-profiles"
		#self.profileGroupsUri = self.saseApi + __configV1 + "profile-groups"
		#self.securityRulesUri = self.saseApi + __configV1 + "security-rules"
		#self.urlAccessProfilesUri = self.saseApi + __configV1 + "url-access-profiles"
		#self.vulnerabilityProtectProfilesUri = self.saseApi + __configV1 + "vulnerability-protection-profiles"
		#self.vulnerabilityProtectSignaturesUri = self.saseApi + __configV1 + "vulnerability-protection-signatures"
		#self.wildfireAntiVirusProfilesUri = self.saseApi + __configV1 + "wildfire-anti-virus-profiles"

	def __init__(self, __saseToken):
		"""Initialize Class"""
		self.prismaAccessPythonAPIVersion = "0.10"
		self.saseApi = "https://api.sase.paloaltonetworks.com"
		self.saseToken = __saseToken
		self.contentType = "application/json"
		self.saseAuthHeaders = { 
			"Authorization": f"Bearer {self.saseToken['bearerToken']}",
			"Content-Type": f"{self.contentType}"
		}

		# Set all API URI variables
		self.initApiUri()