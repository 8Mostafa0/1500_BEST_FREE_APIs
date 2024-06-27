from bs4 import BeautifulSoup


def get_data():
    file_path = "web.htm"

    # Open the file and read its contents
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the div with the class 'container'
    all_divs = soup.find("div", class_="flex flex-none justify-center bg-gray-300")

    data = []

    for elm in all_divs.contents:
        category = ""
        for e in elm.contents:
            title = ""
            link = ""
            disc = ""
            if e.name == "div":
                category = e.contents[0].text
            elif e.name == "a":
                title = e.contents[0].contents[0].text
                disc = e.contents[0].contents[1].text
                link = e['href']

            data.append([title,link,disc,category])
    return data

