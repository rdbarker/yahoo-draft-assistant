import json

print("Enter your Client ID (Consumer Key): ")
clientId = input()
print("Enter your Client Secret (Consumer Secret): ")
clientSec = input()

creds = {"consumer_key": clientId, "consumer_secret": clientSec}
with open("oauth2.json", "w") as f:
    f.write(json.dumps(creds))
