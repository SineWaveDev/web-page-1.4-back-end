from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class CalculateTaxView(APIView):
    def generate_authentication_token(self):
        # Replace these values with the actual API key, secret, and version
        api_key = 'key_live_AL1pBGGBcbcWUYZfGwE8ZwUfEIz3hRl4'
        api_secret = 'secret_live_8lFpvO88BgGJwfQoQEPcGf26Enprq0Yi'
        api_version = '1.0'

        url = 'https://api.sandbox.co.in/authenticate'

        # Set the headers with API key, secret, and version
        headers = {
            'x-api-key': api_key,
            'x-api-secret': api_secret,
            'x-api-version': api_version
        }

        try:
            response = requests.post(url, headers=headers)
            response_data = response.json()
            if "access_token" in response_data:
                access_token = response_data["access_token"]
                return access_token
            else:
                print("Access token not found in the response.")
                return None

        except requests.exceptions.RequestException as e:
            print("Error occurred while making the request:", e)
            return None

    def post(self, request):
        # Generate the authentication token
        access_token = self.generate_authentication_token()
        if not access_token:
            return Response("Failed to generate authentication token.", status=500)

        url = "https://api.sandbox.co.in/calculators/income-tax/old"

        # Define the headers with the access token, API key, and version
        headers = {
            "Authorization": access_token,
            "x-api-key": "key_live_AL1pBGGBcbcWUYZfGwE8ZwUfEIz3hRl4",
            "x-api-version": "1.0"
        }

        payload = request.data
        print("request:",request)
        print("payload:",payload)
        # print("data:",data)
        

        # Make a POST request to the API with headers and JSON payload
        response = requests.post(url, headers=headers, json=payload)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Retrieve the response data
            data = response.json()

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

            # Return the calculated values as a response
            # Render the template with the calculated values
            return Response({
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

            })

        else:
                return Response("Request failed with status code: " + str(response.status_code), status=response.status_code)

    def new_method(self, data):
        return data


