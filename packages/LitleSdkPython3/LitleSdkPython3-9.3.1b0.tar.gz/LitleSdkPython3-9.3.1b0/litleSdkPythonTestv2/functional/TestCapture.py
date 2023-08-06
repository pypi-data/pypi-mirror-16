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

class TestCapture(unittest.TestCase):
    
    def testSimpleCapture(self):
        Capture = litleXmlFields.capture()
        Capture.litleTxnId = 123456000
        Capture.amount = 106
        Capture.payPalNotes = "Notes"
    
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(Capture)
            
        self.assertEqual("Approved",response.message)
        
    def testSimpleCaptureWithPartial(self):
        Capture = litleXmlFields.capture()
        Capture.litleTxnId = 123456000
        Capture.amount = 106
        Capture.partial = True
        Capture.payPalNotes = "Notes"
    
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(Capture)
            
        self.assertEqual("Approved",response.message)
        
    def testComplexCapture(self):
        Capture = litleXmlFields.capture()
        Capture.litleTxnId = 123456000
        Capture.amount = 106
        Capture.payPalNotes = "Notes"
        
        enhanced = litleXmlFields.enhancedData()
        enhanced.customerReference = "Litle"
        enhanced.salesTax = 50
        enhanced.deliveryType = "TBD"
        Capture.enhancedData = enhanced
        
        Capture.payPalOrderComplete = True
    
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(Capture)
            
        self.assertEqual("Approved",response.message)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCapture)
    return suite

if __name__ =='__main__':
    unittest.main()