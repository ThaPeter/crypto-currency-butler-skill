from mycroft import MycroftSkill, intent_file_handler


class CryptoCurrencyButler(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('butler.currency.crypto.intent')
    def handle_butler_currency_crypto(self, message):
        currency = message.data.get('currency')

        self.speak_dialog('butler.currency.crypto', data={
            'currency': currency
        })


def create_skill():
    return CryptoCurrencyButler()

