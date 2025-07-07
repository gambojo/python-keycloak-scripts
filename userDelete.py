#!/usr/bin/env python3

from keycloak import KeycloakAdmin, KeycloakOpenIDConnection
import urllib3, json, yaml
# Disable warnings
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

''' docker run -it --rm --network host -v /папка-со-скриптом/на-твоей-машине:/scripts -w /scripts python:3.11 bash
    pip install python-keycloak
    python userDelete.py '''

# Set credentials
adminUser = 'apihubidentity'
adminPassword = 'C2KFi6uA-_'
clientId = 'apihub-cli'
realm = 'APIHUB'
url = 'https://keycloak.apps.k8s-6.cp.dev.cldx.ru'
usersYamlFile = 'users-del.yaml'

''' Define a variable with the users you want to delete
    Alternatively, specify these users in the yaml file
    whose name is defined in the usersYamlFile variable.
    Example of filling in a file:
    ---
    - user1
    - user2
    - user3 '''

usersToDeleteDefault = [
    'user1'
]


def parseUsers(usersToDeleteDefault):
    try:
        with open(usersYamlFile) as file:
            usersToDelete = yaml.safe_load(file)
    except Exception:
        usersToDelete = usersToDeleteDefault
        pass
    return usersToDelete

def admin(adminUser, adminPassword, clientId, realm, url):
    kcConnection = KeycloakOpenIDConnection(username=adminUser, password=adminPassword,
                                            client_id=clientId, server_url=url,
                                            realm_name=realm, verify=False)
    kcAdmin = KeycloakAdmin(connection=kcConnection)
    return kcAdmin

def getUserID(username, kcAdmin):
    userID = kcAdmin.get_user_id(username)
    return userID

def userDelete(userId, kcAdmin):
    delUser = kcAdmin.delete_user(user_id=userId)
    return delUser

def msgCreate(status, username, message):
    msg = {
        "status": status,
        "user": username,
        "message": message
    }
    return msg

def main():
    kcAdmin = admin(adminUser, adminPassword, clientId, realm, url)
    jsonResult = []
    usersToDelete = parseUsers(usersToDeleteDefault)
    for username in usersToDelete:
        userId = getUserID(username, kcAdmin)
        try:
            userDelete(userId, kcAdmin)
            msg = msgCreate("success", username, "User successful deleted")
            jsonResult.append(msg)
        except Exception:
            msg = msgCreate("error", username, "User not found")
            jsonResult.append(msg)
            pass
    print(json.dumps(jsonResult, indent=2))

if __name__ == '__main__':
    main()
