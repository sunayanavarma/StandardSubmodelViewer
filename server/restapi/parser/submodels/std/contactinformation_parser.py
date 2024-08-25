'''
Created on 4 Jul 2024

@author: pakala
'''
class ContactInformationParser:
    def __init__(self,std_submodel):
        self.data = std_submodel
        self.ContactInformationSubmodelData = dict()

    def get_mlp_data(self,mlp):
        try:
            return mlp["value"][0]["text"]
        except:
            return ""
    
    def getElemValue(self,elem):
        if elem["modelType"] == "Property":
            return elem["value"]
        elif elem["modelType"] == "MultiLanguageProperty":
            return self.get_mlp_data(elem)
        elif elem["modelType"] == "SubmodelElementCollection":
            elementCollectionDict = dict()
            for elemC in elem["value"]:
                elementCollectionDict[elemC["idShort"]] = self.getElemValue(elemC)
            return elementCollectionDict
        
    def parse(self):
        try:
            for submodelElem in self.data["submodelElements"]:
                ContactInformationDict = dict()
                for contactInformation in submodelElem["value"]:
                    ContactInformationDict[contactInformation["idShort"]] = self.getElemValue(contactInformation)
                self.ContactInformationSubmodelData[submodelElem["idShort"]] = ContactInformationDict
        except Exception as E:
            print(str(E))
            