from ftplib import FTP

FTP_HOST = "ftpadr.kantarmedia.fr"
FTP_USER = "ADR_KETILMED_SMAUGER"
FTP_PASS = "S09MAUGER12"

try:
    print("🔌 Connexion au serveur FTP...")
    ftp = FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)

    print("✔ Connexion réussie !")

    folder = "MENSUEL RADIO"
    ftp.cwd(folder)

    print(f"📂 Contenu du dossier : {folder}")

    ftp.retrlines('LIST')

    ftp.quit()

except Exception as e:
    print("❌ Erreur :", e)


