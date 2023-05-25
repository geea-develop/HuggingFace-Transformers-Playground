# Semantic Analysis
# Attempts to detect the semantic (positive or negative) direction of the text
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
res = classifier(
    [
        "I've been waiting for a HuggingFace course my whole life.",
        "I hate this so much!",
    ]
)

print(res)