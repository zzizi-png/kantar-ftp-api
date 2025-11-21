from ftplib import FTP_TLS

host = "ftpadr.kantarmedia.fr"
user = "ADR_KETILMED_SMAUGER"
password = "S09MAUGER12"

try:
    print("🔐 Connexion FTPS sécurisée...")
    ftps = FTP_TLS()
    
    # Connexion au port 21
    ftps.connect(host, 21, timeout=10)
    
    # Activation de TLS
    ftps.auth()
    ftps.prot_p()

    # Login
    ftps.login(user, password)
    print("✔ Connecté en FTPS (TLS)")

    # Mode passif
    ftps.set_pasv(True)

    # Lister les dossiers à la racine
    print("📂 Liste des dossiers :")
    fichiers = ftps.nlst()

    for f in fichiers:
        print("  ➤", f)

    ftps.quit()

except Exception as e:
    print("❌ Erreur FTPS :", e)
