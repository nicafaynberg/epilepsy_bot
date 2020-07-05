import json

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from config import GOOGLE_CREDENTIALS

scope = ['https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_dict(GOOGLE_CREDENTIALS, scope)
client = gspread.authorize(creds)
link = "https://docs.google.com/spreadsheets/d/1llFFWnE3XV8TZrX39VUNihkXZwjwQId95j7w0Qb1bRs/edit?usp=sharing"
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open_by_url(link).sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
