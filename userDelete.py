#!/usr/bin/env python3

from keycloak import KeycloakAdmin, KeycloakOpenIDConnection
import urllib3, json, yaml
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)


adminUser = 'admin'
adminPassword = 'password'
clientId = 'admin-cli'
realm = 'master'
server = 'https://keycloak-server.ru'
usersYamlFile = 'users-del.yaml'

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

def admin(adminUser, adminPassword, clientId, realm, server):
    kcConnection = KeycloakOpenIDConnection(username=adminUser, password=adminPassword,
                                            client_id=clientId, server_url=server,
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
    kcAdmin = admin(adminUser, adminPassword, clientId, realm, server)
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
