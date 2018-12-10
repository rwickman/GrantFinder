from gensim import corpora, models, similarities
 
grant_termIDs_dict = corpora.Dictionary.load("data/grant_terms_to_id.dict")
corpus = corpora.MmCorpus("data/grant_terms_corpus.mm")

tfidf = models.TfidfModel(corpus) # Train td-idf model

corpus_tfidf = tfidf[corpus]
# for doc in corpus_tfidf:
#     print(doc)
lsi = models.LsiModel(corpus, id2word=grant_termIDs_dict)
lsi.save("data/model.lsi")
index = similarities.MatrixSimilarity(lsi[corpus])
index.save("data/grant_similarity.index")