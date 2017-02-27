# # !/usr/bin/python
# # -*-coding: utf-8 -*-
# import json
# import sys
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
#
# BOT_NAME = 'Bot'
#
# chatbot = ChatBot(
#                     BOT_NAME,
#                     storage_adapter='chatterbot.adapters.storage.MongoDatabaseAdapter',
#                     database='chatterbot-database',
#                     logic_adapters=[
#                       'chatterbot.adapters.logic.MathematicalEvaluation',
#                       'chatterbot.adapters.logic.TimeLogicAdapter',
#                       'chatterbot.adapters.logic.ClosestMatchAdapter'
#                     ],
#                     filters=[
#                       'chatterbot.filters.RepetitiveResponseFilter'
#                     ],
#                   )
#
# conversation_file = sys.argv[1]
#
# conversations = json.loads(open(conversation_file).read())
#
# print ("[-] Start training bot")
# chatbot.set_trainer(ListTrainer)
# chatbot.train(conversations)
# print ("[-] Train success")

# # -*- coding: utf-8 -*-
import json
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
BOT_NAME = "Bot"
chatbot = ChatBot(BOT_NAME,
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='chatterbot-database'
)

conversation_file = sys.argv[1]

conversations = json.loads(open(conversation_file).read())

print ("[-] Start training bot")
chatbot.set_trainer(ListTrainer)
chatbot.train(conversations)
print ("[-] Train success")
