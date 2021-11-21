
# client = zeep.Client('http://10.64.172.9:7904/OrderMangementService?wsdl')

# response = client.create_message('getCustomerInfoByNumber' , )

import logging.config

import xmltodict
from zeep import Client
from zeep import xsd
from zeep.plugins import HistoryPlugin
import xml.etree.ElementTree as ET




# logging.config.dictConfig({
#     'version': 1,
#     'formatters': {
#         'verbose': {
#             'format': '%(name)s: %(message)s'
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose',
#         },
#     },
#     'loggers': {
#         'zeep.transports': {
#             'level': 'DEBUG',
#             'propagate': True,
#             'handlers': ['console'],
#         },
#     }
# })

wsdl = 'https://ecs.syr.edu/faculty/fawcett/handouts/cse686/code/calcWebService/Calc.asmx?wsdl'
history = HistoryPlugin()
client = Client(wsdl, plugins=[history])
with client.settings(raw_response=True):
    response = client.service.Subtract(50 , 5)
    
    
    my_xml_to_dict = xmltodict.parse(response.content)
    print(my_xml_to_dict)

    
    
    root = ET.fromstring(my_xml_to_dict).getroot()
    for item in root:
        print(item)
        

    

# OrderedDict([('soap:Envelope', OrderedDict([('@xmlns:soap', 'http://schemas.xmlsoap.org/soap/envelope/'), ('@xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance'), ('@xmlns:xsd', 'http://www.w3.org/2001/XMLSchema'), ('soap:Body', OrderedDict([('SubtractResponse', OrderedDict([('@xmlns', 'http://tempuri.org/'), ('SubtractResult', '45')]))]))]))])    