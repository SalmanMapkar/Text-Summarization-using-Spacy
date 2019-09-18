import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
from tkinter import Tk
from tkinter.filedialog import askopenfilename
stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')

def textsummarizar(Text):
    docx = nlp(Text)
    word_frequencies = {}
    for word in docx:
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text]=1
            else:
                word_frequencies[word.text]+=1
    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=(word_frequencies[word]/maximum_frequency)
    sentence_list = [ sentence for sentence in docx.sents]
    sentence_scores={}
    for sent in sentence_list:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(" "))<30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent]=word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent]+=word_frequencies[word.text.lower()]    
    summarized_sentences = nlargest(7,sentence_scores,key=sentence_scores.get)
    final_sentences = [ w.text for w in summarized_sentences ]
    summary=" ".join(final_sentences)
    print("\n\nSummarized Data : {}".format(summary))
    print("Length of original text is {} and Length of summarized text is {}".format(len(Text),len(summary)))

print("1. Enter text\n2. Choose file")
while(1):
    x=int(input("Choose any one of the below option: "))
    if x==1:
        Text = str(input("Enter Text to be summarized: "))
        textsummarizar(Text)
    elif x==2:
        Tk().withdraw() 
        filename = askopenfilename()
        f=open(filename, "r")
        if f.mode=="r":
            Text=f.read()
            textsummarizar(Text)
    else:
        print("Invalid choice")
        continue
    break
