import time
from auth import *
from formtoadmin import *
from admintopublic import *

gc = get_gspread_client()

def main():
    
    while True:

        try: 

            update_admin_with_form()
            print(logtimer(), "[MAIN] Successfully updated admin sheet with form answer sheet via FTA module.")
            update_public_with_admin()
            print(logtimer(), "[MAIN] Successfully updated public bingo sheet with admin sheet via ATP module.")

        except Exception as e:

            print(f"Error: {e}")

        time.sleep(5)

if __name__ == "__main__":
    main()