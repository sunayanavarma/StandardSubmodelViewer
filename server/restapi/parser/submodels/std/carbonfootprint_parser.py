'''
Created on 4 Jul 2024

@author: pakala
'''

class CarbonFootPrintParser:
    def __init__(self,std_submodel):
        self.data = std_submodel
        self.carbonFootPrintData = dict()


    def get_mlp_data(self,mlp):
        try:
            return mlp["value"][0]["text"]
        except:
            return         
    
    def parse(self):
        ProductCarbonFootprint = dict()
        TransportCarbonFootprint = dict()
        for sme in self.data["submodelElements"]:
            if sme["idShort"] == "ProductCarbonFootprint":
                for pcfe in sme["value"]:
                      
                    if  pcfe["idShort"] == "PCFGoodsAddressHandover":
                        PCFGoodsAddressHandover = dict()
                        for pcfgah in pcfe["value"]:
                            PCFGoodsAddressHandover[pcfgah["idShort"]] = pcfgah["value"]
                    
                        ProductCarbonFootprint["PCFGoodsAddressHandover"] = PCFGoodsAddressHandover
 
                    else:
                        ProductCarbonFootprint[pcfe["idShort"]] = pcfe["value"]
 
                        
            if sme["idShort"] == "TransportCarbonFootprint":
                for tcfe in sme["value"]:
                
                    if tcfe["idShort"] == "TCFGoodsTransportAddressTakeover":
                        TCFGoodsTransportAddressTakeover = dict()
                        for tcfgtat in tcfe["value"]:
                            TCFGoodsTransportAddressTakeover[tcfgtat["idShort"]] = tcfgtat["value"]
                    
                            TransportCarbonFootprint["TCFGoodsTransportAddressTakeover"] = TCFGoodsTransportAddressTakeover
                        
                    elif tcfe["idShort"] == "TCFGoodsTransportAddressHandover":
                        TCFGoodsTransportAddressHandover = dict()
                        for tcfgtat in tcfe["value"]:
                            TCFGoodsTransportAddressHandover[tcfgtat["idShort"]] = tcfgtat["value"]
                    
                        TransportCarbonFootprint["TCFGoodsTransportAddressHandover"] = TCFGoodsTransportAddressHandover
                
                        
                    else:
                        TransportCarbonFootprint[tcfe["idShort"]] = tcfe["value"]
                
        
                        self.carbonFootPrintData["ProductCarbonFootprint"] = ProductCarbonFootprint
                        self.carbonFootPrintData["TransportCarbonFootprint"] = TransportCarbonFootprint
        
                        print(json.dumps(self.carbonFootPrintData, indent=4))
import json
'''
           
f = open('IDTA 2023-0-9 _Template_CarbonFootprint.json')
data = json.load(f)
cfp = CarbonFootPrintParser(data)
cfp.parse()
'''