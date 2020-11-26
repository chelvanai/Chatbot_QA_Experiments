from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot('chatbot')

trainer = ListTrainer(chatbot)

trainer.train(
   "./ai.yml"
)

response = chatbot.get_response('Are you sapient?')

print(response)