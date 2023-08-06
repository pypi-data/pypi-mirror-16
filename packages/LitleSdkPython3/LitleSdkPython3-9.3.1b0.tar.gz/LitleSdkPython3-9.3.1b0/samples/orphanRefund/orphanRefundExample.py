from litleSdkPython.litleOnlineRequest import *
 
config = Configuration()
config.username="jenkins"
config.password="certpass"
config.merchantId="0180"
config.url="Sandbox"
config.proxy="iwp1.lowell.litle.com:8080"


credit = litleXmlFields.credit()
credit.orderId = "abc123"
credit.amount = 100
credit.orderSource = "ecommerce"
card = litleXmlFields.cardType()
card.number = "4457010000000009"
card.expDate = "0112"
card.cardValidationNum = "349"
card.type = "VI"
credit.card = card
 
litleXml = litleOnlineRequest(config)
response = litleXml.sendRequest(credit)
 
#display results
print("Response: " + response.response)
print("Message: " + response.message)
print("LitleTransaction ID: " + str(response.litleTxnId))

if response.response != "000":
	raise Exception("Incorrect response")
