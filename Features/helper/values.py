"""
This simple file hides the elements and urls used in the project

"""
# The parent url where all the fun happens
#-----------------------------------------------------------------------------------------------------------#

parent_url = "https://www.amazon.com/"

# The selector elements used on the site, some are ids, while others are css selectors
#-----------------------------------------------------------------------------------------------------------#

# The selector elements used when searching
#-----------------------------------------------------------------------------------------------------------#

search_word = "hindemith cardillac"
search_box = "twotabsearchtextbox"
search_btn = "nav-input"

# The selector elements used when selecting item and trying to verify some elements before adding to cart
#-----------------------------------------------------------------------------------------------------------#

item_link = "div.sg-col-20-of-24:nth-child(3) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1) > a:nth-child(1) > span:nth-child(1)"
ratings = "ratings"
reviews = "averageCustomerReviews"
cart_btn = "add-to-cart-button-ubb"

# The checkout phase
#-----------------------------------------------------------------------------------------------------------#

checkout_btn = "hlb-ptc-btn-native"

# The new url expected, which should display the sign in or sign up option
#-----------------------------------------------------------------------------------------------------------#

new_url = "https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=amazon_checkout_" \
          "us&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=" \
          "http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=" \
          "http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2" \
          "Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2" \
          "Fgp%2Fbuy%2Fsignin%2Fhandlers%2Fcontinue.html%3Fie%3DUTF8%26brandId%3D%26cartItemIds%3D%26eGCApp%" \
          "3D%26hasWorkingJavascript%3D0%26isEGCOrder%3D0%26isFresh%3D0%26oldCustomerId%3D%26oldPurchaseId%" \
          "3D%26preInitiateCustomerId%3D%26purchaseInProgress%3D%26ref_%3Dcart_signin_submit%26siteDesign%" \
          "3D&pageId=amazon_checkout_us&showRmrMe=0&siteState=isRegularCheckout.1%7CIMBMsgs.%7CisRedirect.0"

