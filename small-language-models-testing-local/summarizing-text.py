from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# The text you want to summarize
text = """
The Hugging Face library is an open-source library that provides a wide range of natural language processing tools, 
including pre-trained models for text summarization, translation, text generation, and many more tasks. 
With the help of these models, developers can easily integrate advanced NLP capabilities into their applications 
without having to train models from scratch.
"""

# Run the summarization
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)

# Output the summary
print("Summary:", summary[0]['summary_text'])