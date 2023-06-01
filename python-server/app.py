from flask import Flask
import arxiv

app = Flask(__name__)

@app.route("/")
async def index():
    search = arxiv.Search(
    query = "quantum",
    max_results = 10,
    sort_by = arxiv.SortCriterion.SubmittedDate)
    print(type(search))
    # print(len(search))
    for result in search.results():
        print(result.title)  
        # return result
        document = {'Title': "", 'Summary': "", "Entry_id": '', "PDF_URL": "", "Published": "", "Authors": [], "Primary_category": ""}
        summary = str(result.summary)
        summary2 = summary.replace("\n", " ")
        document['Title'] = str(result.title)
        # document['Summary'] = str(result.summary)
        document['Summary'] = summary2
        document['Entry_id'] = str(result.entry_id)
        document['PDF_URL'] = str(result.pdf_url)
        document['Published'] = str(result.published)
        document['Authors'] = str(result.authors[0])
        document['Primary_category'] = str(result.primary_category)
        # print(document) 
        return document