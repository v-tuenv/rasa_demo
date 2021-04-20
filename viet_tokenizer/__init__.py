# import re
# from typing import Any, Dict, List, Text

# from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer
# from rasa.shared.nlu.training_data.message import Message
# from rasa.nlu.constants import TOKENS_NAMES, MESSAGE_ATTRIBUTES
# from rasa.nlu import registry
# from rasa.core import registry
# from underthesea import word_tokenize
# import logging

# class VietTokenizer(Tokenizer):

#     provides = [TOKENS_NAMES[attribute] for attribute in MESSAGE_ATTRIBUTES]

#     def __init__(self, component_config: Dict[Text, Any] = None) -> None:
#         super().__init__(component_config)
        
#         # att

#     def tokenize(self, message: Message, attribute: Text) -> List[Token]:
#         text = message.get(attribute)
#         words = word_tokenize(text)
#         Z = self._convert_words_to_tokens(words, text)
#         return Z