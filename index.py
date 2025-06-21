from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/indexing"]
SERVICE_ACCOUNT_FILE = "sa.json"   # Ahora apunta al archivo creado en GitHub Actions

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

service = build("indexing", "v3", credentials=credentials)

body = {
    "url": "https://shopwithcarlos.xyz/",
    "type": "URL_UPDATED"
}

response = service.urlNotifications().publish(body=body).execute()
print("✅ Éxito:", response)
