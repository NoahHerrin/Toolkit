# I know Pandas and other packages exist for this purpose

import sys
import xlrd

class SpreadSheet(object):
    def __init__(self, Path):
        self.Path = Path
        self.Document = xlrd.open_workbook(Path)
        self.SheetNames = self.Document.sheet_names()
        self.Pages = []
        self.ActivePage = None
        self.ActivePageRows = None
        self.ActivePageCols = None

        for name in self.SheetNames:
            self.Pages.append(self.Document.sheet_by_name(name))

    def selectPage(self, PageName):
        if PageName in self.SheetNames:
            self.ActivePage = self.Pages[self.SheetNames.index(PageName)]
            self.ActivePageRows = int(self.ActivePage.cell(0,0).value)
            self.ActivePageCols = int(self.ActivePage.cell(0,1).value)
    def fetchAllEntries(self):
        Data = [[0 for x in range(self.ActivePageCols)] for y in range(self.ActivePageRows)]

        for row in range(self.ActivePageRows):
            for column in range(self.ActivePageCols):
                Data[row][column] = self.ActivePage.cell(row + 1, column).value

        return Data
    def fetchEntry(self, row, column):
        if row >= 0 and row < self.ActivePageRows and column >= 0 and column < self.ActivePageCols:
            return self.ActivePage.cell(row,column).value
        else:
            raise Exception("Invalid row: {} and column: {}".format(row, column))

def TestSpreadSheet():
    path = "D:\Documents\Projects\Python\Toolkit\BetterXLRD\Example.xlsx"
    document = SpreadSheet(path)
    document.selectPage("ExampleSheet")
    print(document.fetchAllEntries())
