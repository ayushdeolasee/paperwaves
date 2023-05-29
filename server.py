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

search = arxiv.Search(
  query = "quantum",
  max_results = 10,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

for result in search.results():
#   document = {'Title': "", 'Summary': "", "Entry_id": '', "PDF_URL": "", "Published": "", "Authors": [], "Primary_category": ""}
  document = {'Title': "", 'Summary': "", "Entry_id": '', "PDF_URL": "", "Primary_category": ""}
  document['Title'] = str(result.title)
  document['Summary'] = str(result.summary)
  document['Entry_id'] = str(result.entry_id)
  document['PDF_URL'] = str(result.pdf_url)
#   document['Published'] = str(result.published)
#   document['Authors'] = str(result.authors)
  document['Primary_category'] = str(result.primary_category)
#   print(str(result.authors))
  json = json.dumps(document)
  print(json)