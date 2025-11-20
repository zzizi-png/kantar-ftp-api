from fastapi import FastAPI, Response
from ftplib import FTP
import os

app = FastAPI()

FTP_HOST = "ftpadr.kantarmedia.fr"
FTP_USER = "ADR_KETILMED_SMAUGER"
FTP_PASS = "S09MAUGER12"

FOLDER = "MENSUEL RADIO"
FILE_TO_DOWNLOAD = "202510 KETIL - DONNEES RADIO_ (1) RADIO_MENSUELLE.CSV"

@app.get("/download-file")
def download_file():
    try:
        ftp = FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd(FOLDER)

        buffer = bytearray()
        ftp.retrbinary(f"RETR {FILE_TO_DOWNLOAD}", buffer.extend)
        ftp.quit()

        return Response(
            content=bytes(buffer),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=data.csv"}
        )

    except Exception as e:
        return {"error": str(e)}
