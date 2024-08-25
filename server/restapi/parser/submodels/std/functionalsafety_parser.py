'''
Created on 8 Jul 2024

@author: pakala
'''
       
class FunctionalSafetyParser:
    def __init__(self,std_submodel):
        self.data = std_submodel
        self.FunctionalSafetyData = dict()

    def get_mlp_data(self,mlp):
        try:
            return mlp["value"][0]["text"]
        except:
            return
        
    def parse(self):
        for submodelElement in self.data["submodelElements"]:
            if (submodelElement["idShort"]) == "NumberOfFunctionalSafetySetsOfCharacteristics":
                self.FunctionalSafetyData["NumberOfFunctionalSafetySetsOfCharacteristics"] = submodelElement["value"]
                    
            elif (submodelElement["idShort"]) == "OperatingConditionsOfFunctionalSafetyCharacteristics":                            
                OperatingConditionsOfFunctionalSafetyCharacteristics = dict()
                for ocfsc in submodelElement["value"]:
                    OperatingConditionsOfFunctionalSafetyCharacteristics[ocfsc["idShort"]] = ocfsc["value"]
                self.FunctionalSafetyData["OperatingConditionsOfFunctionalSafetyCharacteristics"] = OperatingConditionsOfFunctionalSafetyCharacteristics
                    
            elif (submodelElement["idShort"]) == "SafetyDeviceTypes":
                SafetyDeviceTypes = dict()
                for sdtElem in submodelElement["value"]:
                    if sdtElem["idShort"] == "SafetySubsystem":
                        SafetySubsystem = dict()
                        for ssElem in sdtElem["value"]:
                            SafetySubsystem[ssElem["idShort"]] = ssElem["value"]
                                
                        SafetyDeviceTypes["SafetySubsystem"] = SafetySubsystem
                                
                    elif sdtElem["idShort"] == "ElectronicElement":
                        ElectronicElement = dict()
                        for eeElem in sdtElem["value"]:
                            ElectronicElement[eeElem["idShort"]] = eeElem["value"]       
                                
                        SafetyDeviceTypes["ElectronicElement"] = ElectronicElement
                                            
                    elif sdtElem["idShort"] == "ElectromechanicalElement":
                        ElectromechanicalElement = dict()
                        for emeElem in sdtElem["value"]:
                            ElectromechanicalElement[emeElem["idShort"]] = emeElem["value"]
                                    
                        SafetyDeviceTypes["ElectromechanicalElement"] = ElectromechanicalElement
                            
                    elif sdtElem["idShort"] == "InherentlySafeSubsystem":
                        InherentlySafeSubsystem = dict()
                        for isElem in sdtElem["value"]:
                            InherentlySafeSubsystem[isElem["idShort"]] = isElem["value"]         
                    
                        SafetyDeviceTypes["InherentlySafeSubsystem"] = InherentlySafeSubsystem
                                
                    elif sdtElem["idShort"] == "FunctionalSafetyDeviceType":
                        SafetyDeviceTypes["FunctionalSafetyDeviceType"] = sdtElem["value"]
                        
                self.FunctionalSafetyData["SafetyDeviceTypes"] = SafetyDeviceTypes
        
        return self.FunctionalSafetyData    
                        
'''                    
import json           
f = open('IDTA 02014-1-0_Template_FunctionalSafety.json')
data = json.load(f)
fsp = FunctionalSafetyParser(data)
fsp.parse()
'''
                            
                            
