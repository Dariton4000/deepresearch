from env import provider
from providers.lm_studio import lm_studio, lm_studio_summarize, lm_studio_structured
import asyncio

async def lm_with_timeout(prompt, timeout):
    try:
        return await asyncio.wait_for(lm_studio(prompt), timeout)
    except asyncio.TimeoutError:
        return "Error: The request timed out."

async def lmsummarize_with_timeout(prompt, timeout):
    try:
        return await asyncio.wait_for(lm_studio_summarize(prompt), timeout)
    except asyncio.TimeoutError:
        return "Error: The request timed out."

def lm(prompt):
    if provider == "lmstudio":
        try:
            return asyncio.run(lm_with_timeout(prompt, 30))
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        print("No provider selected")
        return None
    

def lmsummarize(prompt):
    if provider == "lmstudio":
        try:
            return asyncio.run(lmsummarize_with_timeout(prompt, 30))
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        print("No provider selected")
        return None
    

def lm_structured(prompt):
    if provider == "lmstudio":
        return lm_studio_structured(prompt)
    else:
        print("No provider selected")
        return None
