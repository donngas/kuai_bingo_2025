from gspread import service_account
from os import getenv
from dotenv import load_dotenv
from time import strftime, localtime

load_dotenv()

authpath = str(getenv('PATH_TO_AUTH_KEY_JSON'))

def get_gspread_client():
    return service_account(filename=authpath)

def to_a1(row, col):
    col_str = ''
    while col > 0:
        col, rem = divmod(col - 1, 26)
        col_str = chr(65 + rem) + col_str
    return f'{col_str}{row}'

def logtimer():
    return strftime("%Y-%m-%d %H:%M:%S", localtime())

def timestamp():
    return strftime("%Y년 %m월 %d일 %H시 %M분 %S초", localtime())