import requests
APPID,baseURL = "RPR2YG-TQTXP2G5VE", "http://api.wolframalpha.com/v2/query?input="
function_to_derive = raw_input("Please enter a function: ")
requestObject = requests.get(baseURL + function_to_derive + "&appid=" + APPID)
XMLString = str(requestObject.content)
centerLimit = XMLString.find("=", XMLString.find("d/dx"),XMLString.find("</plaintext>",XMLString.find("d/dx")))
print("Derivative " + XMLString[centerLimit:XMLString.find("</plaintext>",XMLString.find("d/dx"))])