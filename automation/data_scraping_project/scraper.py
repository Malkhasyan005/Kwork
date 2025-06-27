from bs4 import BeautifulSoup
import pandas as pd
import os

file_path = "index.html"

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

data = []

products = soup.find_all('div', class_='product')
for product in products:
    name = product.find('h2').text.strip()
    price = product.find('span', class_='price').text.strip()
    data.append({'Name': name, 'Price': price})

df = pd.DataFrame(data)

if not os.path.exists("output"):
    os.makedirs("output")

df.to_csv("output/products_data.csv", index=False)
print("Data has been saved to output/products_data.csv")
