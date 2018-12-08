import socket, json, os
from sys import path
from time import sleep
from gensim import corpora, models, similarities
 
class SearchLSA:
    def __init__(self, port=50001, host ='', threshold=0.30):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.PORT = port
        self.HOST = host
        self.grant_termIDs_dict = corpora.Dictionary.load(path[0] + "/data/grant_terms_to_id.dict")
        self.corpus = corpora.MmCorpus(path[0] + "/data/grant_terms_corpus.mm")
        self.lsi = models.LsiModel.load(path[0] +'/data/model.lsi')
        self.index = similarities.MatrixSimilarity.load(path[0] + "/data/grant_similarity.index")
        self.threshold = threshold

    def start(self):
        with self.socket as s:
            # Occasionally the previous proccess didn't have enough time to exit/clean up
            ## So need to make sure we use a different port for the time being
            notBinded = True
            #maxRetries = 10
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # To prevent TCP's TIME_WAIT
            while notBinded:
                try:
                    s.bind((self.HOST, self.PORT))
                    notBinded = False
                except Exception as e:
                    print("ERROR IN searchLSA.py: ", e)
                    print("This is due to TCP TIME_WAIT. So please wait for a few seconds")
                    sleep(2)
                    
                    #if curRetries > maxRetries:
                    #    print("MAX RETRIES EXCEEDED FOR BIND")
                    #    exit()

            s.listen(1)
            while True:
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    data = conn.recv(8192)
                    print("Received query. Computing results...")
                    if not data:
                        # If empty query sent back empty array
                        conn.sendall(json.dumps([]).encode()) 
                    else:
                        search_results = self.search(data.decode())
                        json_results = json.dumps(search_results)
                        conn.sendall(json_results.encode())
                    #exit()

    def search(self, query):
        vec_bow = self.grant_termIDs_dict.doc2bow(query.lower().split()) # Convert query to bag of words
        vec_lsi = self.lsi[vec_bow] # Transfrom bow to lsi vector space

        sims = self.index[vec_lsi] # perform a similarity query against the corpus
        sims = sorted(enumerate(sims, 1), key=lambda cosine_tuple: cosine_tuple[1], reverse=True) # Maps the grants ID to consine similarity value
        # for i, s in enumerate(sims):
        #     if i > 10:
        #         break
        #     print(s)

        search_results = []
        for grant_cosine_tuple in sims:
            if grant_cosine_tuple[1] > self.threshold:
                grant_cosine_list = list(grant_cosine_tuple)
                grant_cosine_list[1] = float(grant_cosine_list[1]) 
                search_results.append(grant_cosine_list)
        return search_results


def main():
    s_lsa = SearchLSA()
    s_lsa.start()

if __name__ == "__main__":
    main()
