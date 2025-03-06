from env import provider
from providers.lm_studio import lm_studio, lm_studio_summarize

def lm(prompt):
    if provider == "lmstudio":
        return lm_studio(prompt)
    else:
        print("No provider selected")
        return None
    

def lmsummarize(prompt):
    if provider == "lmstudio":
        return lm_studio_summarize(prompt)
    else:
        print("No provider selected")
        return None