import asyncio
from crawler import crawl
from router import lm, lmtools



def main():
    request = input("What would you like to research? \nType it in here: ")
    result = lmtools("You are a research assistant. Do not Halucinate any information. Please help me with this query: " + request)
    print(result)
    


#async def main():
#    result = await crawl("https://www.example.com")
#    print(result)


if __name__ == "__main__":
    main()