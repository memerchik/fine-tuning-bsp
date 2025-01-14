import google.generativeai as genai
from google.generativeai import caching
import datetime
import argparse


INSTRUCTIONS_FOR_THE_LLM="""
You are tasked with summarizing articles provided in various formats (e.g., HTML files) into a concise JSON format. The JSON output must follow a specific structure with four required fields: "goal", "methods", "process", and "results". Each field must adhere to the following guidelines:

goal: Describe the overarching purpose of the article, written in present continuous form (e.g., "Analyzing...," "Exploring..."). Avoid starting with "To."
methods: Explain the techniques, tools, and methodologies used in the article. Format this field as an array of single-line sentences descibing each method.
process: Summarize the step-by-step approach or actions described in the article.
results: Highlight the key outcomes, findings, or conclusions derived from the article.
The JSON output must be formatted as a single line with no unnecessary whitespace, and each value must be encapsulated in double quotes. Ensure that the output is concise while maintaining accuracy, and write in a natural and professional tone.

Example Input: An article describing a computational analysis of Tacitus' vocabulary in political narratives.

Expected Output:

{"goal":"Analyzing Tacitus’ representation of crowds to explore their semantic, sociological, and political dimensions through computational and lexicological methods.","methods":"Combining natural language processing, manual annotation, and data visualization using tools like Pandas and Matplotlib to analyze occurrences and contexts of crowd-related terms such as vulgus, turba, and multitudo.","process":"Constructing a detailed CSV dataset with annotations for crowd-related terms, filtering irrelevant instances, and using visualization techniques to analyze term distributions and patterns across Tacitus’ works.","results":"Revealed nuanced distinctions in Tacitus’ vocabulary, with vulgus representing politically active crowds and turba/multitudo depicting disorderly groups, while demonstrating the potential of computational tools in classical scholarship."}
This formatting technique ensures consistency, accuracy, and clarity across all summaries.
"""

def initializationOfTheModel():
    model = genai.GenerativeModel(
        "models/gemini-1.5-flash",
        system_instruction=INSTRUCTIONS_FOR_THE_LLM,
    )

    with open("./template.txt", "r", encoding="utf-8") as file:
        article_text = file.read()

    response = model.generate_content(article_text)

    res = response.text.strip()

    if res[0]!="{" or res[-1]!="}":
        print(f"fail during the initialization. {res[0]} {res[-10:]}")
        return initializationOfTheModel()
    else:
        print("initialization successful")
        return model

def main():
    # creating the argument parser
    parser = argparse.ArgumentParser(description="A script to print a word passed as a console parameter.")
    
    parser.add_argument('-key', type=str, required=True, help="key for the gemini api")
    parser.add_argument('-article', type=str, required=True, help="file name of the article txt file")
    
    # parsing the arguments
    args = parser.parse_args()
    


    genai.configure(api_key=args.key)

    llm=initializationOfTheModel()

    with open(f"./{args.article}", "r", encoding="utf-8") as file:
            article2_text = file.read()

    response=llm.generate_content(article2_text)
    print(response.text)

if __name__ == "__main__":
    main()





