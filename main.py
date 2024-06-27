import requests
from bs4 import BeautifulSoup

file_path = "web.htm"

# Open the file and read its contents
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the <a> tags with the speci"rounded-lg bg-gray-200 p-4 m-3 shadow-lg break-words w-72 hover:shadow-xl hover:bg-gray-100 flex flex-col justify-between
api_links = soup.find_all("a", class_="rounded-lg bg-gray-200 p-4 m-3 shadow-lg break-words w-72 hover:shadow-xl hover:bg-gray-100 flex flex-col justify-between")
titles = soup.find_all("div", class_="text-2xl text-gray-900 font-bold pb-2")


data = []

# Extract the text content and URLs of the API links
for i in range(0,len(api_links)):
    api_name = api_links[i].get_text(strip=True)
    api_url = api_links[i]["href"]
    title = titles[i].get_text(strip=True)
    data.append([title,api_name,api_url])



print(len(data))