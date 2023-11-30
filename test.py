from duckduckgo_search import  DDGS

with DDGS() as ddgs:
    results = [r for r in ddgs.text('clippy',max_results=100)]
    print(results)
    print(results[0]['href'])
    print(results[1]['href'])