#Classification problem
# find root of the words, remove suffixes and prefixes
# ex eat, eating, eaten
words=["eating","eats","eaten","write","wrote", "written","writing"]

##PorterStemmer

from nltk.stem import PorterStemmer
stemming = PorterStemmer()
for word in words:
    print(word+"--->"+stemming.stem(word))
#congratulations --> congratul (not ideal)

#RegexpStemmer
from nltk.stem import RegexpStemmer
reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4) #suffix expressions
print(reg_stemmer.stem('eating')) #eat
print(reg_stemmer.stem('ingeating')) #ingeat

#Snowball Stemmer
from nltk.stem import SnowballStemmer
snowballstemmer = SnowballStemmer('english')
for word in words:
    print(word+'--->'+snowballstemmer.stem(word))
    






    
