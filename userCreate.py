#!/usr/bin/env python3

from keycloak import KeycloakAdmin, KeycloakOpenIDConnection
import urllib3, json, yaml
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)


adminUser = 'admin'
adminPassword = 'password'
clientId = 'admin-cli'
realm = 'master'
server = 'https://keycloak-server.ru'
usersYamlFile = 'users-add.yaml'

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

def admin(adminUser, adminPassword, clientId, realm, server):
    kcConnection = KeycloakOpenIDConnection(username=adminUser, password=adminPassword,
                                            client_id=clientId, server_url=server,
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
    kcAdmin = admin(adminUser, adminPassword, clientId, realm, server)
    usersToCreate = parseUsers(usersToCreateDefault)
    for item in usersToCreate:
        userID = userCreate(item['name'], item['password'], item['email'], kcAdmin)
        msg = msgCreate("success", item['name'], userID, "User successful created")
        jsonResult.append(msg)
    print(json.dumps(jsonResult, indent=2))


if __name__ == '__main__':
    main()
