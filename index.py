import sys
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/indexing"]
SERVICE_ACCOUNT_FILE = "sa.json"  # Este archivo se crea desde el secret en GitHub Actions

def main():
    try:
        print("Cargando credenciales desde", SERVICE_ACCOUNT_FILE)
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        print("Construyendo servicio de Google Indexing API...")
        service = build("indexing", "v3", credentials=credentials)

        body = {
            "url": "https://shopwithcarlos.xyz/",
            "type": "URL_UPDATED"
        }
        print("Enviando petición con cuerpo:")
        print(json.dumps(body, indent=2))

        response = service.urlNotifications().publish(body=body).execute()
        print("✅ Éxito. Respuesta de la API:")
        print(json.dumps(response, indent=2))

    except HttpError as e:
        print(f"HttpError: {e.status_code} - {e._get_reason()}")
        try:
            content = e.content.decode()
            print("Contenido del error:")
            print(content)
        except Exception:
            print("No se pudo decodificar el contenido del error.")
        sys.exit(1)
    except Exception as e:
        print("Error inesperado:", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
