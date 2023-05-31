import arxiv
import json 

search = arxiv.Search(
    query = "quantum",
    max_results = 10,
    sort_by = arxiv.SortCriterion.SubmittedDate)

for result in search.results():
    finalDocument = {}
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
    document['Authors'] = str(result.authors[0])
    document['Primary_category'] = str(result.primary_category)
    # print(document)
#   print(str(result.authors))
    # json_document = json.dumps(document)
    finalDocument = finalDocument | document
    # print(document)
print(finalDocument)