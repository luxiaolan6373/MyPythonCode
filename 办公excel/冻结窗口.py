import openpyxl
fiilename=r"C:\Users\Administrator\Desktop\top250.xlsx"
wb=openpyxl.load_workbook(fiilename)
ws=wb.active
print(ws.title)
#指定一个单元格,它上方和坐标的单元格将全部定住
ws.freeze_panes='B2'
#解冻
#ws.freeze_panes=None
wb.save(fiilename)