# import requests

# api_url = "http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1"

# # Send a GET request to the API URL
# response = requests.get(api_url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Extract the response content in XML format
#     xml_data = response.text
    
#     # Process the XML data or perform any desired operations
#     print(xml_data)
# else:
#     print("Error occurred. Status code:", response.status_code)

# from xml.dom.minidom import parse, parseString
# # document = parse(xml_data)
# # document.version
# # print(document.getElementById("title"))

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
    #   document = {'Title': "", 'Summary': "", "Entry_id": '', "PDF_URL": "", "Primary_category": ""}
        summary = str(result.summary)
        summary2 = summary.replace("\n", " ")
        document['Title'] = str(result.title)
        # document['Summary'] = str(result.summary)
        document['Summary'] = summary2
        document['Entry_id'] = str(result.entry_id)
        document['PDF_URL'] = str(result.pdf_url)
        document['Published'] = str(result.published)
        document['Authors'] = str(result.authors[1])
        document['Primary_category'] = str(result.primary_category)
        # print(document)
    #   print(str(result.authors))
        json_document = json.dumps(document)
        # return json_document
        return document