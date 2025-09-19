class Spreadsheet(object):

    def __init__(self, rows):
        self.rows = rows
        self.cols = 26
        self.sheet = [[0] * self.cols for _ in range(rows)]

    def _parseCell(self, cell):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        return row, col

    def setCell(self, cell, value):
        row, col = self._parseCell(cell)
        self.sheet[row][col] = value

    def resetCell(self, cell):
        row, col = self._parseCell(cell)
        self.sheet[row][col] = 0

    def getValue(self, formula):
        formula = formula[1:]  # remove '='
        parts = formula.split('+')
        total = 0
        for part in parts:
            if part[0].isalpha():
                row, col = self._parseCell(part)
                total += self.sheet[row][col]
            else:
                total += int(part)
        return total
