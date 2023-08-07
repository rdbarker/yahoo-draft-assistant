import xlwings as xw


class ExcelWriter:
    def __init__(self, workbook_location, sheet_name):
        self.rows = []
        self.workbook = xw.Book(workbook_location)
        self.sheet = self.workbook.sheets[sheet_name]

    def add_row(self, string_to_write):
        self.rows.append(string_to_write)

    def write_rows(self, starting_grid_location):
        self.sheet[starting_grid_location].value = self.rows
        self.sheet[starting_grid_location].expand().value

    def clear_rows(self):
        self.rows = []
