import gspread
import auth

gc = auth.get_gspread_client()
sh = gc.open_by_key('1EtBESSL4iLeri2jajRfooAKU6SCmmZfpQzEj748B9dU')
ws = sh.get_worksheet(0)

val = ws.get_all_values()
print(val)
print(len(val[1]))