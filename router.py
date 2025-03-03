from env import provider
from lm_studio import lm_studio, lm_studio_tools

def lm(prompt):
    if provider == "lmstudio":
        return lm_studio(prompt)
    else:
        print("No provider selected")
        return None
    

def lmtools(prompt):
    if provider == "lmstudio":
        return lm_studio_tools(prompt)
    else:
        print("No provider selected")
        return None
    