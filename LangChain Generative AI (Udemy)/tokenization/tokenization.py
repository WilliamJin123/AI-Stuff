from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize, TreebankWordTokenizer #sent-tokenize converts par to sentence

corpus = """Hello Welcome, to NLP tutorials.
My name is William's, I am a university student. Hello World.
"""
print(corpus)
### Tokenization
## Paragraph --> Sentence
documents = sent_tokenize(corpus) #period-separated
print(documents)
for sentence in documents:
    print(sentence)
## Tokenization
## Paragraph --> words
## Sentence --> words
words = word_tokenize(corpus)
print(words)
for sentence in documents:
    print(word_tokenize(sentence))
#all punctuation is separated
print(wordpunct_tokenize(corpus))
 
tokenizer = TreebankWordTokenizer() #periods aren't separate
lst = tokenizer.tokenize(corpus)
print(lst)






