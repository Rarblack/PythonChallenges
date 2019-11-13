import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":

    # Specify url
    url = input()

    # Package the request, send the request and catch the response
    r = requests.get(url)

    # Extract the response as html
    html_doc = r.text

    # Create a BeautifulSoup object from the HTML
    soup = BeautifulSoup(html_doc, "html.parser")

    # Find amount of followers
    followers = soup.select_one('.ProfileNav-item--followers .ProfileNav-stat .ProfileNav-value').get_text(strip=True)

    # Print followers
    print(followers)