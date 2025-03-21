sentence="The Eiffel Tower was built from 1887 to 1889 by French engineer Gustave Eiffel, whose company specialized in building metal frameworks and structures."
"""
Person Eg: Krish C Naik
Place Or Location Eg: India
Date Eg: September,24-09-1989
Time  Eg: 4:30pm
Money Eg: 1 million dollar
Organization Eg: iNeuron Private Limited
Percent Eg: 20%, twenty percent
"""
sentence="The Eiffel Tower was built from 1887 to 1889 by Gustave Eiffel, whose company specialized in building metal frameworks and structures."
import nltk
words = nltk.word_tokenize(sentence)
print(words)
tag_elems = nltk.pos_tag(words)

nltk.ne_chunk(tag_elems).draw()
