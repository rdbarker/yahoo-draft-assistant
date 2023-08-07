import xlwings as xw
from src.excel_writer import ExcelWriter
from src.config import Config
from src.yahoo import Yahoo
import keyboard

config = Config("config.ini", "oauth2.json")
writer = ExcelWriter(config.workbook_location, config.sheet_name)
yahoo = Yahoo(config)


def update_draft_results():
    for pick in yahoo.draft_picks():
        writer.add_row([pick["name"]["full"]])
    writer.write_rows(config.starting_cell)


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed(config.refesh_keys):
            update_draft_results()
        if keyboard.is_pressed(config.quit_keys):
            break
