import arxiv
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import aiosqlite
import asyncio
from fastapi import BackgroundTasks
from datetime import datetime, timedelta

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

DB_PATH = 'articles_cache.db'
REFRESH_INTERVAL = 60 * 90  # 1.5 hours in seconds

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                entry_id TEXT PRIMARY KEY,
                title TEXT,
                summary TEXT,
                pdf_url TEXT,
                published TEXT,
                authors TEXT,
                primary_category TEXT,
                updated_at TEXT
            )
        ''')
        await db.commit()

async def cache_articles():
    search = arxiv.Search(
        query="quantum",
        max_results=50,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    async with aiosqlite.connect(DB_PATH) as db:
        for result in search.results():
            authors = [str(a) for a in result.authors]
            await db.execute('''
                INSERT OR REPLACE INTO articles (entry_id, title, summary, pdf_url, published, authors, primary_category, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                str(result.entry_id),
                str(result.title),
                str(result.summary).replace("\n", " "),
                str(result.pdf_url),
                str(result.published),
                json.dumps(authors),
                str(result.primary_category),
                datetime.utcnow().isoformat()
            ))
        await db.commit()

async def refresh_cache_periodically():
    while True:
        await cache_articles()
        await asyncio.sleep(REFRESH_INTERVAL)

@app.on_event("startup")
async def on_startup():
    await init_db()
    asyncio.create_task(refresh_cache_periodically())

@app.get("/")
async def root():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('SELECT entry_id, title, summary, pdf_url, published, authors, primary_category FROM articles ORDER BY published DESC LIMIT 50')
        rows = await cursor.fetchall()
        finalDocument = []
        for row in rows:
            document = {
                'Entry_id': row[0],
                'Title': row[1],
                'Summary': row[2],
                'PDF_URL': row[3],
                'Published': row[4],
                'Authors': json.loads(row[5]),
                'Primary_category': row[6]
            }
            finalDocument.append(document)
        return finalDocument

@app.get("/info/{id}")
async def info(id: str):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('SELECT entry_id, title, summary, pdf_url, published, authors, primary_category FROM articles WHERE entry_id = ?', (id,))
        row = await cursor.fetchone()
        if row:
            document = {
                'Entry_id': row[0],
                'Title': row[1],
                'Summary': row[2],
                'PDF_URL': row[3],
                'Published': row[4],
                'Authors': json.loads(row[5]),
                'Primary_category': row[6]
            }
            return document
        return {"error": "Article not found"} 