# python-keycloak-scripts

## Variables
**adminUser:** username of realm admin </br>
**adminPassword:** password of realm admin </br>
**clientId:** id of client </br>
**realm:** realm name </br>
**usersYamlFile:** path to yaml file with users, example - users-add.yaml or users-del.yaml </br>
**usersToCreateDefault/usersToDeleteDefault:** default var with users if yaml file does not exists. </br>
**requestedUserId**: id of user for token exchange


## Create users
#### Set required users to create in yaml file example ./users-add.yaml
Define a variable with the users you want to add </br>
Alternatively, specify these users in the yaml file </br>
whose name is defined in the usersYamlFile variable. </br>
Example of filling in a file:
```
---
- name: user1
  email: user1@local.ru
  password: user1Password
- name: user2
  email: user2@local.ru
  password: user2Password
- name: user3
  email: user3@local.ru
  password: user3Password
```
#### Command
```
docker run -it --rm --network host -v /dir-with-script/on-your-host:/scripts -w /scripts python:3.11 bash
pip install python-keycloak
python userCreate.py

```
#### Response
```
[
  {
    "status": "success",
    "user": "user1",
    "id": "20774d49-84a7-4dc0-a099-1421186d5b51",
    "message": "User successful created"
  },
  {
    "status": "success",
    "user": "user2",
    "id": "6d6be780-3a42-4006-8c79-dd56d81cf6f0",
    "message": "User successful created"
  },
  {
    "status": "success",
    "user": "user3",
    "id": "eee8734f-b5c9-4791-a5f3-2cb90bbf58da",
    "message": "User successful created"
  }
]
```

## Delete users
Define a variable with the users you want to delete </br>
Alternatively, specify these users in the yaml file </br>
whose name is defined in the usersYamlFile variable. </br>
Example of filling in a file:
```
---
- user1
- user2
- user3
```
#### Set required users to delete in yaml file example ./users-del.yaml
#### Command
```
docker run -it --rm --network host -v /dir-with-script/on-your-host:/scripts -w /scripts python:3.11 bash
pip install python-keycloak
python userDelete.py
```
#### Response
```
[
  {
    "status": "success",
    "user": "user1",
    "message": "User successful deleted"
  },
  {
    "status": "success",
    "user": "user2",
    "message": "User successful deleted"
  },
  {
    "status": "success",
    "user": "user3",
    "message": "User successful deleted"
  }
]
```

## Get access token and token exchange
#### Command
```
docker run -it --rm --network host -v /dir-with-script/on-your-host:/scripts -w /scripts python:3.11 bash
pip install requests
python tokenExchange.py
```
#### Response
```
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUI...",
  "expires_in": 1800,
  "refresh_expires_in": 0,
  "token_type": "Bearer",
  "not-before-policy": 0,
  "session_state": "b5fdb54f-cb14-4263-9a75-5a05446994a3",
  "scope": "email profile",
  "issued_token_type": "urn:ietf:params:oauth:token-type:access_token"
}
```
