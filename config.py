import os
from dotenv import load_dotenv

if not load_dotenv():
    raise FileNotFoundError('.env file does not exist') 

TOKEN = os.environ.get('BOT_TOKEN')
if not TOKEN:
    raise ValueError("BOT_TOKEN is not set in the environment variables")

DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 'yes', 'on')

TEAM_MEMBERS_STR = """
Team:
- Lukyanov E. - @queue_qq
- Serik T. - @tam_serik
- Skripchenko V. - @Sunny_Vls
- Islamberdi A. - @Y191900
"""
