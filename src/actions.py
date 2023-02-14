from datetime import datetime

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config.settings import Settings
from gapi.auth import get_credentials

test_range='2023!A2:E999'

class Actions:

    @staticmethod
    async def register_run(raw: str) -> str:
        today = datetime.now().date().strftime("%d/%m/%Y")

        try:
            data = [float(x) for x in raw.split()]
            minutes, distance = (max(data), min(data), )
            response = (
                f"Então, você correu {distance} km em {minutes} minutos?\n\n"
                f"Quer que eu registre isso na planilha com a data de {today}? (S/N?)"
            )

        except Exception as e:
            response = "Foi mal, não entendi nada, repete por favor."
            if Settings.DEBUG:
                response += f"({str(e)})"

        finally:
            return response

    @staticmethod
    async def get_entire_sheet_data():

        rows = []
        response = ""
        creds = get_credentials()

        try:
            service = build('sheets', 'v4', credentials=creds)

            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=Settings.SPREADSHEET_ID,
                                        range=test_range).execute()
            values = result.get('values', [])

            if not values:
                raise Exception('No data found!')

            for v in values:
                rows.append("".join(v))

            response = "\n".join(rows)[:1000]

        except HttpError as err:
            response = f"Opa, deu erro!"
            if Settings.DEBUG:
                response += f"({str(err)})"
            return response

        finally:
            return response
