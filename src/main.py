import win32com.client

try:
    catia = win32com.client.Dispatch("CATIA.Application")
    catia.Visible = True
    print("✅ Connexion réussie à CATIA !")
except Exception as e:
    print("❌ Erreur de connexion :", e)
