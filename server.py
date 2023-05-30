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
    max_results = 1,
    sort_by = arxiv.SortCriterion.SubmittedDate
    )

    for result in search.results():
        document = {'Title': "", 'Summary': "", "Entry_id": '', "PDF_URL": "", "Published": "", "Authors": [], "Primary_category": ""}
        summary = str(result.summary)
        summary2 = summary.replace("\n", " ")
        document['Title'] = str(result.title)
        document['Summary'] = summary2
        document['Entry_id'] = str(result.entry_id)
        document['PDF_URL'] = str(result.pdf_url)
        document['Published'] = str(result.published)
        document['Authors'] = str(result.authors[0])
        document['Primary_category'] = str(result.primary_category)

        print(result.primary_category)
        print(result.primary_category)
        return document