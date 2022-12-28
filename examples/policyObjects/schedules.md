# Examples on how to work with schedules
In all examples, it will either return a success or failure when attempting the operation.

## Authentication
First authenticate to the API service:
```python
from auth import saseAuthentication
from access import prismaAccess

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()
n = prismaAccess.prismaAccess(p.saseToken)
```

Now we can proceed with the commands below.

## List all Schedules
To list all schedules within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)

o.paSchedulesListSchedules()
```


To list all schedules within a specific folder, e.g. _Remote Networks_
```python
o = policyObjects.policyObjects(n)

o.paSchedulesListSchedules("Remote Networks")
```


## Create an Schedules
To create an schedule in the _Shared_ folder (it defaults to _Shared_)

```python
o = policyObjects.policyObjects(n)

schedulesObject = {"name": "myTestSchedule1234", "schedule_type": {"recurring": {"daily": ["14:15-15:15"]}}}
o.paSchedulesCreate(schedulesObject)
```

This will create an schedule filter in the "Remote Networks" folder.

```python
o = policyObjects.policyObjects(n)

schedulesObject = { "name": "myTestApp12345", "category": "media", "subcategory": "audio-streaming", "technology": "client-server", "default": { "port": [ "tcp/80", "tcp/443" ] }, "risk": 1}
o.paSchedulesCreate(schedulesObject, "Remote Networks")
```

## Edit a Schedule Filter
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing schedule filter in the _Remote Networks_ folder. 

This will edit an existing schedule filter object named _myTestApplicationFilter2_.

```python
o = policyObjects.policyObjects(n)

schedulesObject = {"name": "myTestSchedule1234", "schedule_type": {"recurring": {"daily": ["11:15-15:15"]}}}
o.paSchedulesEdit(schedulesObject, "Remote Networks")
```

## Delete a Schedule
To delete a Schedule in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

schedulesObject = {"name": "myTestSchedule1234"}
o.paSchedulesDelete(schedulesObject)
```