import zeep
# define a URL do WSDL
wsdl_url = "http://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

numero = input("Digite um numero: ")

result = client.service.NumberToWords(
    ubiNum=numero
)

#resultado
print(f"O numero por extenso e em inglês = {result}")