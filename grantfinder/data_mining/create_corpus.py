import json
from nltk.corpus import stopwords
from gensim import corpora, models
import sqlite3

# Create set of stop words
skipterms = set(["funding", "opportunity", "purpose", "announcement", "this", "the", "a", "of", "from", "to", "through", "foa", "is", "in", "with", "into", "and", "or", "that", "on", "for", "as", "have", "be", "should", "by", "will", "can", "it", "note", "applicants"])
stop_set =  set(stopwords.words('english'))
stop_set.update(skipterms)

# Create a list of grant term_vectors by extracting from database
conn = sqlite3.connect("../db/development.sqlite3")
c = conn.cursor()
grant_terms = []
for row in c.execute("SELECT term_vector FROM grant_descriptions"):
    term_vector = []
    for term in row[0][1:-1].split(" "):
        term = term[1:-1]
        if term[-1] == "\"":
            term = term[:-1]
        if term not in stop_set:
            term_vector.append(term)
    grant_terms.append(term_vector)

# Create term to ID dictionary
grant_dict = corpora.Dictionary(grant_terms)
grant_dict.save("data/grant_terms_to_id.dict")
#print(grant_dict.token2id)

# Create corpus from grant_terms by transforming each term_vector into a bag of words 
corpus = [grant_dict.doc2bow(term_vector) for term_vector in grant_terms ]
corpora.MmCorpus.serialize("data/grant_terms_corpus.mm", corpus)
#print(corpus)