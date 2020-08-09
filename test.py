from app import app
import unittest
import json


class MorseCodeTest(unittest.TestCase):

    # This method test for the index page that the response  status code is 200.
    def test_index_statuscode(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200,
                         'Index page did not returned 200 status code.')

    # Test the content of the index page.
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.content_type, 'text/html; charset=utf-8',
                         'Response content is not of html type.')

        self.assertTrue(b'The Morse Code' in response.data,
                        '"The Morse Code" was not found in the returned resposne.')

    # Test the encrypt post api for positive scenario.
    def test_encrypt_success(self):
        tester = app.test_client(self)
        request_data = {'message': 'Hi, Welcome.'}
        response = tester.post('/encrypt/', data=request_data,
                               content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200,
                         'Encryt request did not returned 200 status code.')

        self.assertEqual(response.content_type, 'application/json',
                         'Response content is not of json type.')

        self.assertEqual(response.json['status'], 'success')
        self.assertEqual(
            response.json['cipher'], '.... .. --..-- / .-- . .-.. -.-. --- -- . .-.-.-')

    # Test the encrypt post api for negative scenario.
    def test_encrypt_error(self):
        tester = app.test_client(self)
        request_data = {}
        response = tester.post('/encrypt/', data=request_data,
                               content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 400,
                         'Encryt request did not returned 400 status code.')

        self.assertEqual(response.content_type, 'application/json',
                         'Response content is not of json type.')

        self.assertEqual(response.json['status'], 'error')

    # Test the decrypt post api for positive scenario.
    def test_decrypt_success(self):
        tester = app.test_client(self)
        request_data = {'cipher': '.... .. --..-- / .-- . .-.. -.-. --- -- . .-.-.-'}
        response = tester.post('/decrypt/', data=request_data,
                               content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200,
                         'Decryt request did not returned 200 status code.')

        self.assertEqual(response.content_type, 'application/json',
                         'Response content is not of json type.')

        self.assertEqual(response.json['status'], 'success')
        self.assertEqual(
            response.json['message'], 'Hi, welcome.')

    # Test the decrypt post api for negative scenario.
    def test_decrypt_error(self):
        tester = app.test_client(self)
        request_data = {}
        response = tester.post('/decrypt/', data=request_data,
                               content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 400,
                         'Decryt request did not returned 400 status code.')

        self.assertEqual(response.content_type, 'application/json',
                         'Response content is not of json type.')

        self.assertEqual(response.json['status'], 'error')


if __name__ == '__main__':
    unittest.main()
