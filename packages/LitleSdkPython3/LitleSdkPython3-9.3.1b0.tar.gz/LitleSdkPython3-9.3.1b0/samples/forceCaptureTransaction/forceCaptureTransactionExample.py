from litleSdkPython.litleOnlineRequest import *
 
config = Configuration()
config.username="jenkins"
config.password="certpass"
config.merchantId="0180"
config.url="Sandbox"
config.proxy="iwp1.lowell.litle.com:8080"
 
#Force Capture
forcecapture = litleXmlFields.forceCapture()
forcecapture.reportGroup = "Planets"
forcecapture.litleTxnId = "123456"
forcecapture.amount = 106
forcecapture.orderId = '12344'
forcecapture.orderSource = 'ecommerce'
        
card = litleXmlFields.cardType()
card.type = 'VI'
card.number = "4100000000000001"
card.expDate = "1210"
forcecapture.card = card
        
litleXml =  litleOnlineRequest(config)
response = litleXml.sendRequest(forcecapture)
 
#display results
print("Response: " + response.response)
print("Message: " + response.message)
print("LitleTransaction ID: " + str(response.litleTxnId))

if response.response != "000":
        raise Exception("Invalid response")
