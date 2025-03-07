import lmstudio
import lmstudio as lms
import asyncio
import time


#will give you a response based on the given prompt
def lm_studio(prompt):
    model = lms.llm()
    response = model.respond(prompt)
    return response

#will summarize given input into 3 or less sentences
def lm_studio_summarize(prompt):
    model = lms.llm()
    response = model.respond("Summarize the following into 3 or less sentences: " + prompt)
    return response

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
    result = model.respond("Give me 4 google queries based on the following research theme: " + prompt + " Keep in mind, today is the " + today + " and these should be queries for Google or Bing, so you should use clear and specific keywords. Do not include any dates in the queries because the information will be up to date anyways. The information should be enough to generate a report with it. Do not hallucinate or make up any information; be sure to ask important information about " + prompt, response_format=schema)
    response = result.parsed
    return response
