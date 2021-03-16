import requests
from bs4 import BeautifulSoup
import pandas as pd

#site
html = 'https://pl.wikipedia.org/wiki/Wroc%C5%82aw'
downloaded_html = requests.get(html)
soup_html = BeautifulSoup(downloaded_html.text)

#table
table_full = soup_html.select('div > table:nth-child(369)')[0]

#head
table_columns = []
for element in table_full.select('tr th'):
    col_elem = element.text.strip()
    table_columns.append(col_elem)

table_content = []
for index, values in enumerate(table_full.select('tr')):
    if index > 0:
        table_row = []
        for value in values.select('td'):
            table_row.append(value.text.strip())
        table_content.append(table_row)

df = pd.DataFrame(table_content, columns=table_columns)
print(df)