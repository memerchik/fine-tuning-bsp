# AI Historical article summarizer

This repository contains tools and datasets for summarizing text using Google Gemini/HuggingFace API, together with fine-tuning pre-trained language models for specific tasks.

## Repository Structure

### Root Files
- **requirements.txt**: Contains the necessary dependencies for running the project.

### Directories

#### 1. `llm-summarizer`
This is the main directory containing the code of the final summarizer. 
- **summarizer.py**: The main script file. 
```bash
   cd llm-summarizer
   python3 summarizer.py -key="*put_your_api_key_here*" -article="test_article.txt"
```
- **template.txt**: An example unformatted article that is used for validation of the output during initialization process.
- **test_article.txt**: The article that is used for test summarization. All articles that need to be summarized must be placed alongside with this one and their name has to be passed to the script.

#### 2. `small-language-models-testing-local`
This directory contains code for summarizing articles using HuggingFace’s API. It includes:

- **article.json**: An example unformatted jupyter notebook input file that can be used for summarization after the formatting is performed.
- **summarizing-in-parts.py**: A script designed to summarize large articles by splitting them into smaller parts. This allows processing articles that exceed the token limit of the API.
- **summarizing-text.py**: A general script for summarizing articles using HuggingFace's summarization models.

#### 3. `small-language-models-testing-remote`
This directory contains datasets used for fine-tuning models remotely. It includes:

- **dataset-3-1.csv**: The final dataset containing input/output pairs that was used for fine tuning.
- **dataset-2.csv, dataset-3.csv, dataset.csv**: Additional and first versions of the final dataset.

##### Subdirectories
- **inputs**: Contains articles stored in HTML format. These articles are the raw inputs for the summarization process.
- **outputs**: Contains summarized versions of the articles stored in JSON format.
- **text_versions**: Contains the articles formatted as plain text (.txt) files before the summarization process.

### Additional Files
- **script.py**: A general-purpose script that may be used for tasks such as dataset management, preprocessing, or summarization workflows.

## Usage

### Setting Up the Environment
Install the required dependencies listed in `requirements.txt`:
```bash
pip3 install -r requirements.txt
```

### Local Summarization
To summarize large articles:
1. Place the article in the `text_for_summary` variable inside of the `summarizing-in-parts.py`.
2. Run the `summarizing-in-parts.py` script:
   ```bash
   python3 small-language-models-testing-local/summarizing-in-parts.py
   ```
3. For simpler tasks, use `summarizing-text.py`.

### Fine-Tuning Models
1. Use the datasets in the `small-language-models-testing-remote` directory.
2. Articles in the `inputs` folder serve as the raw input, and their summarized counterparts in `outputs` are used for fine-tuning the models.
3. Ensure proper dataset preparation and follow fine-tuning instructions provided by HuggingFace documentation.

### Text Preprocessing
- Articles in `text_versions` serve as intermediary plain text files for additional analysis or preprocessing before summarization.
