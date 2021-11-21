# client = zeep.Client('http://10.64.172.9:7904/OrderMangementService?wsdl')

# response = client.create_message('getCustomerInfoByNumber' , )

from zeep import Client
from zeep import xsd
from zeep.plugins import HistoryPlugin
import lxml.etree as etree
import logging.config
import xmltodict , json



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

wsdl = 'http://10.64.172.9:7904/OrderMangementService?wsdl'
history = HistoryPlugin()
client = Client(wsdl, plugins=[history])

# GetCustomerInfoByNumberRequestType(
# {http://omantel.om/ordermanagementservice}GetCustomerInfoByNumberRequestType(OT_EAI_HEADER: {http://omantel.om/ordermanagementservice}OT_EAI_HEADERType, Request: {http://omantel.om/ordermanagementservice}GetCustomerInfoByNumberReqType))


try:
    with client.settings(raw_response=True):
        response = client.service.getCustomerInfoByNumber(OT_EAI_HEADER={
            "MsgFormat": "" , 
            "MsgVersion":"", 
            "RequestorId":"NEP" , 
            "RequestorChannelId":"" ,
            "RequestorUserId":"",
            "RequestorLanguage" :"" , 
            "RequestorSecurityInfo":""  , 
            "EaiReference" : ""  ,
            "ReturnCode" :"" } ,
            Request={
                "ReferenceNo":"NEP_2591981997258846" ,
                "externalId": "940192",
                "externalIdType": "200", 
                "acctExternalId" :"", 
                "changeWho": ""

                }
                )
        # print("Printing Response.....")        
        print(response)

        xml_dictionary = xmltodict.parse(response.content)
        my_dict = json.dumps(xml_dictionary)

except Exception as e:
    print(e.message)
