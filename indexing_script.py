from google.oauth2 import service_account
from googleapiclient.discovery import build

print("Cargando credenciales desde 'sa.json'")
SCOPES = ["https://www.googleapis.com/auth/indexing"]

try:
    credentials = service_account.Credentials.from_service_account_file("sa.json", scopes=SCOPES)
    service = build("indexing", "v3", credentials=credentials)

    body = {
        "url": "https://shopwithcarlos.xyz/",
        "type": "URL_UPDATED"
    }

    response = service.urlNotifications().publish(body=body).execute()
    print("✅ Éxito:", response)

except Exception as e:
    print("❌ Error inesperado:", e)
    exit(1)
