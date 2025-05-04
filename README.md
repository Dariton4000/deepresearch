# __VERY EARLY PREVIEW__

# DeepResearch

A research assistant tool that uses language models to help with research queries.

## Description

DeepResearch helps automate research tasks by using AI to process and analyze information. It can crawl websites, search the internet, and answer research questions using language models.

## Features

- Crawl websites and extract relevant information
- Search the internet for research queries
- Summarize content using language models
- Save research results to a file

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/deepresearch.git
   cd deepresearch
   ```

2. Create an python environment:
   ```bash
   python3 -m venv env
   ```
   
3. Activate the environment (Windows):
   ```bash
   .\env\Scripts\activate
   ``` 
 
3. Activate the environment(Linux):
   ```bash
   source env/bin/activate
   ``` 

4. Install dependencies in the environment:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

If not already activated, activate your environment.

Activate the environment (Windows):
   ```bash
   .\env\Scripts\activate
   ``` 
 
Activate the environment (Linux):
   ```bash
   source env/bin/activate
   ``` 

Run the main script and input your research query when prompted:

```bash
python main.py
```

## Configuration

The system currently uses LMStudio as the AI provider. You can configure this in the `env.py` file. (Well not currently)
