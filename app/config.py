import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URLS = {
    "Arts": "https://allduniv.ac.in/p/716/ug-admission-2026-faculty-of-arts",
    "Science": "https://allduniv.ac.in/p/710/ug-admission-2026-science-faculty",
    "IPS": "https://allduniv.ac.in/p/713/ug-admission-2026-ips",
}