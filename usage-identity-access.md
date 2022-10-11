# Setup API access

First thing is to setup access to your tenant in [TSG hub](sase.paloaltonetworks.com).
| Step | Screenshot |
| ---- | ---------- |
| 1. Select _Identity & Access / Access Management_.<br>2. Navigate to the appropriate TSG Tenant.<br>3. Click _Add_. | ![Identity Access](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/images/identity-access-add-new-identity.png) | 
| 4. Enter the account information that align with your company best practices. Ensure that you have a contact email and accurate description for the account being created. | ![Account Information](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/images/identity-access-add-service-account.png) | 
| 5. Save the _Client ID_ and _Client Secret_ in a secure location. | ![Client Credentials](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/images/identity-access-client-credentials.png) |
| 6. _(Optional)_ Assign appropriate _Roles_ to the account. In our example, we gave the account _Superuser_ access for  _Prisma Access_ in _Apps & Services_| ![Assign Roles](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/images/identity-access-assign-roles.png) | 