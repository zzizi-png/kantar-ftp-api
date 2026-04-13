from ftplib import FTP_TLS

host = "ftpadr.kantarmedia.fr"
user = "ADR_KETILMED_SMAUGER"
password = "S09MAUGER12"

# 👉 Le dossier et fichier que tu veux télécharger
remote_folder = "HEBDO RADIO"
remote_file = "2026 semaine 15 KETIL - DONNEES RADIO HEBDO_ (1) RADIO_HEBDO.CSV"

# 👉 Le nom du fichier en local
local_file = "downloaded_radio3.csv"

try:
    print("🔐 Connexion FTPS...")
    ftps = FTP_TLS()
    ftps.connect(host, 21, timeout=10)
    ftps.auth()
    ftps.prot_p()
    ftps.login(user, password)
    ftps.set_pasv(True)

    print("📂 Aller dans le dossier :", remote_folder)
    ftps.cwd(remote_folder)

    print("⬇ Téléchargement du fichier :", remote_file)
    with open(local_file, "wb") as f:
        ftps.retrbinary(f"RETR {remote_file}", f.write)

    print("✔ Téléchargement terminé →", local_file)

    ftps.quit()

except Exception as e:
    print("❌ Erreur :", e)
