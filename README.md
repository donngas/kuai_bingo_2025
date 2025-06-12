# kuai_bingo_2025
This is a real-time automation tool that updates and displays completion status for each mission in [Korea University Department of Artificial Intelligence 2025 Bingo Event](https://www.instagram.com/p/DKd2NMXh6Ag/?utm_source=ig_web_copy_link&igsh=NnoyeDJsM3dwcmt0).

## Requirements
- Everything in requirements.txt
- PC/Server/(Cloud) Virtual Machine with Python runtime for real-time service
- Google service bot for Google Sheets & its authentication key file.

## Modules
- main.py: Performs update loop in set time interval.
- auth.py: Authenticates a Google service bot with Google Sheets API([gspread](https://docs.gspread.org/)), providing some utility functions as well.
- formtoadmin.py: Updates disclosed admin sheet with Google form responses.
- admintopublic.py: Updates public bingo status sheet with admin sheet data.

## Log
- Successfully serviced for KUAI Bingo Event 2025(June 5, 2025 - June 7, 2025), continuously and in real-time.
- [Public bingo status sheet](https://docs.google.com/spreadsheets/d/1wBV3FgkoCbsiNpDkDemK85WXgfDtZVk655P5dIHTqHM/edit?gid=0#gid=0)
