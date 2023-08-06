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
from _ast import TryExcept
from http.client import EXPECTATION_FAILED
lib_path = os.path.abspath('../all')
sys.path.append(lib_path)

from SetupTest import *
import unittest

class TestCredit(unittest.TestCase):
    
    def testSimpleCreditWithCard(self):
        credit = litleXmlFields.credit()
        credit.amount = 106
        credit.orderId = "12344"
        credit.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        credit.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(credit)
        self.assertEqual("Approved", response.message)

    def testSimpleCreditWithPaypal(self):
        credit = litleXmlFields.credit()
        credit.amount = 106
        credit.orderId = "123456"
        credit.orderSource = 'ecommerce'
        
        paypal = litleXmlFields.payPal()
        paypal.payerId = "1234"
        credit.paypal = paypal
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(credit)
        self.assertEqual("Approved", response.message)
        
    def testSimpleCreditWithCardAndSecondaryAmount(self):
        credit = litleXmlFields.credit()
        credit.amount = 106
        credit.secondaryAmount = 10
        credit.orderId = "12344"
        credit.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        credit.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(credit)
        self.assertEqual("Approved", response.message)
        
    def testsimpleCreditWithTxnAndSecondaryAmount(self):
        credit = litleXmlFields.credit()
        credit.amount = 106
        credit.secondaryAmount = 10
        credit.orderId = "12345"
        credit.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        credit.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(credit)
        self.assertEqual("Approved", response.message)
        
    def simpleCreditConflictWithTxnAndOrderId(self):
        credit = litleXmlFields.credit()
        credit.orderId = "12344"
        credit.amount = 106
        credit.secondaryAmount = 10
        credit.litleTxnId = "12345"
        
        litleXml =  litleOnlineRequest(config)
        try:
            response = litleXml.sendRequest(credit)
            self.fail("Litle Txn and Order Id should conflict, fail to throw a exception")
        except Exception:
            self.assertTrue(response.message.startswith("Error validating xml data against the schema"),"Error in validating")        

    def testPaypalNotes(self):
        credit = litleXmlFields.credit()
        credit.amount = 106
        credit.orderId = "12344"
        credit.payPalNotes = "Hello"
        credit.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        credit.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(credit)
        self.assertEqual("Approved", response.message)

    def testProcessingInstructionAndAmexData(self):
        credit = litleXmlFields.credit()
        credit.amount = 2000
        credit.orderId = "12344"
        credit.orderSource = 'ecommerce'
        
        pI = litleXmlFields.processingInstructions()
        pI.bypassVelocityCheck = True
        credit.processingInstructions = pI
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        credit.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(credit)
            
        self.assertEqual("Approved", response.message)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCredit)
    return suite

if __name__ =='__main__':
    unittest.main()