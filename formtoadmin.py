from auth import *
from dotenv import load_dotenv
from os import getenv

load_dotenv()

gc = get_gspread_client()
formAnsSh = gc.open_by_key(getenv('FORM_ANS_SHEET_KEY'))
adminSh = gc.open_by_key(getenv('ADMIN_SHEET_KEY'))
ws1 = formAnsSh.get_worksheet(0)
ws2 = adminSh.get_worksheet(0)
currentrow = 1

missDict = {'미션1': 1, '미션2': 2, '미션3': 3, '미션4': 4, '미션5': 5, '미션6': 6, '미션7': 7, '미션8': 8, '미션9': 9, '미션10': 10, '미션11': 11, '미션12': 12, '미션13': 13, '미션14': 14, '미션15': 15, '미션16': 16}

DEBUG = False

def update_admin_with_form():

    global DEBUG

    #Read all values and find length
    allCurrentVal = ws1.get_all_values()
    allAdminVal = ws2.get_all_values()
    totalRows = len(allCurrentVal)
    print(logtimer(), "[FTA] Successfully fetched spreadsheets.")

    #Skip tasks if there are no entries
    if totalRows == 0:
        print(logtimer(), "[FTA] No Google Form entry yet.")
        return 0
    
    #Identify rows to work on, and skip tasks if there are nothing to update
    rowsToWorkOn = []

    for i in range(2, totalRows+1):
        if not allCurrentVal[i-1][6]:
            rowsToWorkOn.append(i)

    if rowsToWorkOn:
        print(logtimer(), f"[FTA] Rows to work on: {rowsToWorkOn}")
    else:
        print(logtimer(), "[FTA] Nothing to update.")
        return 0

    #Work on each row
    for i in rowsToWorkOn:

        name = allCurrentVal[i-1][1]
        insta = allCurrentVal[i-1][3]
        print(logtimer(), f"[FTA] Updating entry of {name}")

        #Get corresponding row for admin sheet by converting mission via dictionary
        #Empty strings are sanitized for corrAdminRow
        corrAdminRowIndex = missDict[allCurrentVal[i-1][5]] - 1
        corrAdminRow = [x for x in allAdminVal[corrAdminRowIndex] if x != '']
        corrAdminRowLen = len(corrAdminRow)
        print(logtimer(), f"[FTA] Length of corresponding admin row for {name}: {corrAdminRowLen}")

        #Update the value of appropriate cell online
        ws2.update_cell(corrAdminRowIndex+1, corrAdminRowLen+1, name+" "+insta)
        if corrAdminRowLen == 1:
            ws2.format(to_a1(corrAdminRowIndex+1, corrAdminRowLen+1), {"backgroundColor": {"red": 0.0, "green": 48.0, "blue": 0.0}})
        print(logtimer(), f"[FTA] Successfully updated entry of {name} (Instagram handle: {insta})")
        #Mark the row worked on
        ws1.update_cell(i, 7, "V")

        #Update the value of appropriate cell for allAdminVal
        #Port empty string sanitization from above
        allAdminVal[corrAdminRowIndex] = corrAdminRow
        allAdminVal[corrAdminRowIndex].append(name+" "+insta) 
        if DEBUG is True:
            print(logtimer(), f"[FTA] DEBUG: showing corresponding local allAdminVal row: {allAdminVal[corrAdminRowIndex]}")
        #Mark the row worked on
        allCurrentVal[i-1][6] = "V"
        if DEBUG is True:
            print(logtimer(), f"[FTA] DEBUG: showing marked allCurrentVal row: {allCurrentVal[i]}")

if __name__ == "__main__":

    update_admin_with_form()
