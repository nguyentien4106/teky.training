# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

def openFile(filename):
    return open(filename, "r").read()

def collectTRs(table):
    return table.select("tr")

def collectTDs(tr):
    return tr.select("td")

def collectText(elements):
    if isinstance(elements, list):
        return list(map(lambda item: item.text, elements))
    return elements.text

def writeExcel(excel, filename):
    df = pd.DataFrame(excel)
    df.to_excel(filename, sheet_name="Data", index=False, header=False)

def writeTable(table, index):
    trs = collectTRs(table)
    excel_table = []
    for tr in trs:
        tds = collectTDs(tr)
        excel_table.append(collectText(tds))

    writeExcel(excel_table, f"{index}.xlsx")

def main():
    # Opening the html file
    data = openFile("data.html")
    
    # Creating a BeautifulSoup object and specifying the parser
    bs = BeautifulSoup(data, 'lxml')
    tables = bs.select("table")
    i = 0
    for table in tables:
        writeTable(table, i)
        i += 1


if __name__ == '__main__':
    main()