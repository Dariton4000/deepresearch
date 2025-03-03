# __VERY EARLY PREVIEW__

# DeepResearch

A research assistant tool that uses language models to help with research queries.

## Description

DeepResearch helps automate research tasks by using AI to process and analyze information. It can crawl websites, search the internet, and answer research questions using language models.

## Features

- Web crawling for information gathering
- Search capabilities
- AI-powered research assistant

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

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install lmstudio crawl4ai
   ```

## Usage

Run the main script and input your research query when prompted:

```bash
python main.py
```

## Configuration

The system currently uses LMStudio as the AI provider. You can configure this in the `env.py` file. (Well not currently)

## License

MIT
