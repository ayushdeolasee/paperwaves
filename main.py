# import arxiv
# import json 

# search = arxiv.Search(
#     query = "quantum+physics",
#     max_results = 10,
#     sort_by = arxiv.SortCriterion.SubmittedDate)

# for result in search.results():
#     finalDocument = {}
#     document = {'Title': "", 'Summary': "", "Entry_id": '', "PDF_URL": "", "Published": "", "Authors": [], "Primary_category": ""}
# #   document = {'Title': "", 'Summary': "", "Entry_id": '', "PDF_URL": "", "Primary_category": ""}
#     summary = str(result.summary)
#     summary2 = summary.replace("\n", " ")
#     document['Title'] = str(result.title)
#     # document['Summary'] = str(result.summary)
#     document['Summary'] = summary2
#     document['Entry_id'] = str(result.entry_id)
#     document['PDF_URL'] = str(result.pdf_url)
#     document['Published'] = str(result.published)
#     document['Authors'] = str(result.authors[0])
#     # print(len(result.authors))
#     document['Primary_category'] = str(result.primary_category)
#     print(document)
#     # print(document)
# #   print(str(result.authors))
#     # json_document = json.dumps(document)
#     # print(document)
#     # print(document)

import requests
import json
import xmltodict

url = "https://export.arxiv.org/api/query?search_query=quantum+physics&start=0&max_results=10"

response = requests.get(url)

if response.status_code == 200:
    xml_data = response.text
    data_dict = xmltodict.parse(xml_data)
    final_document = {}
    document = data_dict
    entry = document["feed"]["entry"]
    # for i in entry:
    if all(k in i for k in ("arxiv:comment", "arxiv:primary_category")):
        del i["link"]
        print("Works")
        # print(i["category"][1])
        # print(i)
        # print(i["arxiv:comment"])
        # del lists[6]
        # del lists[7]
        # print(i["category"]["@term"])
    # del entry[8]
    # print(entry)
else:
    print("Error:", response.status_code)
