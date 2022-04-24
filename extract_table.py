import pdfplumber
import pandas as pd

writer = pd.ExcelWriter('/Users/yjc/Documents/leetcode/vscode/zhuyu/fenjiu_excel.xls')

with pdfplumber.open('/Users/yjc/Documents/leetcode/vscode/zhuyu/fenjiu.pdf') as pdf:
    for j in range(len(pdf.pages)):
        page = pdf.pages[j]
        tables = page.extract_tables()
        print('in page ', j+1, ' table len: ', len(tables), '\n')
        for i in range(len(tables)):
            table = tables[i]
            table_pd = pd.DataFrame(table[1:], columns=table[0])
            table_pd.to_excel(writer,index=False,sheet_name=f'page{j+1}sheet{i+1}')
    writer.save()
writer.close()



