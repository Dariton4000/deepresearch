from lmstudio import ToolFunctionDef, Chat
import lmstudio as lms
from crawler import crawl, search
import asyncio



def lm_studio(prompt):
    model = lms.llm()
    response = model.respond(prompt)
    return response


def lm_studio_tools(prompt):
    model = lms.llm()    
    chat.add_user_message(prompt)
    
    # Let the model use the crawler tool
    tool_execution = model.act(
        prompt,
        [crawl],
    )
    response = model.respond(chat)
    return response



def sync_crawl(url):
    """A synchronous wrapper for the async crawl function."""
    return asyncio.run(crawl(url))


search = ToolFunctionDef(
    name="Search",
    description="Searches google with the provided query.",
    parameters={
        "query": str,
    },
    implementation=sync_search,
)

crawl = ToolFunctionDef(
    name="web_crawler",
    description="A web crawler that can scrape a specified link for information.",
    parameters={
        "url": str,
    },
    implementation=sync_crawl,
)