from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

logging.basicConfig(level=logging.INFO)

chatbot = ChatBot("Chatpot")

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)


exit_conditions = (":q", "quit", "exit")
while True:
    query = input("\U0001F600 ")
    if query in exit_conditions:
        break
    else:
        print(f"\U0001F916 {chatbot.get_response(query)}")

