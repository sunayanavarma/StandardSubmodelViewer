'''
Created on 4 Jul 2024

@author: pakala
'''
from htmlgenerator import render, DIV,H2,BUTTON

class NamePlateParser:
    def __init__(self,std_submodel):
        self.data = std_submodel
        self.nameplateData = dict()

    def get_mlp_data(self,mlp):
        try:
            return mlp["value"][0]["text"]
        except:
            return ""
    
    def get_contact_information(self,submodelElement):
        contactInformation = dict()
        for Addresselement in submodelElement["value"]:
            
            if (Addresselement["idShort"]) == "RoleOfContactPerson":
                contactInformation["RoleOfContactPerson"] = Addresselement["value"]
            
            if (Addresselement["idShort"]) == "NationalCode":
                contactInformation["NationalCode"] = self.get_mlp_data(Addresselement)
                                        
            if (Addresselement["idShort"]) == "Language":
                contactInformation["Language"] = Addresselement["value"]
                                    
            if (Addresselement["idShort"]) == "TimeZone":
                contactInformation["TimeZone"] = Addresselement["value"]
                                        
            if (Addresselement["idShort"]) == "CityTown":
                contactInformation["CityTown"] = self.get_mlp_data(Addresselement)
                                        
            if (Addresselement["idShort"]) == "Company":
                contactInformation["Company"] = self.get_mlp_data(Addresselement)
                                    
            if (Addresselement["idShort"]) == "Department":
                contactInformation["CityTown"] = self.get_mlp_data(Addresselement)
                                        
            if (Addresselement["idShort"]) == "StateCounty":
                contactInformation["StateCounty"] = self.get_mlp_data(Addresselement)
                
                
                                        
            if (Addresselement["idShort"]) == "Street":
                contactInformation["Street"] = self.get_mlp_data(Addresselement)
                                        
            if (Addresselement["idShort"]) == "Zipcode":
                contactInformation["Zipcode"] = self.get_mlp_data(Addresselement)
                                    
            if (Addresselement["idShort"]) == "POBox":
                contactInformation["POBox"] = self.get_mlp_data(Addresselement)
            
            if (Addresselement["idShort"]) == "ZipCodeOfPOBox":
                contactInformation["ZipCodeOfPOBox"] = self.get_mlp_data(Addresselement)
                                        
            if (Addresselement["idShort"]) == "StateCounty":
                contactInformation["StateCounty"] = self.get_mlp_data(Addresselement)
                                    
            if (Addresselement["idShort"]) == "StateCounty":
                contactInformation["StateCounty"] = self.get_mlp_data(Addresselement)
            
            '''    
            if (Addresselement["idShort"]) == "FirstName":
                contactInformation["FirstName"] = self.get_mlp_data(Addresselement)
                                        
            if (Addresselement["idShort"]) == "MiddleNames":
                contactInformation["MiddleNames"] = self.get_mlp_data(Addresselement)
                                    
            if (Addresselement["idShort"]) == "Title":
                contactInformation["Title"] = self.get_mlp_data(Addresselement)
            
            if (Addresselement["idShort"]) == "AcademicTitle":
                contactInformation["AcademicTitle"] = self.get_mlp_data(Addresselement)
                                        
            if (Addresselement["idShort"]) == "FurtherDetailsOfContact":
                contactInformation["FurtherDetailsOfContact"] = self.get_mlp_data(Addresselement)
                                    
            if (Addresselement["idShort"]) == "AddressOfAdditionalLink":
                contactInformation["AddressOfAdditionalLink"] = self.get_mlp_data(Addresselement)
            '''
        return contactInformation

    def get_marking_information(self,markingE):
        marking = dict()  
        for info in markingE["value"]:
            if info["idShort"] != "ExplosionSafeties":
                marking[info["idShort"]] = info["value"] 
            else:
                ExplosionSafeties = dict()
                j = 0
                for explosionSafety in info["value"]:
                    explosionSafetyDict = dict()
                    for safetyElem in explosionSafety["value"]:
                        if safetyElem["modelType"] == "Property":
                            explosionSafetyDict[safetyElem["idShort"]] = safetyElem["value"]
                        elif safetyElem["modelType"] == "MultiLanguageProperty":
                            explosionSafetyDict[safetyElem["idShort"]] = self.get_mlp_data(safetyElem)
                        elif safetyElem["modelType"] == "SubmodelElementCollection":
                            elemDict = dict()
                            for elem in safetyElem["value"]:
                                if elem["modelType"] == "Property":
                                    elemDict[elem["idShort"]] = elem["value"]
                                elif elem["modelType"] == "MultiLanguageProperty":
                                    elemDict[elem["idShort"]] = self.get_mlp_data(elem)
                                
                            explosionSafetyDict[safetyElem["idShort"]] = elemDict
                    ExplosionSafeties["ExplosionSafety"+ str(j)] =  explosionSafetyDict
                marking["ExplosionSafeties"] = ExplosionSafeties
        return marking
      
    def parse(self):
        self.nameplateData["ManufacturerDetails"] = dict()
        self.nameplateData["ProductInformation"] = dict()
        self.nameplateData["Versioning"] = dict()
        for _key,_value in self.data.items():
            if _key == "submodelElements":
                for submodelElement in _value:
                    
                    if (submodelElement["idShort"]) == "ManufacturerName":
                        self.nameplateData["ManufacturerDetails"]["ManufacturerName"]  =submodelElement["value"][0]["text"]
                                
                    if (submodelElement["idShort"]) == "ManufacturerProductDesignation":
                        self.nameplateData["ManufacturerDetails"]["ManufacturerProductDesignation"] = submodelElement["value"][0]["text"]
                            
                    if (submodelElement["idShort"]) == "ManufacturerProductRoot":
                        self.nameplateData["ManufacturerDetails"]["ManufacturerProductRoot"] = submodelElement["value"][0]["text"]
                                
                    if (submodelElement["idShort"]) == "ManufacturerProductFamily":
                        self.nameplateData["ManufacturerDetails"]["ManufacturerProductFamily"] = submodelElement["value"][0]["text"]
                            
                    if (submodelElement["idShort"]) == "ManufacturerProductType":
                        self.nameplateData["ManufacturerDetails"]["ManufacturerProductType"] = submodelElement["value"][0]["text"]
                            
                    if (submodelElement["idShort"]) == "OrderCodeOfManufacturer":
                        self.nameplateData["ManufacturerDetails"]["OrderCodeOfManufacturer"] = submodelElement["value"][0]["text"]
                    
                    if (submodelElement["idShort"]) == "SerialNumber": 
                        self.nameplateData["ManufacturerDetails"]["SerialNumber"] = submodelElement["value"]
                        
                        
                    # Product Details Start
                                
                    if (submodelElement["idShort"]) == "URIOfTheProduct":
                        self.nameplateData["ProductInformation"]["URIOfTheProduct"]  =submodelElement["value"]
                
                    if (submodelElement["idShort"]) == "ProductArticleNumberOfManufacturer":
                        self.nameplateData["ProductInformation"]["ProductArticleNumberOfManufacturer"] = submodelElement["value"][0]["text"]
                            
                    if (submodelElement["idShort"]) == "SerialNumber":
                        self.nameplateData["ProductInformation"]["SerialNumber"] = submodelElement["value"]
                                
                    if (submodelElement["idShort"]) == "YearOfConstruction":
                        self.nameplateData["ProductInformation"]["YearOfConstruction"] = submodelElement["value"]
                            
                    if (submodelElement["idShort"]) == "DateOfManufacture":
                        self.nameplateData["ProductInformation"]["DateOfManufacture"] = submodelElement["value"]
                            
                    if (submodelElement["idShort"]) == "CountryOfOrigin":
                        self.nameplateData["ProductInformation"]["CountryOfOrigin"] = submodelElement["value"]
                                
                    if (submodelElement["idShort"]) == "CompanyLogo":
                        self.nameplateData["ProductInformation"]["CompanyLogo"] = submodelElement["value"]    
                                
                    # Product Details End
                    
                    # Contact Information Start    
                    
                    if (submodelElement["idShort"]) == "ContactInformation":
                        self.nameplateData["ContactInformation"] = self.get_contact_information(submodelElement) 
                        
                    # Contact Information End  
                        
                    # Versioning Details Start
                                
                    if (submodelElement["idShort"]) == "HardwareVersion":
                        self.nameplateData["Versioning"]["HardwareVersion"]  =submodelElement["value"][0]["text"]
                
                    if (submodelElement["idShort"]) == "FirmwareVersion":
                        self.nameplateData["Versioning"]["FirmwareVersion"] = submodelElement["value"][0]["text"]
                            
                    if (submodelElement["idShort"]) == "SoftwareVersion":
                        self.nameplateData["Versioning"]["SoftwareVersion"] = submodelElement["value"][0]["text"]
                                
                    # Versioning Details End    
                        
                    # Markings Information Start    
                    
                    if (submodelElement["idShort"]) == "Markings":
                        for marking in submodelElement["value"]:
                            self.nameplateData[marking["idShort"]] = self.get_marking_information(marking) 
                        
                    # Markings Information End
                    
                    # Asset Specific Properties start
                    '''
                    if (submodelElement["idShort"]) == "AssetSpecificProperties":
                        for AssetSpecificProperties in submodelElement["value"]:
                            nameplateData[AssetSpecificProperties["idShort"]] = get_AssetSpecificProperties_information(AssetSpecificProperties)
                    '''        
                    # Asset Specific Properties End
            