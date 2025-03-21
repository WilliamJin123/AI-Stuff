import nltk
from nltk.corpus import stopwords
paragraph = 'Out of another, I get a lovely view of the bay and a little private wharf belonging to the estate. There is a beautiful shaded lane that runs down there from the house. I always fancy I see people walking in these numerous paths and arbors, but John has cautioned me not to give way to fancy in the least. He says that with my imaginative power and habit of story-making a nervous weakness like mine is sure to lead to all manner of excited fancies and that I ought to use my will and good sense to check the tendency. So I try.'

sentences = nltk.sent_tokenize(paragraph)
print(sentences)

## Find Pos Tag

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [word for word in words if word not in set(stopwords.words('english'))]
    pos_tags = nltk.pos_tag(words)
    print(pos_tags)
    
sentence = "I go to university of Waterloo"
print(nltk.pos_tag(sentence.split()))