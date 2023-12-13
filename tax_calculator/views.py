from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from datetime import datetime, timedelta
import json
from rest_framework.generics import GenericAPIView
from rest_framework.schemas import get_schema_view
from rest_framework import permissions

info = {
    'title': 'Your API Title',
    'description': 'Description of your API',
    'version': '1.0',
    'terms_of_service': 'https://example.com/terms',
    'contact': {
        'name': 'Your Name',
        'email': 'your@email.com',
        'url': 'https://example.com/contact',
    },
    'license': {
        'name': 'Your License',
        'url': 'https://example.com/license',
    },
}

SchemaView = get_schema_view(
    title='Your API Title',
    description='Description of your API',
    version='1.0',
    permission_classes=[permissions.AllowAny],  # Adjust permissions as needed
)


class CalculateTaxView(GenericAPIView):

    def post(self, request):
        # Generate the authentication token

        pass1 = "submit1"
        pass2 = "submit2"

        url = "https://taxapi.sinewave.co.in/API/TaxCalculator/CalculateTax"
        print("url_2:", url)

        new_payload = request.data.copy()
        # print("first_payload:", new_payload)

        New = "New"
        Old = "Old"

        if request.data['whichSubmit'] == "submit2":
            if New in request.data['TaxMethod']:
                print("TaxMethod:", New)
                request.data['TaxMethod'] = "R"
            elif Old in request.data['TaxMethod']:
                print("TaxMethod:", Old)
                # Use the second API URL
                request.data['TaxMethod'] = "N"
        pass

        if request.data['whichSubmit'] == "submit2":
            Due_Date = request.data['Due_Date']
            print("Due_Date:", Due_Date)
            Filing_Date = request.data['Filing_Date']
            print("Filing_Date:", Filing_Date)
            DOB = request.data['DOB']
            print("DOB:", DOB)

            Due_Date_obj = datetime.strptime(Due_Date, "%Y-%m-%d")
            Filing_Date_obj = datetime.strptime(Filing_Date, "%Y-%m-%d")
            DOB_obj = datetime.strptime(DOB, "%d/%m/%Y")

            # Convert to Unix timestamp in milliseconds
            unix_timestamp_ms_1 = int(Due_Date_obj.timestamp() * 1000)
            unix_timestamp_ms_2 = int(Filing_Date_obj.timestamp() * 1000)
            unix_timestamp_ms_3 = int(DOB_obj.timestamp() * 1000)

            # Calculate timezone offset
            timezone_offset_1 = timedelta(hours=5, minutes=30)
            timezone_offset_2 = timedelta(
                hours=5, minutes=30)  # +05:30 timezone offset
            timezone_offset_3 = timedelta(hours=5, minutes=30)

            timezone_offset_str_1 = f"{timezone_offset_1.days * 24 * 60 + timezone_offset_1.seconds // 60:02d}{timezone_offset_1.seconds % 60:02d}"
            timezone_offset_str_2 = f"{timezone_offset_2.days * 24 * 60 + timezone_offset_2.seconds // 60:02d}{timezone_offset_2.seconds % 60:02d}"
            timezone_offset_str_3 = f"{timezone_offset_3.days * 24 * 60 + timezone_offset_3.seconds // 60:02d}{timezone_offset_3.seconds % 60:02d}"
            # Create the formatted date string
            New_Due_Date = f"/Date({unix_timestamp_ms_1}+{timezone_offset_str_1})/"
            New_Filing_Date = f"/Date({unix_timestamp_ms_2}+{timezone_offset_str_2})/"
            New_DOB = f"/Date({unix_timestamp_ms_3}+{timezone_offset_str_3})/"

            request.data['Due_Date'] = New_Due_Date
            request.data['Filing_Date'] = New_Filing_Date
            request.data['DOB'] = New_DOB

            # print("New_Due_Date:",New_Due_Date)
            # print("New_Filing_Date:",New_Filing_Date)

        pass

        # Define the headers with the access token, API key, and version
        headers = {
            # Set the content type based on API requirements
            "Content-Type": "application/json"
        }

        payload = request.data
        # print("payload:",payload)

        def remove_quotes(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, dict) or isinstance(value, list):
                        # Recursive call for nested dictionaries or lists
                        remove_quotes(value)
                    elif isinstance(value, str):
                        if value == "0":
                            data[key] = 0
                    elif isinstance(value, int):
                        if value == 0:
                            data[key] = 0
            elif isinstance(data, list):
                for i in range(len(data)):
                    if isinstance(data[i], dict) or isinstance(data[i], list):
                        # Recursive call for nested dictionaries or lists
                        remove_quotes(data[i])
                    elif isinstance(data[i], str):
                        if data[i] == "0":
                            data[i] = 0
                    elif isinstance(data[i], int):
                        if data[i] == 0:
                            data[i] = 0

        # Apply the replacement
        # replace_quotes(payload)
        remove_quotes(payload)

        new_payload = json.dumps(payload, indent=2)

        # Print the modified data
        print("new_payload:", new_payload)

        # Convert new_payload to a dictionary
        payload_dict = json.loads(new_payload)

        # First Request with "TaxMethod": "N"
        payload_n = payload_dict.copy()
        payload_n["TaxMethod"] = "N"

        response_n = requests.post(url, json=payload_n)
        Ndata = response_n.json()
        print("Ndata:", Ndata)

        # Second Request with "TaxMethod": "R"
        payload_r = payload_dict.copy()
        payload_r["TaxMethod"] = "R"

        response_r = requests.post(url, json=payload_r)
        Rdata = response_r.json()
        print("Rdata:", Rdata)

        # print("access_token:",access_token)
        # print("data:",data)

        # Make a POST request to the API with headers and JSON payload
        response = requests.post(url, headers=headers, json=payload)
        print("response:", response)

        # Check if the request was successful (status code 200)
        if response.status_code == 200 and pass1 in request.data['whichSubmit']:
            # Retrieve the response data
            data = response.json()

            print("Output_data", data)

            # Extract specific values from the response
            gross_taxable_income = data["data"]["gross_taxable_income"]
            tax_on_total_income = data["data"]["tax_on_total_income"]
            surcharge = data["data"]["surcharge"]
            health_and_education_cess = data["data"]["health_and_education_cess"]
            gross_total_income = data["data"]["gross_total_income"]
            total_deductions_under_chapter_vi_a = data["data"]["total_deductions_under_chapter_vi_a"]
            cyla = data["data"]["cyla"]
            rebate = data["data"]["rebate"]
            cfl = data["data"]["cfl"]
            due = data["data"]["due"]
            bfla = data["data"]["bfla"]
            total_taxes_paid = data["data"]["total_taxes_paid"]
            total_tax_payable = data["data"]["total_tax_payable"]
            effective_tax_rate = data["data"]["effective_tax_rate"]
            refund = data["data"]["refund"]
            NbalancePayable = Ndata.get("TaxPayableRefundable")
            RbalancePayable = Rdata.get("TaxPayableRefundable")
            balancePayable = 0
            lessRebate87A = 0
            taxWithoutSurcharge = 0
            totalIncome = 0

            print("NbalancePayable:", NbalancePayable)
            print("health_and_education_cess:", health_and_education_cess)

            response_data = {
                'gross_taxable_income': gross_taxable_income,
                'tax_on_total_income': tax_on_total_income,
                'surcharge': surcharge,
                'health_and_education_cess': health_and_education_cess,
                'gross_total_income': gross_total_income,
                'total_deductions_under_chapter_vi_a': total_deductions_under_chapter_vi_a,
                'cyla': cyla,
                'rebate': rebate,
                'cfl': cfl,
                'due': due,
                'bfla': bfla,
                'total_taxes_paid': total_taxes_paid,
                'total_tax_payable': total_tax_payable,
                'effective_tax_rate': effective_tax_rate,
                'refund': refund,
                'balancePayable': balancePayable,
                'lessRebate87A': lessRebate87A,
                'taxWithoutSurcharge': taxWithoutSurcharge,
                'totalIncome': totalIncome,
                'NbalancePayable': NbalancePayable,
                'RbalancePayable': RbalancePayable,
            }
        else:
            response.status_code == 200 and pass2 in request.data['whichSubmit']
            data = response.json()
            print("Output_data", data)

            lessRebate87A = data["Lessrebate87A"]
            surcharge = data["Surcharge"]
            health_and_education_cess = data["EducationCess"]
            tax_on_total_income = data["TotalTax"]
            incomeTaxNormal = data["NormalTax"]
            incomeTaxSpecial = data["SpecialTax"]
            totalIncome = data["TotalIncome"]
            gross_total_income = data["GrossTotalIncome"]
            total_deductions_under_chapter_vi_a = data["T80cout"]
            taxWithoutSurcharge = data["TaxwoSurcharge"]
            balancePayable = data["BalancePayable"]
            total_tax_payable = data["TaxPayable"]
            TaxPayableRefundable = data["TaxPayableRefundable"]
            T234A = data['InterestUS']['T234A']
            T234B = data['InterestUS']["T234B"]
            T234C = data['InterestUS']["T234C"]
            T234C = data['InterestUS']["T234C"]
            NbalancePayable = Ndata["TaxPayableRefundable"]
            RbalancePayable = Rdata["TaxPayableRefundable"]
            Total_234 = data['InterestUS']["Total_234"]
            T234C_1506 = data['InterestUS']["T234C_1506"]
            T234C_1509 = data['InterestUS']["T234C_1509"]
            T234C_1512 = data['InterestUS']["T234C_1512"]
            T234C_1503 = data['InterestUS']["T234C_1503"]

            response_data = {
                'tax_on_total_income': tax_on_total_income,
                'incomeTaxNormal': incomeTaxNormal,
                'incomeTaxSpecial': incomeTaxSpecial,
                'surcharge': surcharge,
                'health_and_education_cess': health_and_education_cess,
                'gross_total_income': gross_total_income,
                'total_deductions_under_chapter_vi_a': total_deductions_under_chapter_vi_a,
                'lessRebate87A': lessRebate87A,
                'totalIncome': totalIncome,
                'taxWithoutSurcharge': taxWithoutSurcharge,
                'balancePayable': balancePayable,
                'total_tax_payable': total_tax_payable,
                'T234A': T234A,
                'T234B': T234B,
                'T234C': T234C,
                'TaxPayableRefundable': TaxPayableRefundable,
                'NbalancePayable': NbalancePayable,
                'RbalancePayable': RbalancePayable,


            }
            print("response_data:", response_data)

        if response.status_code == 200:
            return Response(response_data)
        else:
            return Response(response_data, status=response.status_code)

    def new_method(self, data):
        return data
