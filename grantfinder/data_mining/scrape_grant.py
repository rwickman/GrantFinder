# TODO
## In ruby code, will still need format of termSet to produce the corresponding search vector
## Will also be used in case none of the search terms appear in the term set

# Don't need the NOT document types since they are only notices

import requests
from bs4 import BeautifulSoup

class Document:
    def __init__(self, url, term_vector = list()):
        self.url = url
        self.term_vector = term_vector

class GrantScrapper:
    def __init__(self):
        self.termSet = set()
        self.termList = list() # will need to convert the set to a list only once so the order is maintained
        # May not need skipterms due to tf-idf
        self.skipterms = set(["funding", "opportunity", "purpose", "announcement", "this", "the", "a", "of", "from", "to", "through", "foa", "is", "in", "with", "into", "and", "or", "that", "on", "for", "as", "have", "be", "should", "by", "will", "can", "it", "note", "applicants"]) #Maybe read in a list a of common terms

    # Scrape a RFA document and returns term frequency map
    #TODO
    ## Need to check if this will return an empty dictionary
    ## Will need to store the purpose since we later have to write it with the term vector to CSV 
    def RFA_Scrape(self, url):
        #TODO
        ## Check how this responds in other RFA documents
        term_frequency_map = dict()

        doc = requests.get(url)
        soup = BeautifulSoup(doc.text, "html.parser")
        divs = soup.findAll("div", {"class" : "row" })#soup.findAll("div", {"class" : "col-md-8 datacolumn"}) # Get all div elements with class row
        purpose = ""
        for div in divs:
            #print("DIV TYPE: ", type(div))
            div_labels = div.findAll("div", {"class" : "col-md-4 datalabel"})
            isLabelToPurpose = False
            for label in div_labels:
                if "Funding Opportunity Purpose" in label:
                    isLabelToPurpose = True

            if isLabelToPurpose:
                purpose_el = div.find("div", {"class" : "col-md-8 datacolumn"})
                if purpose_el:
                    purpose += purpose_el.text.strip()
        

        #purpose_terms = [term for term in purpose.split(" ") if term.isalnum() and term not in self.skipterms] #Get all the terms that are valuable
        
        for term in purpose.split(" "):
            if len(term) <= 1:
                continue
            
            term = term.lower()
            if term[0] == "(" and term[-1] == ")":
                term = term[1:-1]
            if term.isalnum() and term not in self.skipterms:
                # check if the term is already in the frequency map
                if term in term_frequency_map:
                    term_frequency_map[term] += 1
                else:
                    term_frequency_map[term] = 1
                # check if the term is already in self.termSet
                if term not in self.termSet:
                    self.termSet.add(term)
    
        return term_frequency_map

    def generateTermVector(self, term_frequency_map):
        print("\n TERM VECTOR")        
        # Iterate through the termSet
        ## check if term is in fm
        ## If it is, then append the number else append 0
        
        termVector = []
        for term in self.termList :
            if term in term_frequency_map:
                termVector.append(term_frequency_map[term])
            else:
                termVector.append(0)
        return termVector

gs = GrantScrapper()

gs.termSet.add("cat")
gs.termSet.add("sog")
gs.termSet.add("tree")
par_link = "https://grants.nih.gov/grants/guide/pa-files/PAR-18-291.html"
pa_link = "https://grants.nih.gov/grants/guide/pa-files/PA-18-350.html"
par = gs.RFA_Scrape(par_link)
#pa = gs.RFA_Scrape(pa_link)
print(par)
#fm = gs.RFA_Scrape("https://grants.nih.gov/grants/guide/rfa-files/RFA-DK-18-014.html")
#fm2 = gs.RFA_Scrape("https://grants.nih.gov/grants/guide/rfa-files/RFA-CA-19-015.html")
#fm3 = gs.RFA_Scrape("https://grants.nih.gov/grants/guide/rfa-files/RFA-CA-19-014.html")
# print(fm)
# print(fm2)
# print(fm3)

gs.termList = list(gs.termSet)

# print(gs.generateTermVector(fm))
# print(gs.generateTermVector(fm2))
# print(gs.generateTermVector(fm3))

