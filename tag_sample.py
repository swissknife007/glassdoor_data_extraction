import nltk
from nltk.tag.stanford import POSTagger
from nltk.tag.stanford import POSTagger
st = POSTagger('stanford-postagger-2014-01-04/models/english-bidirectional-distsim.tagger','stanford-postagger-2014-01-04/stanford-postagger.jar')
sentence='Himanshu Bindal is a genius?'
taggedSentence= st.tag(nltk.word_tokenize(sentence))
print taggedSentence
