import arxiv
import json 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5501",
    "http://127.0.0.1:5501",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    search = arxiv.Search(
    query = "quantum",
    max_results = 10,
    sort_by = arxiv.SortCriterion.SubmittedDate)
    finalDocument = []
    for result in search.results():
        authors = []
        document = {'Title': "", 'Summary': "", "Entry_id": '', "PDF_URL": "", "Published": "", "Authors": [], "Primary_category": ""}
#       document = {'Title': "", 'Summary': "", "Entry_id": '', "PDF_URL": "", "Primary_category": ""}
        summary = str(result.summary)
        summary2 = summary.replace("\n", " ")
        document['Title'] = str(result.title)
        # document['Summary'] = str(result.summary)
        document['Summary'] = summary2
        document['Entry_id'] = str(result.entry_id)
        document['PDF_URL'] = str(result.pdf_url)
        document['Published'] = str(result.published)
        i = 0
        while True:
            if i == len(result.authors):
                break
            authors.append(str(result.authors[i]))
            i += 1
            
        document['Authors'] = authors
        # document['Authors'] = str(result.authors[0])
        document['Primary_category'] = str(result.primary_category)
        # print(document)
#       print(str(result.authors))
        json_document = json.dumps(document)
        # print(document)
        finalDocument.append(document)
        print(document) 
    return finalDocument 