#Wordnet Lemmatizer
#meaningful version of the word
#Wordnet CorpusReaderd
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("going"))
'''
POS - Noun n
verb v
adjective a
avdverb r
'''
print(lemmatizer.lemmatize("going", pos='v'))
words=["eating","eats","eaten","write","wrote", "written","writing"]
for word in words:
    print(word+'--> '+lemmatizer.lemmatize(word, pos='v'))


from nltk.stem import PorterStemmer, SnowballStemmer
from nltk.corpus import stopwords
import nltk

paragraph = 'Out of another, I get a lovely view of the bay and a little private wharf belonging to the estate. There is a beautiful shaded lane that runs down there from the house. I always fancy I see people walking in these numerous paths and arbors, but John has cautioned me not to give way to fancy in the least. He says that with my imaginative power and habit of story-making a nervous weakness like mine is sure to lead to all manner of excited fancies and that I ought to use my will and good sense to check the tendency. So I try.'
print(stopwords.words('english'))
stemmer = SnowballStemmer('english')
sents = nltk.sent_tokenize(paragraph)

## Apply stopwords, filter and apply snowball stemming
for i in range(len(sents)):
    words = nltk.word_tokenize(sents[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sents[i] =' '.join(words) #convert words back into sentences

print(sents)

lemmatizer2 = WordNetLemmatizer()

sents2 = nltk.sent_tokenize(paragraph)
for i in range(len(sents2)):
    words = nltk.word_tokenize(sents2[i])
    words = [lemmatizer2.lemmatize(word.lower(), pos='v') for word in words if word not in set(stopwords.words('english'))]
    sents2[i] =' '.join(words) #convert words back into sentences

print(sents2)



    