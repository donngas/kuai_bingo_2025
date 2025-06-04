import time
from auth import *
from formtoadmin import *
from admintopublic import *

gc = get_gspread_client()

def main():
    
    while True:

        print(logtimer(), "[MAIN]", "\033[1;32mBeginning new main cycle.\033[0m")

        try: 

            update_admin_with_form()
            print(logtimer(), "[MAIN] Successfully updated admin sheet with form answer sheet via FTA module.")
            
            time.sleep(0.5)

            update_public_with_admin()
            print(logtimer(), "[MAIN] Successfully updated public bingo sheet with admin sheet via ATP module.")

        except Exception as e:

            print(logtimer(), f"[MAIN] ERROR: {e}")

        time.sleep(45)

if __name__ == "__main__":
    print(logtimer(), "[MAIN] Script initiated.")
    main()