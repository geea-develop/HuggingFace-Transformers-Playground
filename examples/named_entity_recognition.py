# Named entity recognition (NER)
# Attempts to detect entities such as persons, locations, or organizations in text

from transformers import pipeline

ner = pipeline("ner", grouped_entities=True)
res = ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")

print(res)
