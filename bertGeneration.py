from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch, evaluate, accelerate
from transformers import TrainingArguments, Trainer
import glob
import numpy as np
from datasets import Dataset, load_dataset
import optuna
from evaluate import evaluator
import random

# Set device depending on whether or not you have access to GPUs
if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

# modelname = "distilbert-base-cased"
# tokenizer = AutoTokenizer.from_pretrained(modelname, use_fast=True)
# model = AutoModelForSequenceClassification.from_pretrained(modelname, num_labels=3).to(
#     device
# )


def loadData(path):
    """Loads data from a directory and labels it
        Appointments = 0
        Questions = 1
        Weather = 2
    Args:
        path (str): path to directory

    Returns:
        toRet: list of dictionaries with text and label
    """
    toRet = []
    appointments = path + "appointments.txt"
    questions = path + "questions.txt"
    weather = path + "weather.txt"
    fileList = [appointments, questions, weather]
    for files in fileList:
        with open(files, "r", encoding="utf-8") as f:
            data = f.read()
            for line in data.split("\n"):
                if files == appointments:
                    toRet.append({"text": line, "label": 0})
                elif files == questions:
                    toRet.append({"text": line, "label": 1})
                elif files == weather:
                    toRet.append({"text": line, "label": 2})
    return toRet


def getDataset(
    path: str,
    tokenizer: AutoTokenizer = None,
    tokenize: bool = True,
    percent: float = 0.25,
) -> Dataset:
    """Return HuggingFace Dataset instance
    Args:
        path (str): path to directory
        tokenizer (AutoTokenizer): A HuggingFace pre-trained tokenizer
        tokenize (bool): Whether to tokenize data. Default True
    Returns:
        (Dataset): HuggingFace Dataset instance
    """
    data = loadData(path)
    # Shuffle the data
    random.shuffle(data)
    data = data[: int(len(data) * percent)]
    data = Dataset.from_list(data)
    # Tokenize
    if tokenize:
        if tokenizer is None:
            print("Pass a tokenizer")
            return
        data = data.map(
            lambda examples: tokenizer(
                examples["text"], return_tensors="pt", padding=True, truncation=True
            ),
            batched=True,
        ).with_format("torch")
    return data


# smallDataset = getDataset(
#     path="data/train_data/",
#     tokenizer=tokenizer,
#     percent=0.05,
# )
# trainDataset = getDataset(
#     path="data/train_data/",
#     tokenizer=tokenizer,
#     percent=0.25,
# )
# evalDataset = getDataset(path="data/eval_data/", tokenizer=tokenizer)


def model_init():
    return AutoModelForSequenceClassification.from_pretrained(
        modelname, num_labels=2
    ).to(device)


# Uses accuracy is the metric at eval steps
metric = evaluate.load("accuracy")


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)


# Set some initial parameters
# batch_size = 20
# args = TrainingArguments(
#     f"{modelname}-finetuned-appointment-classifications",
#     evaluation_strategy="epoch",
#     save_strategy="epoch",
#     learning_rate=2e-5,
#     per_device_train_batch_size=batch_size,
#     per_device_eval_batch_size=batch_size,
#     num_train_epochs=2,
#     weight_decay=0.01,
# )

# # Set up a trainer with less data
# trainer = Trainer(
#     model_init=model_init,
#     args=args,
#     train_dataset=smallDataset,
#     eval_dataset=evalDataset,
#     tokenizer=tokenizer,
#     compute_metrics=compute_metrics,
# )
# print("finding hyperparams")
# # Find the best hyperparameters over 10 runs
# best_run = trainer.hyperparameter_search(
#     n_trials=2, direction="maximize", backend="optuna"
# )

# model = AutoModelForSequenceClassification.from_pretrained(modelname, num_labels=3).to(
#     device
# )
# trainer = Trainer(
#     model=model,
#     args=args,
#     train_dataset=trainDataset,
#     eval_dataset=evalDataset,
#     tokenizer=tokenizer,
#     compute_metrics=compute_metrics,
# )

# for n, v in best_run.hyperparameters.items():
#     setattr(trainer.args, n, v)
# trainer.train()
# load pretrained model

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-cased-finetuned-appointment-classifications/checkpoint-1302",
    num_labels=3,
).to(device)

tokenizer = AutoTokenizer.from_pretrained(
    "distilbert-base-cased-finetuned-appointment-classifications/checkpoint-1302"
)
smallDataset = getDataset(
    path="data/train_data/",
    tokenizer=tokenizer,
    percent=0.05,
)
trainDataset = getDataset(
    path="data/train_data/",
    tokenizer=tokenizer,
    percent=0.25,
)
evalDataset = getDataset(path="data/eval_data/", tokenizer=tokenizer)

print("evaluating")

task_evaluator = evaluate.evaluator("text-classification")
model.eval()
model.to("cpu")
# metrics
metric1 = evaluate.load("accuracy")
metric2 = evaluate.load("f1")
metric3 = evaluate.load("precision")
metric4 = evaluate.load("recall")


def computeModelMetrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    accuracy = metric1.compute(predictions=predictions, references=labels)["accuracy"]
    f1 = metric2.compute(predictions=predictions, references=labels, average="micro")[
        "f1"
    ]
    precision = metric3.compute(
        predictions=predictions, references=labels, average="micro"
    )["precision"]
    recall = metric4.compute(
        predictions=predictions, references=labels, average="micro"
    )["recall"]
    return {"precision": precision, "recall": recall, "f1": f1, "accuracy": accuracy}


batch_size = 5
args = TrainingArguments(
    f"finetuned-appointment-classifications",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    num_train_epochs=2,
    weight_decay=0.01,
)

trainer = Trainer(
    model,
    args,
    train_dataset=trainDataset,
    eval_dataset=evalDataset,
    tokenizer=tokenizer,
    compute_metrics=computeModelMetrics,
)
predictions = trainer.predict(evalDataset)
print(predictions)

# evaluate.combine(["accuracy", "recall", "precision", "f1"]),
# results = task_evaluator.compute(
#     model_or_pipeline=model,
#     tokenizer=tokenizer,
#     data=testDataset,
#     metric=evaluate.combine(["accuracy", "recall", "precision", "f1"]),
#     label_mapping={"LABEL_0": 0.0, "LABEL_1": 1.0, "LABEL_2": 2.0},
# )
# print(results)
trainer.save_model(output_dir="model/distilbert-classifier")
