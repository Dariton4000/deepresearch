# __VERY EARLY PREVIEW__

# DeepResearch

A research assistant tool that uses language models to help with research queries.

## Description

DeepResearch helps automate research tasks by using AI to process and analyze information. It can crawl websites, search the internet, and answer research questions using language models.

## Features (how it will work in the future, still WIP)

![image](https://github.com/user-attachments/assets/767bcf30-b6ad-455d-8be1-4139d122797e)

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

If not allready activated, actevate your environment.

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
