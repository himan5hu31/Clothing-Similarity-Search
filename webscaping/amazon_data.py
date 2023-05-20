
import requests
from bs4 import BeautifulSoup
import openpyxl
from function_amazon import get_data_from_url



HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


URL = "https://www.amazon.com/s?k=men+fashion&i=fashion-mens&rh=n%3A7141123011%2Cn%3A7147441011%2Cn%3A1040658&dc&page=2&crid=1DVUGE5NG5UUO&qid=1684424602&rnid=7141123011&sprefix=menfashion%2Caps%2C282&ref=sr_pg_2"
webpage = requests.get(URL, headers=HEADERS)


# Create BeautifulSoup object
soup = BeautifulSoup(webpage.text,  "html.parser")


links=[]
n = 100
while n > 0:
    n -= 1
    # Find the div with class="a-section a-spacing-none s-result-item s-flex-full-width s-widget s-widget-spacing-large"
    div = soup.find("div", class_="a-section a-text-center s-pagination-container")
    a_tag = div.find("a",class_="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator")
    cnp="https://www.amazon.com"+str(a_tag["href"])
    print(cnp)
    get_data_from_url(cnp,HEADERS,"product_data.xlsx")
  
    url=cnp
    r=requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(r.text,"html.parser")
    links.append(cnp)

# Create a new Excel file
wb = openpyxl.Workbook()
sheet = wb.active

# Write the headers
sheet["A1"] = "page link"


# Write the data
for i, (link) in enumerate(links, start=2):
    sheet[f"A{i}"] = link

# Save the Excel file
wb.save("page_link.xlsx")



