'''s
Created on 11 Jul 2024

@author: pakala
'''
from htmlgenerator import render, DIV,H2,BUTTON,SPAN

class HTML_Generator:
    def __init__(self):
        pass
        
    def create_new_accordin(self,name):
        accordin  = DIV(_class = "accordion accordion-flush", id = name,style="border-style: solid;border-width: 0.25px; margin-bottom: 1vh;")
        return accordin
    
    def create_new_accordin_item(self,key, elements,parent):
        aItem = DIV(_class= "accordion-item")
        aItem.append(self.create_accordin_item_header(key))    
        aItem.append(self.create_according_item_body( key, elements,parent))
        return aItem    
    
    def create_accordin_item_header(self,key):
        itemHeader = H2(_class = "accordion-header", id = key)
        headerButton = BUTTON(key,_class = "accordion-button collapsed", type = "button")
        headerButton.attributes["data-bs-toggle"] = "collapse"
        headerButton.attributes["data-bs-target"] = "#collapse"+key
        headerButton.attributes["aria-expanded"] = "false"
        headerButton.attributes["aria-controls"]="collapse"+key
        itemHeader.append(headerButton)
        
        return itemHeader
    
    def create_according_item_body(self,key,elements,parent):
        divAb = DIV(_class = "accordion-collapse collapse" ,id="collapse"+key)
        divAb.attributes["aria-labelledby"] = key
        divAb.attributes["data-bs-parent"] = "#"+parent+"SubmodelAccordin"
            
        divAccordinBody = DIV(_class = "accordion-body", style = "padding :0px")
        divAccordinBody.extend(self.generate_body_elements(elements))
        divAb.append(divAccordinBody)
       
        return divAb
    
    def generate_body_elements(self,Elements):
        bodyElements = []
        for key,value in Elements.items():
            if type(value) == str:
                bodyElements.append(self.create_newcard(key, value))
            else:
                bodyElements.append(self.generate_accordin(key,{ key : value}))
                
        return bodyElements
    
    def create_newcard(self,key,value):
        divCardBody = DIV(_class="card-body",style="background-color: #CCE5FF;")
        innderBody = DIV(style = "border-style: solid;border-width: 0.25px;min-height : 5vh;background-color: #e6e4e4;")
        divRow = DIV(_class = "row", style= "margin-left : 1.5vw;")
        divRow.append(DIV(key,_class= "col-6"))
        divRow.append(DIV(value,_class= "col-6"))
        innderBody.append(divRow)
        divCardBody.append(innderBody)
        return divCardBody
    
    def generate_accordin(self,name,data):
        Accordin = self.create_new_accordin(name+"SubmodelAccordin")
        for key,elements in data.items():
            Accordin.append(self.create_new_accordin_item(key, elements,name))
        return Accordin
    
    def generate_html_code(self,name,SubmodelData):
        Accordin = self.create_new_accordin(name+"SubmodelAccordinParent")
        accordinItem = self.create_new_accordin_item(name, SubmodelData,name+"SubmodelAccordinParent")
        Accordin.append(accordinItem)
        return render(Accordin,{},)
