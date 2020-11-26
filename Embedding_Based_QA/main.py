import pandas as pd
from sentence_transformers import SentenceTransformer

df = pd.read_csv('geo-qa.csv')

questions = df['Question'].to_list()
answers = df['Answer'].to_list()

print(len(questions))
print(len(answers))

model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')

# Sentences are encoded by calling model.encode()
embeddings = model.encode(questions)

# Print the embeddings
for sentence, embedding in zip(questions, embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print("")
