
'''
Created on 27 May 2024

@author: pakala
'''
from flask import Blueprint, render_template,request,Response,redirect,render_template_string

import json
import requests
from time import sleep

from restapi.parser.submodels.std.carbonfootprint_parser import CarbonFootPrintParser
from restapi.parser.submodels.std.contactinformation_parser import ContactInformationParser
from restapi.parser.submodels.std.functionalsafety_parser import FunctionalSafetyParser
from restapi.parser.submodels.std.nameplate_parser import NamePlateParser
from restapi.generator.html_generator import HTML_Generator


bp = Blueprint("pages", __name__)

htmlData = dict()


@bp.route("/",methods=("GET", "POST"))
def home():
    if request.method == "GET":
        return render_template("templates/home.html")
    
    if request.method == "POST":
        try:
            url = request.form.get("inputURL")
            response = requests.get(url)
            if response.status_code == 200:
                submodelsList = json.loads(response.text)
                for submodel in submodelsList:
                    if submodel["semanticId"]["keys"][0]["value"] == "https://admin-shell.io/zvei/nameplate/2/0/Nameplate":
                        nmParser = NamePlateParser(submodel)
                        nmParser.parse()
                        hm = HTML_Generator()
                        htmlData["NamePlate"] = hm.generate_html_code("NamePlate", nmParser.nameplateData)
                        
                    elif submodel["semanticId"]["keys"][0]["value"] == "https://admin-shell.io/zvei/nameplate/1/0/ContactInformations":
                        ciParser = ContactInformationParser(submodel)
                        ciParser.parse() 
                        hm = HTML_Generator()
                        htmlData["ContactInformation"] = hm.generate_html_code("ContactInformations", ciParser.ContactInformationSubmodelData)
                        
                    elif submodel["semanticId"]["keys"][0]["value"] == "https://admin-shell.io/idta/iec62683/1/0/FunctionalSafety":
                        fsParser = FunctionalSafetyParser(submodel)
                        fsParser.parse()
                        hm = HTML_Generator()
                        htmlData["FunctionalSafety"] = hm.generate_html_code("FunctionalSafety", fsParser.FunctionalSafetyData)
                        
                    elif submodel["semanticId"]["keys"][0]["value"] == "https://admin-shell.io/idta/CarbonFootprint/CarbonFootprint/0/9":
                        cfParser = CarbonFootPrintParser(submodel)
                        cfParser.parse()
                        hm = HTML_Generator()
                        htmlData["CarbonFootPrint"] = hm.generate_html_code("CarbonFootPrint", cfParser.carbonFootPrintData)
    
            return render_template("templates/nameplate.html",submodel = htmlData["NamePlate"], submodelsList = list(htmlData.keys()))
        
        except Exception as E:
            print(str(E))
            return redirect("/", code=302)


@bp.route("/nameplate")
def getNamePlate():
    if "NamePlate" in list(htmlData.keys()):
        return render_template("templates/nameplate.html",submodel = htmlData["NamePlate"], submodelsList = list(htmlData.keys()))
    else:
        return redirect("/", code=302)
    
@bp.route("/contactinformation")
def getContactInformation():
    if "ContactInformation" in list(htmlData.keys()):
        return render_template("templates/contactinformation.html",submodel = htmlData["ContactInformation"], submodelsList = list(htmlData.keys()))
    else:
        return redirect("/", code=302)
    
@bp.route("/functionalsafety")
def getFunctionalSafety():
    if "FunctionalSafety" in list(htmlData.keys()):
        return render_template("templates/functionalsafety.html",submodel = htmlData["FunctionalSafety"], submodelsList = list(htmlData.keys()))
    else:
        return redirect("/", code=302)    
    
@bp.route("/carbonfootprint")
def geCarbonFootPrint():
    if "CarbonFootPrint" in list(htmlData.keys()):
        return render_template("templates/carbonfootprint.html",submodel = htmlData["CarbonFootPrint"], submodelsList = list(htmlData.keys()))
    else:
        return redirect("/", code=302)

@bp.route("/timeseries")
def realtimedata(): 
    return render_template("templates/timeseriesdata.html")

 
@bp.route("/ws")
def anything(ws):

    print(f'DEBUG: websocket endpoint called')

    while True:

        for i in range(1000):

            data = 2*i+7

            ws.send(data)

            sleep(2)
