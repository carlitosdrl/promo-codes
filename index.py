from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

def main():
    # Obtener ruta del archivo de credenciales desde variable de entorno
    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "sa.json")

    print(f"Usando credenciales desde '{creds_path}'")

    SCOPES = ["https://www.googleapis.com/auth/indexing"]

    # Cargar credenciales desde el archivo JSON
    credentials = service_account.Credentials.from_service_account_file(
        creds_path, scopes=SCOPES
    )

    # Construir cliente de la API Indexing
    service = build("indexing", "v3", credentials=credentials)

    body = {
        "url": "https://shopwithcarlos.xyz/",
        "type": "URL_UPDATED"
    }

    try:
        response = service.urlNotifications().publish(body=body).execute()
        print("✅ Éxito:", response)
    except Exception as e:
        print("❌ Error inesperado:", e)

if __name__ == "__main__":
    main()
