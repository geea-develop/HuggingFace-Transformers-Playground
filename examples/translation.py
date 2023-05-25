# Translation
# Attempts to translate text to another language

from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
res = translator("Ce cours est produit par Hugging Face.")

print(res)