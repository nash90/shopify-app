import requests
import json

# set up the request parameters

RAINFOREST_APT_KEY = "2CE831533C4C4A258AFFC584C09F93E6"

def getBestSellers(url):
    if url is None:
        url = "https://www.amazon.com/Best-Sellers-Womens-Handbags-Purses-Wallets/zgbs/fashion/15743631"

    params = {
      'api_key': RAINFOREST_APT_KEY,
      'type': 'bestsellers',
      'url': url
    }

    # make the http GET request to Rainforest API
    api_results = requests.get('https://api.rainforestapi.com/request', params)
    json_obj = api_results.json()
    # print the JSON response from Rainforest API
    #print(json.dumps(api_result.json()))
    return json_obj["bestsellers"]

card_html = """
		<li class="grid__item grid__item--collection-template small--one-half medium-up--one-half">
			<h4>{{{CARD_TITLE}}}</h4>
			<a href="{{{ITEM_LINK}}}" target="_blank">
        <img border="0" src="{{{ITEM_IMAGE}}}" >
      </a>
      <img src="https://ir-na.amazon-adsystem.com/e/ir?t=yamacity-20&language=en_US&l=li3&o=1&a=B082B1CZ7P" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
		</li>
"""

body_html = """
<div class="page-width" id="Collection">
	<ul class="grid grid--uniform grid--view-items">
  {{{ITEM_LISTS}}}
  </ul>
</div>
"""

def getBestSellerHtml(url=None, site="en"):

    aff_tag = "&tag=yamacity-20"
    
    if site == "jp":
       aff_tag = "&tag=yamacity-20"

    bestseller = getBestSellers(url)

    item = bestseller[0]

    carditems = ""
    for item in bestseller:

      carditem = card_html.replace("{{{CARD_TITLE}}}", item["title"])
      carditem = carditem.replace("{{{ITEM_LINK}}}", item["link"]+aff_tag)
      carditem = carditem.replace("{{{ITEM_IMAGE}}}", item["image"])

      carditems = carditems + carditem

    body = body_html.replace("{{{ITEM_LISTS}}}", carditems)

    print(body)
    return body