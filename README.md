# python-keycloak-scripts

## Create users
#### Command
```
./userCreate.py
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
#### Command
```
./userDelete.py
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
./tokenExchange.py
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
