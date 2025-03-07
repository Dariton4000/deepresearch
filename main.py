import asyncio
from crawler import crawl, search
from router import lm, lm_structured
import json




def main():
    request = input("Please enter the Topik that should be researched? \n")
    queries = lm_structured(request)
    filterprompt = "Please only provite the links that are relevant to the research theme: " + request + "provide them in this format: [link1, link2, link3, link4, and so on]. DO NOT PROVIDE ANY EXTRA TEXT, JUST THE LINKS. Here is the data: "
    
    for i in range(1, 5):
        query_key = f"query{i}"
        result = asyncio.run(search(queries[query_key]))
        print(lm(filterprompt + result))
        

#async def main():
#    result = await crawl("https://www.example.com")
#    print(result)


if __name__ == "__main__":
    main()