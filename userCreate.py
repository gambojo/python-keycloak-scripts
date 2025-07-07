#!/usr/bin/env python3

from keycloak import KeycloakAdmin, KeycloakOpenIDConnection
import urllib3, json, yaml
# Disable warnings
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

''' docker run -it --rm --network host -v /папка-со-скриптом/на-твоей-машине:/scripts -w /scripts python:3.11 bash
    pip install python-keycloak
    python userCreate.py '''

# Set credentials
adminUser = 'apihubidentity'
adminPassword = 'C2KFi6uA-_'
clientId = 'apihub-cli'
realm = 'APIHUB'
url = 'https://keycloak.apps.k8s-6.cp.dev.cldx.ru'
usersYamlFile = 'users-add.yaml'
''' Define a variable with the users you want to add
    Alternatively, specify these users in the yaml file
    whose name is defined in the usersYamlFile variable.
    Example of filling in a file:
    ---
    - name: user1
      email: user1@local.ru
      password: user1Password
    - name: user2
      email: user2@local.ru
      password: user2Password
    - name: user3
      email: user3@local.ru
      password: user3Password '''

usersToCreateDefault = [
    {
        "name": "user1",
        "email": "user1@local.ru",
        "password": "user1Password"
    }
]


def parseUsers(usersToCreateDefault):
    try:
        with open(usersYamlFile) as file:
            usersToCreate = yaml.safe_load(file)
    except Exception:
        usersToCreate = usersToCreateDefault
        pass
    return usersToCreate

def admin(adminUser, adminPassword, clientId, realm, url):
    kcConnection = KeycloakOpenIDConnection(username=adminUser, password=adminPassword,
                                            client_id=clientId, server_url=url,
                                            realm_name=realm, verify=False)
    kcAdmin = KeycloakAdmin(connection=kcConnection)
    return kcAdmin

def userCreate(username, password, email, kcAdmin):
    addUser = kcAdmin.create_user({"email": email, "username": username,
                                   "enabled": True, "credentials": [{"value": password, "type": "password",
                                                                     "temporary": False}]}, exist_ok=True)
    return addUser

def msgCreate(status, username, userID, message):
    msg = {
        "status": status,
        "user": username,
        "id": userID,
        "message": message
    }
    return msg

def main():
    jsonResult = []
    kcAdmin = admin(adminUser, adminPassword, clientId, realm, url)
    usersToCreate = parseUsers(usersToCreateDefault)
    for item in usersToCreate:
        userID = userCreate(item['name'], item['password'], item['email'], kcAdmin)
        msg = msgCreate("success", item['name'], userID, "User successful created")
        jsonResult.append(msg)
    print(json.dumps(jsonResult, indent=2))

if __name__ == '__main__':
    main()
