import json
import unittest

import requests


class TestApi(unittest.TestCase):
    base_url = "https://fakerapi.it/api/v1/"

    def test_availability(self):
        url = f"{self.base_url}persons?_locale=pl_PL?_quantity=1"
        response = requests.request("GET", url)
        json_response = json.loads(response.text)
        json_response_code = json_response['code']
        self.assertEqual(json_response_code, 200)

    def test_invalid_request(self):
        url = f"{self.base_url}personZ?_locale=InvalidLocale?_quantity=1"
        response = requests.request("GET", url)
        json_response = json.loads(response.text)
        json_response_code = json_response['code']
        self.assertEqual(json_response_code, 404)

    def test_content(self):
        url = f"{self.base_url}persons?_locale=pl_PL"
        response = requests.request("GET", url)
        json_response = json.loads(response.text)
        json_response_data = json_response['data']
        json_response_data_len = len(json_response_data)
        self.assertEqual(json_response_data_len, 10)

    def test_requested_data_is_provided(self):
        requested_quantity = 13
        url = f"{self.base_url}companies?_quantity={requested_quantity}"
        response = requests.request("GET", url)
        json_response = json.loads(response.text)
        json_response_total = json_response['total']
        self.assertEqual(json_response_total, requested_quantity)

    def test_provided_keys(self):
        requested_keys = ["name", "email", "vat", "phone", "country", "addresses", "website", "image", "contact"]
        url = f"{self.base_url}companies?_quantity=1"
        response = requests.request("GET", url)
        json_response = json.loads(response.text)
        json_response_data_first_element = json_response['data'][0]
        response_keys = []
        for key in json_response_data_first_element:
            response_keys.append(key)
        is_requested_keys_in_response = set(requested_keys).issubset(response_keys)
        self.assertTrue(is_requested_keys_in_response)


if __name__ == '__main__':
    unittest.main()
