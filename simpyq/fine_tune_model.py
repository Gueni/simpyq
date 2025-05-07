import torch
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split
import json

# Define paths
MODEL_PATH = r'D:\WORKSPACE\simpyq\simpyq\models\intent_model'
TOKENIZER_PATH = r'D:\WORKSPACE\simpyq\simpyq\models\tokenizer'
LABELS_PATH = r'D:\WORKSPACE\simpyq\simpyq\models\intent_labels.json'
TRAIN_DATA_PATH = './train_data.json'

# Load the tokenizer and labels
tokenizer = BertTokenizer.from_pretrained(TOKENIZER_PATH)

with open(LABELS_PATH, 'r') as f:
    label_map = json.load(f)

# Load training data (queries and corresponding operations)
def load_train_data():
    with open(TRAIN_DATA_PATH, 'r') as f:
        data = json.load(f)
    return data['queries'], data['labels']

queries, labels = load_train_data()

# Sample data loading
with open("train_data.json") as f:
    data = json.load(f)

labels = data["labels"]
label_to_id = data["label_to_id"]

# Validate that all labels exist in the dictionary
for label in labels:
    if label not in label_to_id:
        print(f"Warning: Label '{label}' not found in label_to_id")
    else:
        print(f"Label '{label}' mapped to ID: {label_to_id[label]}")

# Convert labels to their respective IDs
try:
    labels = [label_to_id[label] for label in labels]
    print(f"Labels mapped successfully: {labels}")
except KeyError as e:
    print(f"KeyError: {e}. Ensure all labels are included in label_to_id")


# Tokenize the input queries
inputs = tokenizer(queries, truncation=True, padding=True, max_length=128)

# Split the dataset into training and validation sets
train_inputs, val_inputs, train_labels, val_labels = train_test_split(
    inputs['input_ids'], labels, test_size=0.2, random_state=42
)

# Convert inputs and labels to PyTorch tensors
train_inputs = torch.tensor(train_inputs)
train_labels = torch.tensor(train_labels)
val_inputs = torch.tensor(val_inputs)
val_labels = torch.tensor(val_labels)

# Create a PyTorch dataset
class IntentDataset(torch.utils.data.Dataset):
    def __init__(self, inputs, labels):
        self.inputs = inputs
        self.labels = labels

    def __getitem__(self, idx):
        return {'input_ids': self.inputs[idx], 'labels': self.labels[idx]}

    def __len__(self):
        return len(self.inputs)

train_dataset = IntentDataset(train_inputs, train_labels)
val_dataset = IntentDataset(val_inputs, val_labels)

# Load pre-trained BERT model for classification
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=len(label_map))

# Define the training arguments
training_args = TrainingArguments(
    output_dir=MODEL_PATH,          # Output directory
    num_train_epochs=3,             # Number of training epochs
    per_device_train_batch_size=16, # Batch size for training
    per_device_eval_batch_size=64,  # Batch size for evaluation
    warmup_steps=500,               # Number of warmup steps
    weight_decay=0.01,              # Strength of weight decay
    logging_dir='./logs',           # Directory for storing logs
)

# Trainer
trainer = Trainer(
    model=model, 
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
)

# Start training
trainer.train()

# Save the model, tokenizer, and label map
model.save_pretrained(MODEL_PATH)
tokenizer.save_pretrained(TOKENIZER_PATH)

# Save the label map
with open(LABELS_PATH, 'w') as f:
    json.dump(label_map, f)

print("Model fine-tuned and saved!")
