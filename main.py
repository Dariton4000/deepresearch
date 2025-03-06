import asyncio
from crawler import crawl
from router import lm, lm_structured



def main():
    request = input("Please enter the Topik that should be researched? \n")
    result = lm_structured(request)
    print(result)
    


#async def main():
#    result = await crawl("https://www.example.com")
#    print(result)


if __name__ == "__main__":
    main()