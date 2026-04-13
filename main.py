from fastapi import FastAPI, Response
from ftplib import FTP_TLS

app = FastAPI()

# 🔐 Informations FTPS
FTP_HOST = "ftpadr.kantarmedia.fr"
FTP_USER = "ADR_KETILMED_SMAUGER"
FTP_PASS = "S09MAUGER12"

# 📂 Dossier et fichier à télécharger
REMOTE_FOLDER = "HEBDO RADIO"
REMOTE_FILE = "2026 semaine 15 KETIL - DONNEES RADIO HEBDO_ (1) RADIO_HEBDO.CSV"

@app.get("/download-file")
def download_file():
    try:
        print("🔐 Connexion FTPS...")
        ftps = FTP_TLS()

        # Connexion sécurisée
        ftps.connect(FTP_HOST, 21, timeout=15)
        ftps.auth()
        ftps.prot_p()
        ftps.login(FTP_USER, FTP_PASS)
        ftps.set_pasv(True)

        # Aller dans le dossier
        ftps.cwd(REMOTE_FOLDER)

        # Télécharger dans un buffer mémoire
        buffer = bytearray()
        ftps.retrbinary(f"RETR {REMOTE_FILE}", buffer.extend)

        # Fermer connexion
        ftps.quit()

        # Retourner le CSV à Salesforce
        return Response(
            content=bytes(buffer),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename={REMOTE_FILE}"}
        )

    except Exception as e:
        return {"error": str(e)}
