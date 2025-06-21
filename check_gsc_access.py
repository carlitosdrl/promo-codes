from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/webmasters"]
SERVICE_ACCOUNT_FILE = "sa.json"

print("📂 Cargando credenciales...")
try:
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("webmasters", "v3", credentials=credentials)

    print("🔍 Consultando propiedades de Search Console...")
    site_list = service.sites().list().execute()

    print("\n📋 Propiedades visibles por esta cuenta de servicio:\n")
    for site in site_list.get("siteEntry", []):
        print(f"- {site['siteUrl']} (Permiso: {site['permissionLevel']})")

except Exception as e:
    print("❌ Error:", e)
    exit(1)
