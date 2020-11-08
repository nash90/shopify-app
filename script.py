import os
import requests
from search_script import getBestSellerHtml
import json

PRIVATE_API_KEY = os.environ['PRIVATE_API_KEY']
PRIVATE_API_PASSWORD = os.environ['PRIVATE_API_PASSWORD']


def getSopifyProduct(id=5877039005852): 
    product = shopify.Product.find(id)


def postPage(page_id=69541986460, html=""):
    html = getBestSellerHtml()
    url = "https://%s:%s@yamanocity.myshopify.com/admin/api/2020-10/pages/%s.json" % (PRIVATE_API_KEY, PRIVATE_API_PASSWORD, page_id)
    data = {
      "page": {
        "id": page_id,
        "body_html": html
      }
    }

    r = requests.put(url, json = data)

    print(r)
    return r




