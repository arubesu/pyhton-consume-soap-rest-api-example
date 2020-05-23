from zeep import Client

client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')
print ('List of Countries: \n {} '.format(client.service.ListOfCountryNamesByCode()))
print ('CountryISOCode: \n {}'.format(client.service.CountryISOCode("Netherlands")))
print ('CapitalCity: \n {}'.format(client.service.CapitalCity("NL")))
print ('CountryCurrency: \n {}'.format(client.service.CountryCurrency("NL")))
