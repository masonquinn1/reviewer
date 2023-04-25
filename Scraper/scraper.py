# note this code was taken from https://www.geeksforgeeks.org/web-scraping-amazon-customer-reviews/

import requests
from bs4 import BeautifulSoup

# these are the headers for the HTML request
# TODO: look into how we should be making these headers work
HEADERS = ({'User-Agent':
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
			AppleWebKit/537.36 (KHTML, like Gecko) \
			Chrome/90.0.4430.212 Safari/537.36',
			'Accept-Language': 'en-US, en;q=0.5'})

def scrape_amazon(url, custom_headers=None):
    """
    Scrapes the product reviews for an Amazon Listing given the product's URL.
    Parameters:
    url String: the url of the product we want to scrape
    # TODO: add something for custom headers

    Returns:
    Reviews: a list of reviews
    """
    # TODO: there should eventually be checks here that throw if a bad input is introduced, but until then #yolo
    
    # perform the HTTP request and retrieve the website text and code
    html_response = requests.get(url, headers=HEADERS)
    html_text, http_code = html_response.text, html_response.status_code
    # load HTML text into beautiful soup
    soup = BeautifulSoup(html_text, 'html.parser')
    # go through all the reviews with soup.find_all and store the text of each into an array
    review_texts = []
    for item in soup.find_all("div", class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content"):
        text = item.get_text().strip() # item.get_text returns a review along with space before and after
        review_texts.append(text)

    # return the list of reviews
    return review_texts
    


def test():
    url = "https://www.amazon.com/Cedar-EasyWring-Microfiber-Bucket-Refills/dp/B07NDHY41N/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=4xA81&content-id=amzn1.sym.1bcf206d-941a-4dd9-9560-bdaa3c824953&pf_rd_p=1bcf206d-941a-4dd9-9560-bdaa3c824953&pf_rd_r=X4E04DE9FCE9CJ5KJ3W9&pd_rd_wg=7tKOT&pd_rd_r=6aab8415-a945-48d0-b3aa-53ca6137837a&pd_rd_i=B07NDHY41N&th=1"
    scrape_amazon(url)

test()