import lmstudio
import lmstudio as lms
import asyncio



def lm_studio(prompt):
    model = lms.llm()
    response = model.respond(prompt)
    return response


def lm_studio_summarize(prompt):
    model = lms.llm()
    response = model.respond("Summarize the following into 3 or less sentences: " + prompt)
    return response