import requests, json
from bs4 import BeautifulSoup

class GrantScrapper:
    def __init__(self):
        # May not need skipterms due to tf-idf
        self.skipterms = set(["funding", "opportunity", "purpose", "announcement", "this", "the", "a", "of", "from", "to", "through", "foa", "is", "in", "with", "into", "and", "or", "that", "on", "for", "as", "have", "be", "should", "by", "will", "can", "it", "note", "applicants"]) #Maybe read in a list a of common terms

    def scrape_csv(self, csv_file):
        grant_descriptions = dict()
        with open(csv_file) as grants_csv:
            headings = grants_csv.readline()
            line = grants_csv.readline()
            i = 0
            while line:
                isEmpty = False #Was it able to be scraped correctly
                if (i+1) % 5 == 0:
                    print("Processing grant number: ", i+1)
                row = line.split(",")
                # Urls have \n at the end so need to remove this
                if "\n" in row[-1]:
                    row[-1] = row[-1][0:-1]

                description, term_vector = self.scrape(row[0], row[-1])
                if not description:
                    print("Grant ", i, "description is empty!")
                    isEmpty = True
                if not term_vector:
                    print("Grant ", i, "term_vector is empty!")
                    isEmpty = True
                if not isEmpty:
                    description_no_format = " ".join(description.split())
                    grant_descriptions[i] = {"description" : description_no_format, "term_vector" : term_vector}
                else:
                    print("URL: ", row[-1])
                    grant_descriptions[i] = {"description" : "", "term_vector" : []} #If it was not able to scrape or process correctly, set this to empty
                i += 1
                line = grants_csv.readline()


            self.grant_desc_to_json(grant_descriptions)
                
    # Scrape a grant document and return purpose and term vector
    def scrape(self, title, url):
        try:
            doc = requests.get(url)
            soup = BeautifulSoup(doc.text, "html.parser")
            divs = soup.findAll("div", {"class" : "row" })#soup.findAll("div", {"class" : "col-md-8 datacolumn"}) # Get all div elements with class row
        
            purpose = ""
            for div in divs:
                div_labels = div.findAll("div", {"class" : "col-md-4 datalabel"})
                isLabelToPurpose = False
                for label in div_labels:
                    if label.string and "Funding Opportunity Purpose" in label.string:
                        isLabelToPurpose = True

                if isLabelToPurpose:
                    purpose_el = div.find("div", {"class" : "col-md-8 datacolumn"})
                    if purpose_el:
                        purpose += purpose_el.text.strip()
                
            purpose_with_title = title + " " + purpose # Make sure the title is included in the term vector
            term_vector = []
            for term in purpose_with_title.split(" "):
                if len(term) <= 1:
                    continue
                
                term = term.lower()
                if term[0] == "(":
                    term = term[1:]
                if term[-1] == ")":
                    term = term[:-1]
                if term.isalnum():
                    term_vector.append(term)
            return purpose, term_vector
        except Exception as e:
            print("ERROR IN scrape: ", e)
            return "", []


    def grant_desc_to_json(self, grant_descriptions):
        with open("grant_descriptions.json", "w") as grant_desc_json:
            json.dump(grant_descriptions, grant_desc_json)


def main():
    gs = GrantScrapper()
    csv_file = "11_5_2018-AllGuideResultsReport.csv"
    gs.scrape_csv(csv_file)

if __name__ == "__main__":
    main()