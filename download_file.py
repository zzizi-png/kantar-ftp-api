from ftplib import FTP

FTP_HOST = "ftpadr.kantarmedia.fr"
FTP_USER = "ADR_KETILMED_SMAUGER"
FTP_PASS = "S09MAUGER12"

FILE_TO_DOWNLOAD = "202510 KETIL - DONNEES RADIO_ (1) RADIO_MENSUELLE.CSV"
FOLDER = "MENSUEL RADIO"

try:
    print("🔌 Connexion au serveur FTP…")
    ftp = FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)

    # Aller dans le dossier
    ftp.cwd(FOLDER)
    print(f"📂 Dossier ouvert : {FOLDER}")

    # Télécharger le fichier
    print(f"⬇ Téléchargement : {FILE_TO_DOWNLOAD}")
    with open("downloaded.csv", "wb") as local_file:
        ftp.retrbinary(f"RETR {FILE_TO_DOWNLOAD}", local_file.write)

    ftp.quit()
    print("✔ Téléchargement terminé ! Fichier = downloaded.csv")

except Exception as e:
    print("❌ Erreur :", e)
