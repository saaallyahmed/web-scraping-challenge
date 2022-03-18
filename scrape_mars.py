# importing all required libraries
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import time

def scrape_info():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome''', **executable_path, headless=False)

    #Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(3)

    #NASA Mars News
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find_all('div', class_='content_title')[0].text
    news_p = soup.find_all ('div', class_= 'article_teaser_body')[0].text

    #JPL Mars Space Images
    #featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
    url ="https://spaceimages-mars.com/image/featured/mars3.jpg"
    browser.visit(url)
    html = browser.html
    time.sleep(1)
    soup = BeautifulSoup(html, 'html.parser')
    for div in soup.find_all('div', class_='floating_text_area'):
        a = div.find('a')
        image = a['href']
        print(image)
    Featured_image_url = 'https://spaceimages-mars.com/image/featured/mars3.jpg'

    print(f"Featured_image_url = {Featured_image_url}")
    url = 'https://marshemispheres.com/'

    #Mars Facts 
    df = pd.read_html('https://galaxyfacts-mars.com')[0]
    df.head()

    
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(1)
    
    results = soup.find_all('div', class_='description')
    Hemisphere_img_urls = []
    # Loop through returned results
    for result in results:
        # Error handling
        try:
            # Identify and return title of listing
            title = result.find('h3').text
            # get the image link
            img_link = result.a['href']
            url = f"https://marshemispheres.com/" + img_link
            browser.visit(url)
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            output = soup.find('img', class_= "wide-image")
            download_link = output['src']
            img_url = f"https://marshemispheres.com/" + download_link
                # Print results only if title, price, and link are available

            if (title and download_link):
                print(title)
                print(f"https://marshemispheres.com/" + download_link)
                print('-'*107)
                
                hemis_dictionary = { 
                    'Title' :title, 
                    'img_url': img_url}
                
                Hemisphere_img_urls.append(hemis_dictionary)
                
        except Exception as e:
            print(e)
    scraped_info = {
        'news_title': news_title,
        'news': news_p,
        'url_featured_image': Featured_image_url,
        'mars_facts': df.to_html(index = False),
        'hemisphere': Hemisphere_img_urls
    }
    browser.quit()
    return scraped_info
if __name__ == "__main__":
    
    # If running as script, print scraped data
    print(scrape_info())