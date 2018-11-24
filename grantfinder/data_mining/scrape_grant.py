import requests, json
from bs4 import BeautifulSoup

class GrantScrapper:
    def __init__(self):
        self.termSet = set()
        self.termList = list() # will need to convert the set to a list only once so the order is maintained
        # May not need skipterms due to tf-idf
        self.skipterms = set(["funding", "opportunity", "purpose", "announcement", "this", "the", "a", "of", "from", "to", "through", "foa", "is", "in", "with", "into", "and", "or", "that", "on", "for", "as", "have", "be", "should", "by", "will", "can", "it", "note", "applicants"]) #Maybe read in a list a of common terms

    # Scrape a grant document and return purpose and term vector
    def scrape(self, title, url):
        try:
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
                    if label.string and "Funding Opportunity Purpose" in label.string:
                        #print("Label found")
                        isLabelToPurpose = True

                if isLabelToPurpose:
                    purpose_el = div.find("div", {"class" : "col-md-8 datacolumn"})
                    if purpose_el:
                        purpose += purpose_el.text.strip()
            
            term_vector = []
            for term in purpose.split(" "):
                if len(term) <= 1:
                    continue
                
                term = term.lower()
                if term[0] == "(" and term[-1] == ")":
                    term = term[1:-1]
                if term.isalnum():
                    term_vector.append(term)
            return purpose, term_vector
        except Exception as e:
            print("ERROR IN scrape: ", e)
            return "", []
