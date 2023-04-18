# Examples on how to work with File Blocking Profiles
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

## List all File Blocking Profiles
To list all File Blocking Profiles within shared folder (it defaults to _Shared_ folder)
```python
s = securityServices.securityServices(n)

s.paFileBlockingProfilesList()
```


To list all File Blocking Profiles within a specific folder, e.g. _Shared_ (it defaults to _Shared_).
```python
s = securityServices.securityServices(n)

s.paFileBlockingProfilesList("Shared")
```


## Create a File Blocking Profile
To create a File Blocking Profile in the _Remote Networks_ folder (it defaults to _Shared_).

```python
s = securityServices.securityServices(n)

fileBlockingProfiles = {"name":"best-practice2","folder":"Shared","rules":[{"name":"Block all risky file types","application":["any"],"file_type":["7z","ace","arj","bas","bat","bzip2","cab","chm","class","cmd","com","cpl","deflate64-zip","dll","dmg","elf","encrypted-7z","encrypted-rar","encrypted-zip","exe","flash","gadget","hlp","hta","ico","inf","iso","jar","job","jse","lib","lnk","lzh","macapp","mach-o","microsoft-shell","mpkg","msc","msi","Multi-Level-Encoding","PE","pif","pkg","pl","powershell","prg","py","rar","reg","scf","scr","sh","shk","split-cab","split-rar","sys","tbz2","torrent","vb","vbe","vbs","vmdk","vxd","wsf","wsh"],"direction":"both","action":"block"},{"name":"Continue prompt encrypted files","application":["any"],"file_type":["encrypted-rar","encrypted-zip"],"direction":"both","action":"block"},{"name":"Log all other file types","application":["any"],"file_type":["any"],"direction":"both","action":"alert"}],"description":"Best practice file blocking security profile"}
s.paFileBlockingProfilesCreate(fileBlockingProfiles)
```

This will create a File Blocking Profile in the _"Remote Networks"_ folder.

```python
s = securityServices.securityServices(n)

fileBlockingProfiles = {"name":"best-practice2","folder":"Shared","rules":[{"name":"Block all risky file types","application":["any"],"file_type":["7z","ace","arj","bas","bat","bzip2","cab","chm","class","cmd","com","cpl","deflate64-zip","dll","dmg","elf","encrypted-7z","encrypted-rar","encrypted-zip","exe","flash","gadget","hlp","hta","ico","inf","iso","jar","job","jse","lib","lnk","lzh","macapp","mach-o","microsoft-shell","mpkg","msc","msi","Multi-Level-Encoding","PE","pif","pkg","pl","powershell","prg","py","rar","reg","scf","scr","sh","shk","split-cab","split-rar","sys","tbz2","torrent","vb","vbe","vbs","vmdk","vxd","wsf","wsh"],"direction":"both","action":"block"},{"name":"Continue prompt encrypted files","application":["any"],"file_type":["encrypted-rar","encrypted-zip"],"direction":"both","action":"block"},{"name":"Log all other file types","application":["any"],"file_type":["any"],"direction":"both","action":"alert"}],"description":"Best practice file blocking security profile"}
s.paFileBlockingProfilesCreate(fileBlockingProfiles, "Remote Networks")
```

## Edit a File Blocking Profile
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing File Blocking Profile in the _Remote Networks_ folder. 

This will edit an existing File Blocking Profile named _Sample Policy_.

```python
s = securityServices.securityServices(n)

fileBlockingProfiles = {"name":"best-practice2","folder":"Shared","rules":[{"name":"Block all risky file types","application":["any"],"file_type":["7z","ace","arj","bas","bat","bzip2","cab","chm","class","cmd","com","cpl","deflate64-zip","dll","dmg","elf","encrypted-7z","encrypted-rar","encrypted-zip","exe","flash","gadget","hlp","hta","ico","inf","iso","jar","job","jse","lib","lnk","lzh","macapp","mach-o","microsoft-shell","mpkg","msc","msi","Multi-Level-Encoding","PE","pif","pkg","pl","powershell","prg","py","rar","reg","scf","scr","sh","shk","split-cab","split-rar","sys","tbz2","torrent","vb","vbe","vbs","vmdk","vxd","wsf","wsh"],"direction":"both","action":"block"},{"name":"Continue prompt encrypted files","application":["any"],"file_type":["encrypted-rar","encrypted-zip"],"direction":"both","action":"block"},{"name":"Log all other file types","application":["any"],"file_type":["any"],"direction":"both","action":"alert"}],"description":"Best practice file blocking security profile"}
s.paFileBlockingProfilesEdit(fileBlockingProfiles, "Remote Networks")
```

## Delete a File Blocking Profile
To delete a File Blocking Profile in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
s = securityServices.securityServices(n)

fileBlockingProfiles = { "name": "best-practice2" }
s.paFileBlockingProfilesDelete(fileBlockingProfiles, "Remote Networks")
```