#
# Copyright (c) 2016 MasterCard International Incorporated
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of
# conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of
# conditions and the following disclaimer in the documentation and/or other materials
# provided with the distribution.
# Neither the name of the MasterCard International Incorporated nor the names of its
# contributors may be used to endorse or promote products derived from this software
# without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#

import unittest
from mastercardapicore import RequestMap, Config, OAuthAuthentication
from os.path import dirname, realpath, join
from mastercardlocations import *


class ATMCountrySubdivisionsTest(unittest.TestCase):

    def setUp(self):
        keyFile = join(dirname(realpath(__file__)),"resources","mcapi_sandbox_key.p12")
        auth = OAuthAuthentication("L5BsiPgaF-O3qA36znUATgQXwJB6MRoMSdhjd7wt50c97279!50596e52466e3966546d434b7354584c4975693238513d3d",keyFile, "alias", "password")
        Config.setAuthentication(auth)
        Config.setDebug(True)

    
        
        
        
        
        
        
                
    def test_example_atm_countrysubdivision(self):
        mapObj = RequestMap()
        mapObj.set("Country", "USA")
        
        response = ATMCountrySubdivisions.query(mapObj)
        self.customAssertValue("ARMED FORCES AMERICAS", response.get("CountrySubdivisions.CountrySubdivision[0].Name"))
        self.customAssertValue("AA", response.get("CountrySubdivisions.CountrySubdivision[0].Code"))
        self.customAssertValue("ARMED FORCES CAN AFRICA E", response.get("CountrySubdivisions.CountrySubdivision[1].Name"))
        self.customAssertValue("AE", response.get("CountrySubdivisions.CountrySubdivision[1].Code"))
        self.customAssertValue("ALASKA", response.get("CountrySubdivisions.CountrySubdivision[2].Name"))
        self.customAssertValue("AK", response.get("CountrySubdivisions.CountrySubdivision[2].Code"))
        
    
        
    

    def customAssertValue(self,expected,actual):
        if (isinstance(actual,float)):
            self.assertEqual(float(expected), actual)
        else:
            self.assertEqual(expected.lower(), str(actual).lower())


if __name__ == '__main__':
    unittest.main()

