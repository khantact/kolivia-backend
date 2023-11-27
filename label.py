from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch, evaluate, accelerate
from transformers import TrainingArguments, Trainer
import glob
import numpy as np
from datasets import Dataset, load_dataset
import optuna
import random

if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

print(device)

model = AutoModelForSequenceClassification.from_pretrained(
    "model/distilbert-classifier", num_labels=3
).to(device)
tokenizer = AutoTokenizer.from_pretrained("model/distilbert-classifier", use_fast=True)


@torch.no_grad()
def getScore(
    review: str, model: AutoModelForSequenceClassification, tokenizer: AutoTokenizer
) -> str:
    model.eval()
    model = model.to("cpu")
    input_ids = tokenizer(review, return_tensors="pt", padding=True, truncation=True)
    output = model(**input_ids).logits
    pred = np.argmax(output, axis=-1).tolist()[0]
    if pred == 0:
        return "Appointments"
    elif pred == 1:
        return "Questions"
    elif pred == 2:
        return "Weather"


review = "What is the weather like today?"
print(getScore(review, model, tokenizer))
