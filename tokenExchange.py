#!/usr/bin/env python3

''' docker run -it --rm --network host -v /папка-со-скриптом/на-твоей-машине:/scripts -w /scripts python:3.11 bash
    pip install requests
    python tokenExchange.py '''

import requests, json

# Set credentials
user = 'user1'
password = 'password'
clientId = 'admin-cli'
requestedUserId = 'dcaf3acb-3ba6-437e-b1ed-337e5bfc556e'
realm = 'master'
server = 'https://keycloak-server.ru'

# Const
url = f"{server}/realms/{realm}/protocol/openid-connect/token"

def accessToken():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'password',
        'client_id': clientId,
        'subject_token_type': 'urn:ietf:params:oauth:token-type:access_token',
        'username': user,
        'password': password
    }
    response = requests.post(url=url, headers=headers, data=data)
    return response.json()['access_token']

def exchangeToken(subjectToken):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'urn:ietf:params:oauth:grant-type:token-exchange',
        'client_id': clientId,
        'subject_token_type': 'urn:ietf:params:oauth:token-type:access_token',
        'requested_token_type': 'urn:ietf:params:oauth:token-type:access_token',
        'requested_subject': requestedUserId,
        'subject_token': subjectToken
    }
    response = requests.post(url=url, headers=headers, data=data)
    return response.json()

def main():
    tokenAccess = accessToken()
    tokenExchange = exchangeToken(tokenAccess)
    jsonResult = json.dumps(tokenExchange, indent=2)
    print(jsonResult)

if __name__ == '__main__':
    main()
