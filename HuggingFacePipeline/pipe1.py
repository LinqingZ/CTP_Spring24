from transformers import pipeline
classifier = pipeline("sentiment-analysis")
res = classifier("I have been waiting for a huggingface course my whole life.")
print(res)