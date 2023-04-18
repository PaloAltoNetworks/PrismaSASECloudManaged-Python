# Changelog

## 2023/04/18 - Version 0.26
### Features Added
* Added Security Services
  * Security Rules - Delete, Edit, Create, List
  * Anti-Spyware Profiles - Delete, Edit, Create, List
  * Anti-Spyware Signatures - Delete, Edit, Create, List
  * Dns Security Profiles - Delete, Edit, Create, List
  * Decryption Exclusions - Delete, Edit, Create, List
  * Decryption Profiles - Delete, Edit, Create, List
  * Decryption Rules - Delete, Edit, Create, List
  * File-Blocking Profiles - Delete, Edit, Create, List
  * Http-Header Profiles - Delete, Edit, Create, List
  * Profile Groups - Delete, Edit, Create, List
  * Url Access Profiles - Delete, Edit, Create, List
  * Vulnerability Protect Profiles - Delete, Edit, Create, List
  * Vulnerability Protect Signatures - Delete, Edit, Create, List
  * Wildfire AntiVirus Profiles - Delete, Edit, Create, List
### Changes
* Add position arg to saseApi paList, paCreate, paEdit, paDelete to support Security Rules and Decryption Rules
* Update paList - a check for response type to return a list without further processing (For paLocationsListLocations which returns a list)
* Added name_key arg to paCreate, paEdit, paDelete to support Vuln & AntiSpam Signatures which have a different object name (threatname)


## 2023/01/26 - Version 0.25
* Added URL Filtering Categories - List. Please note that this is currently not working.

## 2023/01/26 - Version 0.24
* Added Dynamic User Groups - Delete, Edit, Create, List

## 2023/01/26 - Version 0.23
* Added URL Categories - Delete, Edit, Create, List

## 2022/12/28 - Version 0.22
* Added External Dynamic Lists - Delete, Edit, Create, List

## 2022/12/28 - Version 0.21
* Added HIP Profiles Objects - Delete, Edit, Create, List

## 2022/12/28 - Version 0.20
* Added HIP Objects - Delete, Edit, Create, List

## 2022/12/28 - Version 0.19
* Added Regions - Delete, Edit, Create, List
* Fixed documentation errors

## 2022/12/28 - Version 0.18
* Added Service Groups - Delete, Edit, Create, List
* Fixed documentation errors

## 2022/12/28 - Version 0.17
* Added schedules - Delete, Edit, Create, List
* Fixed documentation for Applications

## 2022/12/27 - Version 0.16
* Added Applications - Delete Edit, Create, List
* Fixed error with deleting/editing objects where the number of entries is greater than 200 (default limit size).

## 2022/12/27 - Version 0.15
* Added Application Groups - Delete, Edit, Create, List
* Fixed documentation errors for Application Filters

## 2022/12/27 - Version 0.14
* Added Application Filters - Delete, Edit, Create, List

## 2022/11/09 - Version 0.13
* Added IPSec Crypto Profiles - Delete, Edit, Create, List
* Updated examples for IKE Crypto Profiles to reflect new way to make changes

## 2022/11/08 - Version 0.12
* Added services objects - Delete, Edit, Create, List

## 2022/11/08 - Version 0.11
### Features Added
* Added Infrastructure Settings - List and Edit

## 2022/11/08 - Version 0.10
### Features Added
* Added capabilities for Delete, Edit, Create, List for Remote Networks

## 2022/11/03 - Version 0.09
### Features Added
* Added Delete, Edit, Create for IKE Gateways

## 2022/11/02 - Version 0.08
### Features Added
* Added support for Ipsec Tunnels

## 2022/11/02 - Version 0.07
### Features Added
* Added support for Service Connections

## 2022/10/21 - Version 0.06
### Changes
* rewrote all the modules to align with better coding practices.
* updated readme documents to reflect newer way of making changes.

## 2022/10/20 - Version 0.05
### Features Added
#### Service Setup
* IKE Crypto Profiles - Create, Edit, Delete

## 2022/10/14 - Version 0.04
### Features Added
#### Policy Objects
* Address Groups - Delete Edit

## 2022/10/12 - Version 0.04
### Feature Request
* include folder name HTTP responses - [feature request](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/issues/4)

## 2022/10/12 - Version 0.03
### Features Added
#### Policy Objects
* Address Objects - Delete, Edit

## 2022/10/11 - Version 0.02
### Features Added
#### Policy Objects
* Tags - Delete, Edit

### Documentation updated
* Added detailed usage examples for Tags

## 2022/10/09 - Version 0.01
First release!

### Features Added
#### Policy Objects
* Tags - List, Create
* Address Objects - List, Create
* Address Group Objects - List, Create

#### Service Setup
* Service Connections - List
* IKE Crypto Profiles - List
* IKE Gateways for Service Connections - List
* IPSec Tunnels for Service Connections - List
* License Types - List
* Prisma Access Locations - List
