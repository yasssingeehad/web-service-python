# client = zeep.Client('http://10.64.172.9:7904/OrderMangementService?wsdl')

# response = client.create_message('getCustomerInfoByNumber' , )
source_file = 'input.xlsx'


import collections
from zeep import Client
from zeep import xsd
from zeep.plugins import HistoryPlugin
import lxml.etree as etree
import logging.config
import xmltodict
import json
import traceback
import csv
# import pandas as pd
external_id_csv=''
account_categories_csv=''

def fetch_cust_details(subno):
    with open('external_id_type.csv' , 'r')as external_id_file:
        external_id_csv = csv.reader(external_id_file)
        external_id_dict = {}
        for i in external_id_csv:
            external_id_dict[i[0]] = i[2]
    
    with open('account_category_values.csv' , 'r')as account_categories_file:
        account_categories_csv = csv.reader(account_categories_file)
        account_categories_dict = {}
        for i in account_categories_csv:
            account_categories_dict[i[0]] = i[2]
        wsdl = 'http://10.64.172.9:7904/OrderMangementService?wsdl'
        history = HistoryPlugin()
        client = Client(wsdl, plugins=[history])

   
    
    


    # GetCustomerInfoByNumberRequestType(
    # {http://omantel.om/ordermanagementservice}GetCustomerInfoByNumberRequestType(OT_EAI_HEADER: {http://omantel.om/ordermanagementservice}OT_EAI_HEADERType, Request: {http://omantel.om/ordermanagementservice}GetCustomerInfoByNumberReqType))


    try:
        with client.settings(raw_response=True):
            response = client.service.getCustomerInfoByNumber(OT_EAI_HEADER={
                "MsgFormat": "",
                "MsgVersion": "",
                "RequestorId": "NEP",
                "RequestorChannelId": "",
                "RequestorUserId": "",
                "RequestorLanguage": "",
                "RequestorSecurityInfo": "",
                "EaiReference": "",
                "ReturnCode": ""},
                Request={
                    "ReferenceNo": "NEP_2591981997258846",
                    "externalId": subno ,
                    "externalIdType": "200",
                    "acctExternalId": "",
                    "changeWho": ""

            }
            )
            # print("Printing Response.....")
            print(response)

            my_dict = xmltodict.parse(response.content)

            # print(my_dict['soapenv:Envelope']['soapenv:Body']['NS1:GetCustomerInfoByNumberResponse']['Response'].keys())

           
            # map the required fields
            CustPhone1 = my_dict['soapenv:Envelope']['soapenv:Body']['NS1:GetCustomerInfoByNumberResponse']['Response']['custPhone1']
            if type(CustPhone1) == str:
                CustPhone1 = CustPhone1
            else:
                CustPhone1 = ""

            CustPhone2 = my_dict['soapenv:Envelope']['soapenv:Body']['NS1:GetCustomerInfoByNumberResponse']['Response']['custPhone2']
            if type(CustPhone2) == str:
                    CustPhone2 = CustPhone2
            else:
                CustPhone2 = ""

            custAddress1 = my_dict['soapenv:Envelope']['soapenv:Body']['NS1:GetCustomerInfoByNumberResponse']['Response']['custAddress1']
            if type(custAddress1) == str:
                    custAddress1 = custAddress1
            else:
                custAddress1 = ""
            
            custAddress2 = my_dict['soapenv:Envelope']['soapenv:Body']['NS1:GetCustomerInfoByNumberResponse']['Response']['custAddress2']
            if type(custAddress2) == str:
                custAddress2 = custAddress2
            else:
               custAddress2 = ""
            custCity = my_dict['soapenv:Envelope']['soapenv:Body']['NS1:GetCustomerInfoByNumberResponse']['Response']['custCity']
            if type(custCity) == str:
                custCity = custCity
            else:
               custCity = ""
            dateActive = my_dict['soapenv:Envelope']['soapenv:Body']['NS1:GetCustomerInfoByNumberResponse']['Response']['dateActive']
            if type(dateActive) == str:
                dateActive = dateActive
            else:
                dateActive = ""
            accountCategory = my_dict['soapenv:Envelope']['soapenv:Body']['NS1:GetCustomerInfoByNumberResponse']['Response']['accountCategory']
            if type(accountCategory) == str:
                  accountCategory = accountCategory
            else:
                accountCategory = ""
            billFname = my_dict['soapenv:Envelope']['soapenv:Body']['NS1:GetCustomerInfoByNumberResponse']['Response']['billFname'] 
            
            

            if type(billFname) == str:
                  billFname = billFname
            else:
                billFname = ""s

            statementToEmail = my_dict['soapenv:Envelope']['soapenv:Body']['NS1:GetCustomerInfoByNumberResponse']['Response']['statementToEmail'] 
            if type(statementToEmail) == str:
                statementToEmail = statementToEmail.replace("," , ";")
            else:
                statementToEmail = ""    
            customer_id = my_dict['soapenv:Envelope']['soapenv:Body']['NS1:GetCustomerInfoByNumberResponse']['Response']['customerIdDets']
            
            if type(customer_id) ==  list:
                customer_id = customer_id = customer_id[0]
            
            if type(customer_id) == collections.OrderedDict:
                customerId = customer_id['customerId']
                customerIdType = customer_id['customerIdType']

            print(
                "Contact1 # " + str(CustPhone1) + "\n" + 
                "CustPhone2 # "+  str(CustPhone2) + "\n" +  
                "custAddress1 # "+  str(custAddress1) + "\n" +  
                "custAddress2 # "+  str(custAddress2) + "\n" +  
                "dateActive # "+  str(dateActive) + "\n" +  
                "statementToEmail # "+  str(statementToEmail) + "\n" +  
                "custCity # "+  str(custCity) + "\n" +  
                "billFname # "+  str(billFname) + "\n" +  
                "customerId # "+  str(customerId) + "\n" +
                "customerIdType # "+  str(customerIdType) +"\n" +  
                "accountCategory # " + str(accountCategory)
            )

            return {
                "Contact1": str(CustPhone1)  ,  
                "CustPhone2": str(CustPhone2) , 
                "custAddress1" :str(custAddress1),
                "custAddress2" :str(custAddress2),
                "dateActive" :str(dateActive),
                "statementToEmail" :str(statementToEmail),
                "custCity" :str(custCity),
                "billFname" :str(billFname),
                "customerId" :str(customerId),
                "customerIdType" :str(customerIdType),
                "accountCategory" :str(accountCategory)
                }
                

                    



    except Exception as e:
        print("Exception has occured")
        #print(e.m)
        print(traceback.print_exc())


with open('output_account_file.csv' , 'w') as output_f:
    output_f.write(
                "Account_number," + 
                "Contact1 ," + 
                "CustPhone2 ,"+
                "custAddress1 ,"+
                "custAddress2 ,"+
                "dateActive ,"+
                "statementToEmail ,"+
                "custCity ,"+
                "billFname ,"+
                "customerId, "+
                "customerIdType , "+ 
                "accountCategory "+ 
                "\n")





with open('output_account_file.csv' , 'a') as output_f_append:
    with open('input_account_file.csv' , 'r') as input_f:
        data = input_f.readlines()
        for i in data:
            i = i.strip()
            print("Fetching Customer Details for " + i + "\n\n\n\n\n\n\n")
            try:
                customer_details = fetch_cust_details(i)
                print("Customer Details Fetched" + str(customer_details))
                output_f_append.write(
                    i + "," +customer_details['Contact1'] + ","
                    + customer_details['CustPhone2'] + ","
                    + customer_details['custAddress1'] + ","
                    + customer_details['custAddress2'] + ","
                    + customer_details['dateActive'] + ","
                    + customer_details['statementToEmail'] + ","
                    + customer_details['custCity'] + ","
                    + customer_details['billFname'] + ","
                    + customer_details['customerId'] + ","
                    + customer_details['customerIdType'] + ","
                    + customer_details['accountCategory'] + "\n"
                  )
            except Exception as e:
                print("Issue occured while fetching details for sub " + i)
                print(e)

# arbor tables to get the account category labels

# select * from ACCOUNT_CATEGORY_VALUES;


# select * from external_id_type_values where external_id_type = 105;




