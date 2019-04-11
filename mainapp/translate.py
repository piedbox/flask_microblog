import json
import requests
from flask_babel import _
from mainapp import app

def translate(text, dest_language):
    if 'YA_TRANSLATOR_KEY' not in app.config or \
            not app.config['YA_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': app.config['YA_TRANSLATOR_KEY']}
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json'
                     '/translate?key={}&text={}&lang={}&format=plain&options=1'.format(
                         app.config['YA_TRANSLATOR_KEY'],text, dest_language))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    translated_text = json.loads(r.content.decode('utf-8-sig'))
    res = translated_text['text'][0]

    return res
