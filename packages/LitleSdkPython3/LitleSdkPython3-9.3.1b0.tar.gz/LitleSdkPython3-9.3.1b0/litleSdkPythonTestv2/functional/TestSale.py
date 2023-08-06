#Copyright (c) 2011-2012 Litle & Co.
#
#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

import os, sys
lib_path = os.path.abspath('../all')
sys.path.append(lib_path)

from SetupTest import *
import unittest

class TestSale(unittest.TestCase):
    
    def testSimpleSaleWithCard(self):
        sale = litleXmlFields.sale()
        sale.litleTxnId = 123456
        sale.amount = 106
        sale.orderId = '12344'
        sale.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        sale.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEqual("Transaction Received",response.message)
        
    def testSimpleSaleWithPayPal(self):
        sale = litleXmlFields.sale()
        sale.litleTxnId = 123456
        sale.amount = 106
        sale.orderId = '12344'
        sale.orderSource = 'ecommerce'
        
        paypal = litleXmlFields.payPal()
        paypal.payerId = "1234"
        paypal.token = "1234"
        paypal.transactionId = "123456"
        sale.paypal = paypal
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEqual("Approved",response.message)

    def testSimpleSaleWithToken(self):
        sale = litleXmlFields.sale()
        sale.amount = 106
        sale.orderId = '12344'
        sale.orderSource = 'ecommerce'
        token = litleXmlFields.cardTokenType()
        token.cardValidationNum = '349'
        token.expDate = '1214'
        token.litleToken = '1111222233334000'
        token.type = 'VI'
        sale.token = token

        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEqual("Approved",response.message)
        
    def testSimpleSaleWithSecondaryAmountAndApplepay(self):
        sale = litleXmlFields.sale()
        sale.litleTxnId = 123456
        sale.amount = 106
        sale.secondaryAmount = 10
        sale.orderId = '12344'
        sale.orderSource = 'ecommerce'
        
        applepay = litleXmlFields.applepayType()
        applepay.data = "4100000000000000"
        applepay.signature = "sign"
        applepay.version = '1'
        header=litleXmlFields.applepayHeaderType()
        header.applicationData='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        header.ephemeralPublicKey ='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        header.publicKeyHash='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        header.transactionId='1024'
        applepay.header=header
        sale.applepay = applepay
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(sale)
        self.assertEqual("Approved",response.message)
        self.assertEqual(106,response.applepayResponse.transactionAmount)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSale)
    return suite

if __name__ =='__main__':
    unittest.main()