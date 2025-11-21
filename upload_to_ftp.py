from ftplib import FTP

FTP_HOST = "ftpadr.kantarmedia.fr"
FTP_USER = "ADR_KETILMED_SMAUGER"
FTP_PASS = "S09MAUGER12"

# Ton fichier local à envoyer
local_file_path = "RADIO_HEBDO.csv"

# Le nom du fichier une fois sur le FTP
remote_file_name = "2025 semaine 40 KETIL - DONNEES RADIO HEBDO_ (1) RADIO_HEBDO.CSV"

# Le dossier FTP
folder = "HEBDO RADIO"

ftp = FTP(FTP_HOST)
print("🔌 Connexion au FTP...")
ftp.login(FTP_USER, FTP_PASS)
print("✔ Connecté !")

# Aller dans le dossier HEBDO RADIO
ftp.cwd(folder)

# Envoyer le fichier
with open(local_file_path, "rb") as f:
    ftp.storbinary(f"STOR {remote_file_name}", f)

print(f"📤 Upload terminé : {remote_file_name} → {folder}")

ftp.quit()
