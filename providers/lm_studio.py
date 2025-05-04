import lmstudio
import lmstudio as lms
import asyncio
import time
import sys
import re


#will give you a response based on the given prompt
def lm_studio(prompt):
    try:
        model = lms.llm()
        full_response = ""
        # Stream the response to console
        for token in model.respond_stream(prompt):
            if hasattr(token, 'content'):
                # Extract content from LlmPredictionFragment object
                token_content = token.content
            else:
                # If it's already a string, use it directly
                token_content = str(token)
            
            print(token_content, end="", flush=True)
            full_response += token_content
        print()  # Add a newline at the end
        
        # Only return content after the last <think> tag if present
        think_pattern = r'<think>.*?</think>'
        last_think_match = list(re.finditer(think_pattern, full_response, re.DOTALL))
        
        if last_think_match:
            # Get the end position of the last </think> tag
            last_think_end = last_think_match[-1].end()
            # Return only what comes after the last </think> tag
            return full_response[last_think_end:].strip()
        else:
            # If no <think> tags found, return the full response
            return full_response
    except Exception as e:
        print(f"Error in lm_studio: {str(e)}")
        return f"Error: {str(e)}"

#will summarize given input into 3 or less sentences
def lm_studio_summarize(prompt):
    try:
        model = lms.llm("hermes-3-llama-3.2-3b")
        response = model.respond("Summarize the following into 3 or less informationrich sentences: " + prompt)
        return response
    except Exception as e:
        print(f"Error in lm_studio_summarize: {str(e)}")
        return f"Error: {str(e)}"

schema = {
  "type": "object",
  "properties": {
    "query1": { "type": "string" },
    "query2": { "type": "string" },
    "query3": { "type": "string" },
    "query4": { "type": "string" },
  },
  "required": ["query1", "query2", "query3", "query4"],
}

# for getting the research started
# this function will give you 4 google queries based on the research theme in json format
# the json format is defined in the schema variable
def lm_studio_structured(prompt):
    model = lms.llm()
    today = time.strftime("%B %d, %Y")
    result = model.respond("Give me 4 google queries based on the following research theme: " + prompt + " Keep in mind, today is the " + today + " and these should be queries for Google or Bing, so you should use clear and specific keywords. Do not include any dates in the queries because the information will be up to date anyways. All spaces in queries have to be replaced with +. The queries should also be concise and accurate to generate a comprehensive report. Do not hallucinate or make up any information; be sure to ask important information about " + prompt, response_format=schema)
    response = result.parsed
    return response
