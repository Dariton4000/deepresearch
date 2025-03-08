import asyncio
from crawler import crawl, search
from router import lm, lm_structured
from providers.lm_studio import lm_studio_summarize
import json
import re
import os


def main():
    request = input("Please enter the Topik that should be researched? \n")
    queries = lm_structured(request)
    filterprompt = "RESPOND ONLY WITH URLS. Extract all relevant URLs from the following data related to: " + request + ". Return ONLY the URLs with each URL on a separate line. No numbering, no brackets, no explanations, no introductions, no formatting. ONLY return plain URLs that can be processed by a web crawler. The data: "
    
    # Set to store all collected links (using a set for efficient duplicate filtering)
    all_links_set = set()
    
    # URL validation regex pattern
    url_pattern = re.compile(r'^https?://[^\s]+$')
    
    # Process each query and collect links
    for i in range(1, 5):
        query_key = f"query{i}"
        print()
        print("Now searching for " + queries[query_key])
        result = asyncio.run(search(queries[query_key]))
        links = lm(filterprompt + result)
        
        # Filter duplicate links and ensure they're proper URLs
        query_links = []
        if links.strip():
            for link in links.strip().split('\n'):
                link = link.strip()
                # Only add if it's a valid URL (starts with http:// or https://)
                if link and url_pattern.match(link) and link not in query_links:
                    # Filter out Google search URLs and other non-relevant sites
                    if not (link.startswith('https://www.google.com/') or 
                            link.startswith('https://accounts.google.com/') or 
                            link.startswith('https://support.google.com/') or 
                            link.startswith('https://policies.google.com/')):
                        # Make sure URL is relevant to the topic (contains the topic keywords)
                        if request.lower().replace(' ', '') in link.lower().replace(' ', ''):
                            query_links.append(link)
                        # Or if URL is from trusted sources like OpenAI or contains 'gpt'
                        elif ('openai' in link.lower() or 'gpt' in link.lower()):
                            query_links.append(link)
        
        # Print deduplicated results for this query
        print("\n".join(query_links))
        
        # Add to the global links set
        all_links_set.update(query_links)
    
    # Convert set back to list to maintain control over the final order
    all_links = list(all_links_set)
    
    # Print all collected unique links after all queries complete
    print("\n\n=== ALL COLLECTED LINKS ===")
    for link in all_links:
        print(link)
    
    # Crawl all collected links
    print("\n\n=== CRAWLING ALL LINKS ===")
    crawl_results = []
    for link in all_links:
        try:
            print(f"\nCrawling: {link}")
            content = asyncio.run(crawl(link))
            print(f"Successfully crawled: {link}")
            
            # Summarize the content using lm_studio_summarize
            print(f"Summarizing content from: {link}")
            try:
                summary = lm_studio_summarize(content)
                print(f"\nLink: {link}")
                print(f"Summary: {summary}\n")
                
                # Create a serializable dictionary instead of using complex objects
                crawl_results.append({
                    "url": link, 
                    "content": str(content)[:10000],  # Limit content size and convert to string
                    "summary": str(summary)  # Ensure summary is a string
                })
            except Exception as e:
                print(f"Error summarizing {link}: {str(e)}")
                # Still add the link and content without the summary
                crawl_results.append({
                    "url": link, 
                    "content": str(content)[:10000],
                    "summary": f"Error generating summary: {str(e)}"
                })
        except Exception as e:
            print(f"Error crawling {link}: {str(e)}")
    
    # Create a directory for storing research results if it doesn't exist
    results_dir = os.path.join(os.getcwd(), "research_results")
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        print(f"Created directory: {results_dir}")
    
    # Save crawl results to a file in the research_results directory
    result_filename = f"{request.replace(' ', '_')}_research.json"
    result_filepath = os.path.join(results_dir, result_filename)
    
    try:
        with open(result_filepath, "w", encoding="utf-8") as f:
            json.dump(crawl_results, f, ensure_ascii=False, indent=2, default=str)
        print(f"\nCrawl results saved to {result_filepath}")
    except Exception as e:
        print(f"Error saving results to JSON: {str(e)}")
        # Fallback to a text file
        with open(result_filepath.replace(".json", ".txt"), "w", encoding="utf-8") as f:
            for result in crawl_results:
                f.write(f"URL: {result['url']}\n\n")
                f.write(f"SUMMARY: {result['summary']}\n\n")
                f.write("-" * 80 + "\n\n")
        print(f"\nCrawl results saved to {result_filepath.replace('.json', '.txt')} (fallback text format)")


if __name__ == "__main__":
    main()