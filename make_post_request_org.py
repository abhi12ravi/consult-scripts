#This script adds Organisation data to the FHIR server 

#Pre-requisite: Make sure the FHIR server is up and running.

#Run: $python3 make_post_request_org.py

import requests

url = 'http://ec2-18-132-234-236.eu-west-2.compute.amazonaws.com:8080/hapi/fhir/Organization?_format=xml&_pretty=true'
xml = """<?xml version="1.0" encoding="UTF-8"?>

<Organization xmlns="http://hl7.org/fhir">
  <id value="101"/> 
  <text> 
    <status value="generated"/> 
    <div xmlns="http://www.w3.org/1999/xhtml">
      
      <p> Cardiology @ Acme Hospital. ph: +1 555 234 3523, email: 
        <a href="mailto:gastro@acme.org">Cardiology@acme.org</a> 
      </p> 
    
    </div> 
  </text> 
<!--    Clinical Team "Cardiology" at Acme Hospital    -->
  <identifier> 
    <system value="http://www.acme.org.au/units"/> 
    <value value="Gastro"/> 
  </identifier> 
  <name value="Gastroenterology"/> 
  <telecom> 
    <system value="phone"/> 
    <value value="+1 555 234 3523"/> 
    <use value="mobile"/> 
  </telecom> 
  <telecom> 
    <system value="email"/> 
    <value value="gastro@acme.org"/> 
    <use value="work"/> 
  </telecom> 
</Organization>"""

headers = {'Content-Type': 'application/fhir+xml'}

x = requests.post(url, data=xml, headers=headers)

print(x.text)