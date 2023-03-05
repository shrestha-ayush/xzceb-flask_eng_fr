"""
This module provides functions to translate English text to French 
and vice versa using IBM Watson Language Translator API.
"""
import os
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Translate English text to French using IBM Watson Language Translator API.
    :param english_text: The English text to be translated.
    :return: The translated French text.
    """
    if english_text is None:
        return None
    response = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    response_dict = json.loads(json.dumps(response))
    french_text = response_dict['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    Translate French text to English using IBM Watson Language Translator API.
    :param french_text: The French text to be translated.
    :return: The translated English text.
    """
    if french_text is None:
        return None
    response = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    response_dict = json.loads(json.dumps(response))
    english_text = response_dict['translations'][0]['translation']
    # english_text = response['translations'][0]['translation']
    return english_text
