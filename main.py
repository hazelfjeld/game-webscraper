import requests
from bs4 import BeautifulSoup

steam_price=[]


def search(search,platform):
    global steam_price
    
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    if platform == "steam":
        steam_price=[]
        url = f"https://store.steampowered.com/search/?term={search}"
    """
    expandable by adding;
    elif platform == "platformName":
      platform_price=[]
      url= platformURL
    """
    
    html = requests.get(url, headers=headers).text

    results = BeautifulSoup(html, "html.parser")

    search_row = results.find_all("a", class_="search_result_row")
    titles=results.find_all("span", class_="title")
    top3=3
    


    for item in search_row:
        if top3>0: # To only show top 3 results
            top3-=1
            price_div=price_div = item.find("div", class_="search_price") or item.find("div", class_="discount_final_price")

            price=price_div.text.strip() if price_div else "Price not found!"
            title_div=item.find("span", class_="title") or item.find("span", class_="aria-title")
            title=title_div.text.strip() if title_div else "Title not found"
            if platform == "steam":
                steam_price.append(("Steam",title,price))

    


def main():
    game_search=str(input("What would you like to search for?: "))
    search(game_search,"steam")
    print(steam_price)

main()
