from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 27473362))
    API_HASH = env.get("TELEGRAM_API_HASH", "099c6626bcc1b0f8dc0183cc10cc4015")
    OWNER_ID = int(env.get("OWNER_ID", 1942629977))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "file_streame_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6936021254:AAE4HXA9L72kSOPP6R-3y5IWeO8P_5eYcy0")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1001672253678))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "https://filestreamtgx-5b967f463a7a.herokuapp.com")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
