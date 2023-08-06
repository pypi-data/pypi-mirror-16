from litleSdkPython.litleOnlineRequest import *
 
config = Configuration()
config.username="jenkins"
config.password="certpass"
config.merchantId="0180"
config.url="Sandbox"
config.proxy="iwp1.lowell.litle.com:8080"
 
#refund
credit = litleXmlFields.credit()
credit.amount = 106
credit.orderId = "1"
credit.amount = 10010
credit.orderSource = 'ecommerce'
billToAddress = litleXmlFields.contact()
billToAddress.name = "John Smith"
billToAddress.addressLine1 = "1 Main St."
billToAddress.city = "Burlington"
billToAddress.state = "MA"
billToAddress.country = "US"
billToAddress.zip = "01803-3747"
credit.billToAddress = billToAddress
card = litleXmlFields.cardType()
card.type = 'AX'
card.number = "375001010000003"
card.expDate = "0112"
credit.card = card
 
litleXml = litleOnlineRequest(config)
response = litleXml.sendRequest(credit)
 
#display results
print("Response: " + response.response)
print("Message: " + response.message)
print("LitleTransaction ID: " + str(response.litleTxnId))

if response.response != "000":
        raise Exception("Invalid  response")
