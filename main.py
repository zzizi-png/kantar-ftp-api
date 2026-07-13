from fastapi import FastAPI, Response
from ftplib import FTP_TLS

app = FastAPI()

FTP_HOST = "ftpadr.kantarmedia.fr"
FTP_USER = "ADR_KETILMED_SMAUGER"
FTP_PASS = "S09MAUGER12"
REMOTE_FOLDER = "HEBDO RADIO"


def _connect_ftps():
    ftps = FTP_TLS()
    ftps.connect(FTP_HOST, 21, timeout=15)
    ftps.auth()
    ftps.prot_p()
    ftps.login(FTP_USER, FTP_PASS)
    ftps.set_pasv(True)
    ftps.cwd(REMOTE_FOLDER)
    return ftps


def _latest_csv(ftps) -> str | None:
    files = [f for f in ftps.nlst() if f.upper().endswith(".CSV")]
    # "2026 semaine 27 ..." → tri alphabétique = tri chronologique
    return sorted(files)[-1] if files else None


@app.get("/download-file")
def download_file():
    try:
        ftps = _connect_ftps()
        remote_file = _latest_csv(ftps)
        if not remote_file:
            ftps.quit()
            return {"error": "Aucun fichier CSV trouvé dans le dossier"}

        buffer = bytearray()
        ftps.retrbinary(f"RETR {remote_file}", buffer.extend)
        ftps.quit()

        return Response(
            content=bytes(buffer),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename={remote_file}"},
        )

    except Exception as e:
        return {"error": str(e)}


@app.get("/latest-filename")
def latest_filename():
    """Diagnostic : retourne le nom du fichier qui sera téléchargé."""
    try:
        ftps = _connect_ftps()
        name = _latest_csv(ftps)
        ftps.quit()
        return {"file": name}
    except Exception as e:
        return {"error": str(e)}
