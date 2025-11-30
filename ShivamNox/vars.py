# (c) ShivamNox
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', ' '))  #Required
    API_HASH = str(getenv('API_HASH', ' ')) #Required
    BOT_TOKEN = str(getenv('BOT_TOKEN', ' ')) #Required
    name = str(getenv('name', 'FileStreamBot')) #Optional
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1003078994544')) #Required
    PORT = int(getenv('PORT', '3000'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", " ").split())  #Required
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', ' ')) #Required
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '0.0.0.0:3000')) if not ON_HEROKU or getenv('FQDN', '0.0.0.0:3000') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://edustream-video.cariyep778.workers.dev/".format(FQDN) #Required
    else:
        URL = "https://edustream-video.cariyep778.workers.dev/".format(FQDN) #Required
    DATABASE_URL = str(getenv('DATABASE_URL', ' ')) #Required
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', ' ')) #Required
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) #Leave as it is.
