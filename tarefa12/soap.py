import requests
from xml.dom.minidom import parseString

# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
op = input("Digite de 1 a 3: ")
if op =="1":
    operation = "CountryIntPhoneCode"
elif op =="2":
    operation = "CapitalCity"
elif op =="3":
    operation = "CountryName"
country_code = input("Digite o codigo do país: ")

# XML estruturado
payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<{operation} xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>{country_code}</sCountryISOCode>
					</{operation}>
				</soap:Body>
			</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)

# imprime a resposta
if response.status_code == 200:
    if op =="1":
        print("O codigo de telefone é " + parseString(response.text).documentElement.getElementsByTagName("m:CountryIntPhoneCodeResult")[0].firstChild.nodeValue)
    elif op =="2":
        print("O nome da capital é " + parseString(response.text).documentElement.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue)
    elif op =="3":
        print("O nome desse país é " + parseString(response.text).documentElement.getElementsByTagName("m:CountryNameResult")[0].firstChild.nodeValue)
