import requests

# Discord Webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1466766721397297172/erbcxrLow4LPkY3QyxWTawbYeIyppu9bsv2U-Fu51IBB6_jjDIZ6Nr6fdQmgCcw8s1nF"

# GIF URL - Direkte Media-URL verwenden!
# Tenor: Rechtsklick auf GIF → "Bildadresse kopieren"
# Giphy: Rechtsklick auf GIF → "Bildadresse kopieren"  
# Die URL muss mit .gif enden und von media.tenor.com oder i.giphy.com kommen
# Giphy funktioniert besser mit Discord!
# GIPHY VERWENDEN - funktioniert immer!
# 1. Gehe zu giphy.com
# 2. Suche ein GIF
# 3. Klicke auf "Share" → "Copy GIF Link"
# 4. Oder: Rechtsklick auf GIF → "Bildadresse kopieren"
IMAGE_URL = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjI5aHQ3YjFpanYxbWh4OGliYzU2emJzMDdxOWtpaHF2NWloZzlxZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NAivbJDbjN9sgkLzzE/giphy.gif"

# Webhook Payload
payload = {
    "embeds": [
        {
            "title": "🚨Incoming GitHub News🚨",
            "description": "[✅ Jan submitted a new commit. ✅](https://jan.dev.noseryoung.ch) #StayFocused #StayUserFriendly #JohnDoe",
            "color": 0x4a71f0,
            "image": {
                "url": IMAGE_URL
            }
        }
    ]
}

# Nachricht senden
response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 204:
    print("✅Nachricht erfolgreich gesendet!")
else:
    print(f"❌ Fehler: {response.status_code}")
    print(response.text)
