# Prisma SASE Cloud Managed API
Python framework to make changes to Prisma Access Cloud Managed
Current working version - _0.04_

* Authors - [TheScriptGuy](https://github.com/TheScriptGuy)


See [CHANGELOG.md](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/CHANGELOG.md) for updates.

# Prisma Access
## Supported Features 
### policyObjects
| Feature | List | Create | Edit | Delete |
| ------- | ---- | ------ | ---- | ------ |
| Tags | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Address Objects | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Address Group Objects | :white_check_mark: | :white_check_mark: | :x: | :x: |

### Service Setup
| Feature | List | Create | Edit | Delete |
| ------- | ---- | ------ | ---- | ------ |
| Service Connections | :white_check_mark: | :x: | :x: | :x: |
| IKE Crypto Profiles | :white_check_mark: | :x: | :x: | :x: |
| IKE Gateways for Service Connections | :white_check_mark: | :x: | :x: | :x: | 
| IPSec Tunnels for Service Connections | :white_check_mark: | :x: | :x: | :x: |
| License Types | :white_check_mark: | n/a | n/a | n/a |
| Prisma Access Locations | :white_check_mark: | n/a | n/a | n/a |


# SDWAN
Not supported (yet)

# Examples for usage
How to use the API

[Setup API Access in TSG](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/usage-identity-access.md)

[Python Script Usage](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/usage-python.md)