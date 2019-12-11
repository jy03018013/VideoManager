import nltk
from nltk.book import *
from nltk.corpus import inaugural
from matplotlib import pyplot

# text=nltk.word_tokenize("PierreVinken , 59 years old , will join as a nonexecutive director on Nov. 29 .")
# print(text1)

# fdist1 = FreqDist(text1)
# vocabulary1 = list(fdist1.keys())
# vocabulary1[:50]
#
# fdist5 = FreqDist(text5)
# sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)
#
# # P38
# V = set(text1)
# long_words = [w for w in V if len(w) > 15]
# sorted(long_words)
#
# fdist5 = FreqDist(text5)
# sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7])
#
# # p39
# list(bigrams(['more','is','said','than','done']))
#
# text4.collocations()
#
# # p42
# [w for w in set(sent7) if not w.islower()]
# [w for w in set(sent7) if w.islower()]
# [w for w in set(text2) if 'cie' in w or 'cei' in w]
#
# # p58
# from nltk.corpus import brown
# news_text = brown.words(categories='news')
# fdist = nltk.FreqDist([w.lower() for w in news_text])

# p60
# cfd = nltk.ConditionalFreqDist(
#     (target,fileid[:4])
#     for fileid in inaugural.fileids()
#     for w in inaugural.words(fileid)
#     for target in ['america','citizen']
#     if w.lower().startswith(target)
# )
#
# # p69
# def generate_model(cfdist,word,num=15):
#     for i in range(num):
#         print(word),
#         word = cfdist[word].max()
#
# text = nltk.corpus.genesis.words('english-kjv.txt')
# bigram = nltk.bigrams(text)

# p73
def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)

