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

class TestEcheckSale(unittest.TestCase):
    
    def testSimpleEcheckSaleWithEcheck(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.amount = 123456
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum ="123455"
        echecksale.echeckOrEcheckToken = echeck
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echecksale)
        self.assertEqual("Approved",response.message)

    def testNoAmount(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        
        litle = litleOnlineRequest(config)
        with self.assertRaises(Exception):
            litle.sendRequest(echecksale)

    def testEcheckSaleWithShipTo(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.amount = 123456
        echecksale.verify = True
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum ="123455"
        echecksale.echeckOrEcheckToken = echeck
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact
        echecksale.shipToAddress = contact
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echecksale)
        self.assertEqual("Approved",response.message)
      
    def testEcheckSaleWithEcheckToken(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.amount = 123456
        echecksale.verify = True
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
        
        token = litleXmlFields.echeckToken()
        token.accType = 'Checking'
        token.litleToken = "1234565789012"
        token.routingNum = "123456789"
        token.checkNum ="123455"
        echecksale.echeckOrEcheckToken = token
        
        custombilling = litleXmlFields.customBilling()
        custombilling.phone = "123456789"
        custombilling.descriptor = "good"
        echecksale.customBilling = custombilling
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echecksale)
        self.assertEqual("Approved",response.message)
        
    def testEcheckSaleWithSecoundaryAmountAndCCD(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.amount = 123456
        echecksale.secondaryAmount = 10
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
        
        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum ="123455"
        echeck.ccdPaymentInformation = "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
        echecksale.echeckOrEcheckToken = echeck
        
        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echecksale)
        self.assertEqual("Approved",response.message)

    def testEcheckSaleMissingBilling(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.amount = 123456
        
        token = litleXmlFields.echeckTokenType()
        token.accType = 'Checking'
        token.litleToken = "1234565789012"
        token.routingNum = "123456789"
        token.checkNum ="123455"
        echecksale.echeckToken = token
        
        echecksale.verify = True
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'
        
        litle = litleOnlineRequest(config)
        with self.assertRaises(Exception):
            litle.sendRequest(echecksale)

    def testSimpleEcheckSale(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.litleTxnId = 123456789101112
        echecksale.amount = 12
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(echecksale)
        self.assertEqual("Approved",response.message)
        
    def testEcheckSaleWithLitleTxnIdAndSecondryAmount(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.litleTxnId = 123456789101112
        echecksale.amount = 12
        echecksale.secondaryAmount = 10
        
        litleXml =  litleOnlineRequest(config)
        with self.assertRaises(Exception):
            response = litleXml.sendRequest(echecksale)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEcheckSale)
    return suite

if __name__ =='__main__':
    unittest.main()