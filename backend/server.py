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
    return await search_articles("machine learning")




@app.get("/search/{query}")
async def search_articles(query: str):
    search = arxiv.Search(
        query=query,
        max_results=50,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    final_document = []
    for result in search.results():
        summary = str(result.summary).replace("\n", " ")
        document = {
            'Title': str(result.title),
            'Summary': summary,
            'Entry_id': str(result.entry_id),
            'PDF_URL': str(result.pdf_url),
            'Published': str(result.published),
            'Authors': [str(author) for author in result.authors],
            'Primary_category': str(result.primary_category)
        }
        final_document.append(document)
    return final_document 




@app.get("/{article_id}")
async def info(article_id: str):
    print(f"Searching for article with ID: {article_id}")
    search = arxiv.Search(id_list=[article_id])
    result = next(search.results())

    # Create a dictionary with the required fields
    document = {
        'Title': str(result.title),
        'Summary': str(result.summary).replace("\n", " "),
        'Entry_id': str(result.entry_id),
        'PDF_URL': str(result.pdf_url),
        'Published': str(result.published),
        'Authors': [str(author) for author in result.authors],
        'Primary_category': str(result.primary_category)
    }

    return document

 