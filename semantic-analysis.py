from transformers import pipeline

classifier = pipeline("sentiment-analysis")
res = classifier(
    [
        "I've been waiting for a HuggingFace course my whole life.",
        "I hate this so much!",
    ]
)

print(res)