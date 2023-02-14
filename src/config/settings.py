import logging

from decouple import config


class Settings:
    DEBUG = config('DEBUG', cast=bool)

    BOT_TOKEN = config('BOT_TOKEN', cast=str)
    GAPI_TOKEN = config('GAPI_TOKEN', cast=str)
    SPREADSHEET_ID = config('SPREADSHEET_ID', cast=str)
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
