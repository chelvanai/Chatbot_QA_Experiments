from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

labels = []
questions = []

for line in open('que.txt', encoding="utf8"):
    labels.append(line.strip().split(" ")[-1])
    questions.append(" ".join(line.strip().split(" ")[:-1]))

answers = []

for line in open('ans.txt', encoding="utf8"):
    answers.append(line.strip())

bow_vectorizer = CountVectorizer()
training_vectors = bow_vectorizer.fit_transform(questions)

classifier = MultinomialNB()
classifier.fit(training_vectors, labels)


class ChatBot:
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "stop")

    def start_chat(self):
        user_response = input("Hi, I'm a chatbot trained on random dialogs!!\n")
        self.chat(user_response)

    def chat(self, reply):
        while not self.make_exit(reply):
            reply = input(self.generate_response(reply) + "\n")
        return

    def generate_response(self, sentence):
        input_vector = bow_vectorizer.transform([sentence])
        predict = classifier.predict(input_vector)
        index = int(predict[0])
        print("Accurate:", str(classifier.predict_proba(input_vector)[0][index - 1] * 100)[:5] + "%")
        return answers[index - 1]

    def make_exit(self, reply):
        for exit_command in self.exit_commands:
            if exit_command in reply:
                print("Ok, have a great day!")
                return True
        return False


if __name__ == '__main__':
    chatbot = ChatBot()
    chatbot.start_chat()