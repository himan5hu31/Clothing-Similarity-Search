import requests
from bs4 import BeautifulSoup
import openpyxl



def get_data_from_url(URL,HEADERS,filename,mi):

    webpage = requests.get(URL, headers=HEADERS)

    # Create BeautifulSoup object
    soup = BeautifulSoup(webpage.text, "lxml")

    # Find all divs with class="sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right"
    divs = soup.find_all("div", class_="_2B099V")

    # Initialize lists for storing data
    product_names = []
    product_prices = []
    product_ratings = []
    product_links = []

    # Iterate over the divs
    for div in divs:
        # Find the <a> tag with class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"
        product_link_a = div.find("a", class_="IRpwTa")
        product_link = "https://www.flipkart.com" + product_link_a["href"] if product_link_a else ""
        product_name = product_link_a["title"] if product_link else ""

        product_price_span = div.find("div",class_="_30jeq3")
        product_price = product_price_span.text.strip() if product_price_span else ""

        # Append the data to the respective lists
        product_links.append(product_link)
        product_names.append(product_name)
        product_prices.append(product_price)
        product_ratings.append(int(0))


    wb = openpyxl.load_workbook(filename)


    # Select the desired sheet by name
    sheet = wb['Sheet']  # actual sheet name
    ins_row = (len(sheet['B']) + 1 )

    # Write the data
    for i, (name, price, rating, link) in enumerate(zip(product_names, product_prices, product_ratings, product_links), start=2):
        sheet[f"A{i+ins_row}"] = name
        sheet[f"B{i+ins_row}"] = price
        sheet[f"C{i+ins_row}"] = rating
        sheet[f"D{i+ins_row}"] = link


    # print(product_names)
    # Save the Excel file
    wb.save(filename)
    print("---------data saved-------",mi)





HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

for i in range(2,40):
    URL = "https://www.flipkart.com/clothing-and-accessories/bottomwear/pr?sid=clo%2Cvua&p%5B%5D=facets.ideal_for%255B%255D%3DMen&otracker=categorytree&page="+str(i)
    get_data_from_url(URL,HEADERS,"product_data.xlsx",i)
