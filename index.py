import arxiv
import logging

logging.basicConfig(level=logging.INFO)
paper = next(arxiv.Search(id_list=["1605.08386v1"]).results())

big_slow_client = arxiv.Client(
  page_size = 10,
  delay_seconds = 10,
  num_retries = 1
)

# Prints 1000 titles before needing to make another request.
for result in big_slow_client.results(arxiv.Search(query="quantum")):
  print(result.title)