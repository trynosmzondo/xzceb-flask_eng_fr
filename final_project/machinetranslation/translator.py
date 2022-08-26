"""import json"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('Oz6LPOOLzBlb7x22BeKlI1GcKezzD5y7a5FD4fweIE6Z')
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/4364e28f-b298-435d-8f19-90fe1c827cfc')

englishText = language_translator.translate(
    text = 'Bonjour, comment allez-vous?',
    model_id = 'fr-en').get_result()
print (englishText)

frenchText = language_translator.translate(
    text = 'Hello, how are you?',
    model_id = 'en-fr').get_result()
print (frenchText)




