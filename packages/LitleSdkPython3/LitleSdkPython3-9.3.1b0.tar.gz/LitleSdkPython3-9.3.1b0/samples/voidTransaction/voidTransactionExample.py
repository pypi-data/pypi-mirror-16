from litleSdkPython.litleOnlineRequest import *
 
config = Configuration()
config.username="jenkins"
config.password="certpass"
config.merchantId="0180"
config.url="Sandbox"
config.proxy="iwp1.lowell.litle.com:8080"
 
#Void
void = litleXmlFields.void()
void.litleTxnId = 100000000000000001
 
litleXml = litleOnlineRequest(config)
response = litleXml.sendRequest(void)
#display results
print("Response: " + response.response)
print("Message: " + response.message)
print("LitleTransaction ID: " + str(response.litleTxnId))

if response.response != "000":
        raise Exception("Invalid  response")
