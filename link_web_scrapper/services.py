import requests
from bs4 import BeautifulSoup

from link_web_scrapper.models import ScrappedLink


def scrap_website(webpage):
    # Receives a WebPage Object.
    print("-------------------------")
    print(webpage.name)
    response = requests.get(webpage.link)
    website_html = response.content
    soup = BeautifulSoup(website_html, 'html.parser')
    title_tag = soup.find('title')
    print(title_tag)
    all_links = soup.find_all('a')
    for link in all_links:
        href = link.get('href')
        content = link.string
        if ScrappedLink.validate_link(href) and content:
            print(f"href: {href}")
            print(f"content: {content}")
            ScrappedLink.objects.create(webpage=webpage, url_name=content, link=href)

    if title_tag:
        webpage.name = title_tag.text
        print(f"title_tag: {title_tag}")
    webpage.state = "scrapped"
    webpage.save()
