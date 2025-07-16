import arxiv
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from fastapi import BackgroundTasks
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_SERVICE_ROLE')

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

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

REFRESH_INTERVAL = 60 * 90  # 1.5 hours in seconds

async def ensure_articles_table():
    # Supabase is schemaless via API, so ensure table exists via SQL RPC
    # This will only work if the table does not exist
    create_table_sql = '''
    create table if not exists articles (
        entry_id text primary key,
        title text,
        summary text,
        pdf_url text,
        published text,
        authors text,
        primary_category text,
        updated_at text
    );
    '''
    try:
        supabase.rpc("execute_sql", {"sql": create_table_sql}).execute()
    except Exception as e:
        pass  # Table may already exist or function not available

async def cache_articles():
    search = arxiv.Search(
        query="quantum",
        max_results=50,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    for result in search.results():
        authors = [str(a) for a in result.authors]
        data = {
            "entry_id": str(result.entry_id),
            "title": str(result.title),
            "summary": str(result.summary).replace("\n", " "),
            "pdf_url": str(result.pdf_url),
            "published": str(result.published),
            "authors": json.dumps(authors),
            "primary_category": str(result.primary_category),
            "updated_at": datetime.utcnow().isoformat()
        }
        # Upsert (insert or update)
        supabase.table("articles").upsert(data).execute()

async def refresh_cache_periodically():
    while True:
        await cache_articles()
        await asyncio.sleep(REFRESH_INTERVAL)

@app.on_event("startup")
async def on_startup():
    await ensure_articles_table()
    asyncio.create_task(refresh_cache_periodically())

@app.get("/")
async def root():
    # Fetch latest 50 articles ordered by published desc
    response = supabase.table("articles").select(
        "entry_id, title, summary, pdf_url, published, authors, primary_category"
    ).order("published", desc=True).limit(50).execute()
    rows = response.data if hasattr(response, 'data') else response["data"]
    finalDocument = []
    for row in rows:
        document = {
            'Entry_id': row['entry_id'],
            'Title': row['title'],
            'Summary': row['summary'],
            'PDF_URL': row['pdf_url'],
            'Published': row['published'],
            'Authors': json.loads(row['authors']),
            'Primary_category': row['primary_category']
        }
        finalDocument.append(document)
    return finalDocument

@app.get("/info/{id}")
async def info(id: str):
    response = supabase.table("articles").select(
        "entry_id, title, summary, pdf_url, published, authors, primary_category"
    ).eq("entry_id", id).limit(1).execute()
    rows = response.data if hasattr(response, 'data') else response["data"]
    if rows:
        row = rows[0]
        document = {
            'Entry_id': row['entry_id'],
            'Title': row['title'],
            'Summary': row['summary'],
            'PDF_URL': row['pdf_url'],
            'Published': row['published'],
            'Authors': json.loads(row['authors']),
            'Primary_category': row['primary_category']
        }
        return document
    return {"error": "Article not found"} 
