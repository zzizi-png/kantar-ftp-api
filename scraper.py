import time, random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

# Charger fichier CSV
df = pd.read_csv("entreprises.csv", dtype=str)  # ton fichier ici
df["chiffre_affaires"] = None

# Options Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# User-agent aléatoire
ua = UserAgent()
options.add_argument(f"user-agent={ua.random}")

# Lancer Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def get_chiffre_affaires(siret):
    try:
        url = f"https://www.societe.com/societe/{siret}.html"
        driver.get(url)

        time.sleep(random.uniform(3, 6))  # anti-bot

        try:
            element = driver.find_element(By.XPATH, "//td[contains(text(),'Chiffre d’affaires')]/following-sibling::td")
            return element.text.strip()
        except:
            return "Non disponible"

    except Exception as e:
        return f"Erreur : {e}"

# Exécution
for i, row in df.iterrows():
    siret = str(row["siret"]).strip()
    print(f"→ Recherche CA pour {siret}")

    df.at[i, "chiffre_affaires"] = get_chiffre_affaires(siret)

    time.sleep(random.uniform(4, 9))

driver.quit()

df.to_csv("entreprises_CA.csv", index=False)
print("🎉 Fichier exporté : entreprises_CA.csv")
