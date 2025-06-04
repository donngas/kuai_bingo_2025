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

missDict = {'카페에서 공부하기': 1, 'SW프로그래밍의 기초 과제 복습하기': 2, '오늘의 플래너 쓰기': 3, '분위기 전환하러 PC방 or 노래방 가기': 4, '컴퓨터프로그래밍I 과제 복습하기': 5, '우정정보관에서 공부하기': 6, '스터디윗미 보면서 공부하기': 7, '공부 플레이리스트 인증하기': 8, '하나스퀘어에서 공부하기': 9, '내가 가장 아끼는 필기구 소개하기': 10, '머리 식히러 산책하기': 11, '천원의 아침밥 먹고 아침공부하기': 12, '과학도서관에서 공부하기': 13, '공부하다가 출출해서 맛있는 간식 먹기': 14, '전산수학 공부하기': 15, '정운오IT교양관에서 공부하기': 16}

DEBUG = False

def update_admin_with_form():

    global DEBUG

    #Read all values and find length
    allCurrentVal = ws1.get_all_values()
    allAdminVal = ws2.get_all_values()
    totalRows = len(allCurrentVal)
    print(logtimer(), "[FTA] Successfully fetched spreadsheets.")

    #Skip tasks if there are no entries
    if totalRows == 1:
        print(logtimer(), "[FTA] No Google Form entry yet.")
        return 0
    
    #Identify rows to work on, and skip tasks if there are nothing to update
    rowsToWorkOn = []

    for i in range(1, totalRows+1):
        if not allCurrentVal[i-1][8]:
            rowsToWorkOn.append(i)

    if rowsToWorkOn:
        print(logtimer(), f"[FTA] Rows to work on: {rowsToWorkOn}")
    else:
        print(logtimer(), "[FTA] Nothing to update.")
        return 0

    #Work on each row
    for i in rowsToWorkOn:

        name = allCurrentVal[i-1][2]
        insta = allCurrentVal[i-1][5]
        print(logtimer(), f"[FTA] Updating entry of {name}")

        #Get corresponding row for admin sheet by converting mission via dictionary
        #Empty strings are sanitized for corrAdminRow
        corrAdminRowIndex = missDict[allCurrentVal[i-1][6]] - 1
        corrAdminRow = [x for x in allAdminVal[corrAdminRowIndex] if x != '']
        corrAdminRowLen = len(corrAdminRow)
        print(logtimer(), f"[FTA] Length of corresponding admin row for {name}: {corrAdminRowLen}")

        #Update the value of appropriate cell online
        ws2.update_cell(corrAdminRowIndex+1, corrAdminRowLen+1, name+" "+insta)
        if corrAdminRowLen == 1:
            ws2.format(to_a1(corrAdminRowIndex+1, corrAdminRowLen+1), {"backgroundColor": {"red": 0.0, "green": 48.0, "blue": 0.0}})
        print(logtimer(), f"[FTA] Successfully updated entry of {name} (Instagram handle: {insta})")
        #Mark the row worked on
        ws1.update_cell(i, 9, "V")

        #Update the value of appropriate cell for allAdminVal
        #Port empty string sanitization from above
        allAdminVal[corrAdminRowIndex] = corrAdminRow
        allAdminVal[corrAdminRowIndex].append(name+" "+insta) 
        if DEBUG is True:
            print(logtimer(), f"[FTA] DEBUG: showing corresponding local allAdminVal row: {allAdminVal[corrAdminRowIndex]}")
        #Mark the row worked on
        allCurrentVal[i-1][8] = "V"
        if DEBUG is True:
            print(logtimer(), f"[FTA] DEBUG: showing marked allCurrentVal row: {allCurrentVal[i]}")

if __name__ == "__main__":

    update_admin_with_form()
