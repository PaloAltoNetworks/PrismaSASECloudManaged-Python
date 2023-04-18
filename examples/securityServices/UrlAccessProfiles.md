# Examples on how to work with Url Access Profiles
In all examples, it will either return a success or failure when attempting the operation.

## Authentication
First authenticate to the API service:
```python
from auth import saseAuthentication
from access import prismaAccess
from access import securityServices

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()
n = prismaAccess.prismaAccess(p.saseToken)
```

Now we can proceed with the commands below.

## List all Url Access Profiles
To list all Url Access Profiles within shared folder (it defaults to _Shared_ folder)
```python
s = securityServices.securityServices(n)

s.paUrlAccessProfilesList()
```


To list all Url Access Profiles within a specific folder, e.g. _Shared_ (it defaults to _Shared_).
```python
s = securityServices.securityServices(n)

s.paUrlAccessProfilesList("Shared")
```


## Create a Url Access Profile
To create a Url Access Profile in the _Remote Networks_ folder (it defaults to _Shared_).

```python
s = securityServices.securityServices(n)

urlAccessProfiles = {"name":"best-practice2","folder":"Shared","local_inline_cat":True,"credential_enforcement":{"mode":{"ip_user":{}},"log_severity":"medium","alert":["abortion","alcohol-and-tobacco","auctions","business-and-economy","computer-and-internet-info","content-delivery-networks","cryptocurrency","dating","educational-institutions","entertainment-and-arts","financial-services","games","government","health-and-medicine","high-risk","home-and-garden","hunting-and-fishing","internet-communications-and-telephony","internet-portals","job-search","legal","low-risk","medium-risk","military","motor-vehicles","music","news","not-resolved","nudity","online-storage-and-backup","personal-sites-and-blogs","philosophy-and-political-advocacy","private-ip-addresses","real-estate","recreation-and-hobbies","reference-and-research","religion","search-engines","sex-education","shareware-and-freeware","shopping","social-networking","society","sports","stock-advice-and-tools","streaming-media","swimsuits-and-intimate-apparel","training-and-tools","translation","travel","web-advertisements","web-based-email","web-hosting"],"block":["abused-drugs","adult","command-and-control","copyright-infringement","dynamic-dns","extremism","gambling","grayware","hacking","insufficient-content","malware","newly-registered-domain","parked","peer-to-peer","phishing","proxy-avoidance-and-anonymizers","ransomware","questionable","unknown","weapons"]},"alert":["abortion","alcohol-and-tobacco","auctions","business-and-economy","computer-and-internet-info","content-delivery-networks","cryptocurrency","dating","educational-institutions","entertainment-and-arts","financial-services","games","government","health-and-medicine","home-and-garden","hunting-and-fishing","internet-communications-and-telephony","internet-portals","job-search","legal","low-risk","medium-risk","military","motor-vehicles","music","news","not-resolved","nudity","online-storage-and-backup","personal-sites-and-blogs","philosophy-and-political-advocacy","private-ip-addresses","real-estate","recreation-and-hobbies","reference-and-research","religion","search-engines","sex-education","shareware-and-freeware","shopping","social-networking","society","sports","stock-advice-and-tools","streaming-media","swimsuits-and-intimate-apparel","training-and-tools","translation","travel","web-advertisements","web-based-email","web-hosting"],"block":["abused-drugs","adult","command-and-control","copyright-infringement","dynamic-dns","extremism","gambling","grayware","hacking","high-risk","insufficient-content","malware","newly-registered-domain","parked","peer-to-peer","phishing","proxy-avoidance-and-anonymizers","ransomware","questionable","unknown","weapons"]}
s.paUrlAccessProfilesCreate(urlAccessProfiles)
```

This will create a Url Access Profile in the _"Remote Networks"_ folder.

```python
s = securityServices.securityServices(n)

urlAccessProfiles = {"name":"best-practice2","folder":"Shared","local_inline_cat":True,"credential_enforcement":{"mode":{"ip_user":{}},"log_severity":"medium","alert":["abortion","alcohol-and-tobacco","auctions","business-and-economy","computer-and-internet-info","content-delivery-networks","cryptocurrency","dating","educational-institutions","entertainment-and-arts","financial-services","games","government","health-and-medicine","high-risk","home-and-garden","hunting-and-fishing","internet-communications-and-telephony","internet-portals","job-search","legal","low-risk","medium-risk","military","motor-vehicles","music","news","not-resolved","nudity","online-storage-and-backup","personal-sites-and-blogs","philosophy-and-political-advocacy","private-ip-addresses","real-estate","recreation-and-hobbies","reference-and-research","religion","search-engines","sex-education","shareware-and-freeware","shopping","social-networking","society","sports","stock-advice-and-tools","streaming-media","swimsuits-and-intimate-apparel","training-and-tools","translation","travel","web-advertisements","web-based-email","web-hosting"],"block":["abused-drugs","adult","command-and-control","copyright-infringement","dynamic-dns","extremism","gambling","grayware","hacking","insufficient-content","malware","newly-registered-domain","parked","peer-to-peer","phishing","proxy-avoidance-and-anonymizers","ransomware","questionable","unknown","weapons"]},"alert":["abortion","alcohol-and-tobacco","auctions","business-and-economy","computer-and-internet-info","content-delivery-networks","cryptocurrency","dating","educational-institutions","entertainment-and-arts","financial-services","games","government","health-and-medicine","home-and-garden","hunting-and-fishing","internet-communications-and-telephony","internet-portals","job-search","legal","low-risk","medium-risk","military","motor-vehicles","music","news","not-resolved","nudity","online-storage-and-backup","personal-sites-and-blogs","philosophy-and-political-advocacy","private-ip-addresses","real-estate","recreation-and-hobbies","reference-and-research","religion","search-engines","sex-education","shareware-and-freeware","shopping","social-networking","society","sports","stock-advice-and-tools","streaming-media","swimsuits-and-intimate-apparel","training-and-tools","translation","travel","web-advertisements","web-based-email","web-hosting"],"block":["abused-drugs","adult","command-and-control","copyright-infringement","dynamic-dns","extremism","gambling","grayware","hacking","high-risk","insufficient-content","malware","newly-registered-domain","parked","peer-to-peer","phishing","proxy-avoidance-and-anonymizers","ransomware","questionable","unknown","weapons"]}
s.paUrlAccessProfilesCreate(urlAccessProfiles, "Remote Networks")
```

## Edit a Url Access Profile
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing Url Access Profile in the _Remote Networks_ folder. 

This will edit an existing Url Access Profile named _Sample Policy_.

```python
s = securityServices.securityServices(n)

urlAccessProfiles = {"name":"best-practice2","folder":"Shared","local_inline_cat":True,"credential_enforcement":{"mode":{"ip_user":{}},"log_severity":"medium","alert":["abortion","alcohol-and-tobacco","auctions","business-and-economy","computer-and-internet-info","content-delivery-networks","cryptocurrency","dating","educational-institutions","entertainment-and-arts","financial-services","games","government","health-and-medicine","high-risk","home-and-garden","hunting-and-fishing","internet-communications-and-telephony","internet-portals","job-search","legal","low-risk","medium-risk","military","motor-vehicles","music","news","not-resolved","nudity","online-storage-and-backup","personal-sites-and-blogs","philosophy-and-political-advocacy","private-ip-addresses","real-estate","recreation-and-hobbies","reference-and-research","religion","search-engines","sex-education","shareware-and-freeware","shopping","social-networking","society","sports","stock-advice-and-tools","streaming-media","swimsuits-and-intimate-apparel","training-and-tools","translation","travel","web-advertisements","web-based-email","web-hosting"],"block":["abused-drugs","adult","command-and-control","copyright-infringement","dynamic-dns","extremism","gambling","grayware","hacking","insufficient-content","malware","newly-registered-domain","parked","peer-to-peer","phishing","proxy-avoidance-and-anonymizers","ransomware","questionable","unknown","weapons"]},"alert":["abortion","alcohol-and-tobacco","auctions","business-and-economy","computer-and-internet-info","content-delivery-networks","cryptocurrency","dating","educational-institutions","entertainment-and-arts","financial-services","games","government","health-and-medicine","home-and-garden","hunting-and-fishing","internet-communications-and-telephony","internet-portals","job-search","legal","low-risk","medium-risk","military","motor-vehicles","music","news","not-resolved","nudity","online-storage-and-backup","personal-sites-and-blogs","philosophy-and-political-advocacy","private-ip-addresses","real-estate","recreation-and-hobbies","reference-and-research","religion","search-engines","sex-education","shareware-and-freeware","shopping","social-networking","society","sports","stock-advice-and-tools","streaming-media","swimsuits-and-intimate-apparel","training-and-tools","translation","travel","web-advertisements","web-based-email","web-hosting"],"block":["abused-drugs","adult","command-and-control","copyright-infringement","dynamic-dns","extremism","gambling","grayware","hacking","high-risk","insufficient-content","malware","newly-registered-domain","parked","peer-to-peer","phishing","proxy-avoidance-and-anonymizers","ransomware","questionable","unknown","weapons"]}
s.paUrlAccessProfilesEdit(urlAccessProfiles, "Remote Networks")
```

## Delete a Url Access Profile
To delete a Url Access Profile in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
s = securityServices.securityServices(n)

urlAccessProfiles = { "name": "best-practice2" }
s.paUrlAccessProfilesDelete(urlAccessProfiles, "Remote Networks")
```