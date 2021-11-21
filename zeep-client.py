from zeep import Client
import zeep
from xml import *



input=XmlType('''<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
    <SOAP-ENV:Header />
    <SOAP-ENV:Body>
        <ns3:GetCustomerInfoByNumberResquest xmlns:ns3="http://omantel.om/ordermanagementservice">
            <OT_EAI_HEADER>
                <RequestorId>NEP</RequestorId>
            </OT_EAI_HEADER>
            <Request>
                <ReferenceNo>NEP_2591981997258846</ReferenceNo>
                <externalId>940192</externalId>
                <externalIdType>200</externalIdType>
            </Request>
        </ns3:GetCustomerInfoByNumberResquest>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
''')
wsdl = 'http://10.64.172.9:7904/OrderMangementService?wsdl'
client = zeep.Client(wsdl=wsdl)
with client.settings(strict=False):
        resp = client.service.getCustomerInfoByNumber(message=input)
        print(resp.content)

        with open('response_xml.xml' , 'w') as f2:
            f2.write(resp.content)




# request_data =
# response = client.service.getSubscriberDetails(

#     ''
#     {'MsgFormat': ({
#         'RequestorId': 'NEP'
#     }),
#      'ReferenceNo': 'NEP_2591981997258846',
#       'externalId': '940192',
#       'externalIdType': '200'}
