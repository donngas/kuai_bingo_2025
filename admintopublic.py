from auth import *
from dotenv import load_dotenv
from os import getenv

load_dotenv()

gc = get_gspread_client()
adminSh = gc.open_by_key(getenv('ADMIN_SHEET_KEY'))
publicSh = gc.open_by_key(getenv('PUBLIC_SHEET_KEY'))
ws2 = adminSh.get_worksheet(0)
ws3 = publicSh.get_worksheet(0)

DEBUG = False

def task_index_to_a1(index):
    if not 1 <= index <= 16:
        raise ValueError("Task index must be between 1 and 16.")
    start_col = ord('B')  # Column B = index 0
    start_row = 4         # B4 is the new top-left

    idx = index - 1
    row = idx // 4
    col = idx % 4
    col_letter = chr(start_col + col)
    row_number = start_row + row
    return f"{col_letter}{row_number}"


def update_public_with_admin():

    #Real all values
    allAdminVal = ws2.get_all_values()
    allPublicVal = ws3.get_all_values()
    print(logtimer(), "[ATP] Successfully fetched spreadsheets.")

    #Transpose allAdminVal to prepare for column inspection
    everCompleted = []
    allAdminValTrans = list(zip(*allAdminVal))
    if DEBUG is True:
        print(logtimer(), f"[ATP] DEBUG: transposed column: {allAdminValTrans}")

    #Count ever completed tasks
    try:

        for i in allAdminValTrans[1]:
            if i != '':
                everCompleted.append(allAdminValTrans[1].index(i)+1)
        print(logtimer(), "[ATP] Counted all ever completed tasks.")
        print(logtimer(), f"[ATP] Completed tasks are: {everCompleted}")

    except Exception as e:

        print(logtimer(), f"[ATP] ERROR: {e}. Most likely no entries in admin yet.")

    #Update public sheet online
    for i in everCompleted:
        ws3.format(task_index_to_a1(i), {"backgroundColor": {"red": 0.0, "green": 36.0, "blue": 0.0}})
    ws3.update_cell(9, 2, "마지막 자동 업데이트: " + str(timestamp()))
    print(logtimer(), "[ATP] Successfully updated mission status for public bingo sheet.")

if __name__ == "__main__":
    update_public_with_admin()



