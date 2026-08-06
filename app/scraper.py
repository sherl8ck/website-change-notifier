import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    """
    Downloads the webpage HTML.
    """
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    return response.text


def parse_notices(html):
    """
    Extracts admission notices from the University of Allahabad notice table.
    """
    soup = BeautifulSoup(html, "html.parser")
    notices = []

    # Get all tables on the page
    tables = soup.find_all("table")

    # The admission notice table is the second table
    if len(tables) < 2:
        return notices

    table = tables[1]

    rows = table.find_all("tr")

    # Skip the header row
    for row in rows[1:]:
        cols = row.find_all("td")

        if len(cols) < 3:
            continue

        date = cols[0].get_text(strip=True)
        title = cols[1].get_text(" ", strip=True)

        # Get the notice link if available
        link = ""
        a = cols[2].find("a")
        if a and a.get("href"):
            link = a["href"]

            # Convert relative URL to absolute URL
            if link.startswith("/"):
                link = "https://allduniv.ac.in" + link

        notices.append({
            "date": date,
            "title": title,
            "link": link
        })

    return notices