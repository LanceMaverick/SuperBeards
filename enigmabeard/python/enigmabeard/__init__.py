import telepot
import telepot.aio
from skybeard.beards import BeardChatHandler
from skybeard.predicates import regex_predicate
from skybeard.decorators import onerror, getargsorask
from skybeard.utils import get_args
import enigma
class EnigmaBeard(BeardChatHandler):
    __userhelp__ = """
   	To use the early beta version of the Skybeard Enigma M3 Plugin
        simply use the command <code>encrypt</code> followed by your
        chosen 3 letter key then your message without spaces:
        
        <code>/encrypt NUT THISISAMESSAGE</code> 
     """

    __commands__ = [
        ("encrypt", "encode", "Encode message using M3 Enigma Machine." ),
    ]

    _timeout = 5*60

    @onerror()
    @getargsorask([("key", 'What\'s the key?'), ("message", 'What\'s the message?')])
    async def encode(self, msg, key, message):
        enigma_m3 = enigma.Enigma()
        enigma_m3.set_key(key)
        await self.sender.sendMessage(enigma_m3.type_phrase(message)) 

