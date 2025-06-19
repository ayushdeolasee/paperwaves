import arxiv
import json
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5501",
    "http://127.0.0.1:5501",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def result_to_dict(result: arxiv.Result) -> dict:
    """Convert arxiv.Result to a dictionary used by the frontend."""
    authors = [str(author) for author in result.authors]
    summary = result.summary.replace("\n", " ")
    return {
        "Title": result.title,
        "Summary": summary,
        "Entry_id": result.entry_id,
        "PDF_URL": result.pdf_url,
        "Published": str(result.published),
        "Authors": authors,
        "Primary_category": str(result.primary_category),
    }


@app.get("/")
async def root():
    """Return a default set of papers (used on initial page load)."""
    search = arxiv.Search(
        query="quantum",
        max_results=50,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )
    return [result_to_dict(result) for result in search.results()]


@app.get("/info/{paper_id}")
async def info(paper_id: str):
    """Return detailed information for a specific paper."""
    search = arxiv.Search(id_list=[paper_id])
    for result in search.results():
        return result_to_dict(result)
    return {}


@app.get("/search")
async def search(query: str = Query("", alias="query"), author: str = Query("", alias="author"), max_results: int = 50):
    """Search papers by query or author name."""
    if author:
        search_query = f'au:"{author}"'
    else:
        search_query = query
    search = arxiv.Search(
        query=search_query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )
    return [result_to_dict(result) for result in search.results()]

