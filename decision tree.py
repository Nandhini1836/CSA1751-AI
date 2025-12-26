import math
from collections import Counter, defaultdict

# ---------------------------------------
# DATASET (FROM YOUR NOTEBOOK)
# ---------------------------------------

data = [
    {"Outlook": "Sunny",    "Temp": "Hot",  "Humidity": "High",   "Wind": "Weak",   "Play": "No"},
    {"Outlook": "Sunny",    "Temp": "Hot",  "Humidity": "High",   "Wind": "Strong", "Play": "No"},
    {"Outlook": "Overcast", "Temp": "Hot",  "Humidity": "High",   "Wind": "Weak",   "Play": "Yes"},
    {"Outlook": "Rain",     "Temp": "Mild", "Humidity": "High",   "Wind": "Weak",   "Play": "Yes"},
    {"Outlook": "Rain",     "Temp": "Cool", "Humidity": "Normal", "Wind": "Weak",   "Play": "Yes"},
    {"Outlook": "Rain",     "Temp": "Cool", "Humidity": "Normal", "Wind": "Strong", "Play": "No"},
    {"Outlook": "Overcast", "Temp": "Cool", "Humidity": "Normal", "Wind": "Strong", "Play": "Yes"},
    {"Outlook": "Sunny",    "Temp": "Mild", "Humidity": "High",   "Wind": "Weak",   "Play": "No"},
    {"Outlook": "Sunny",    "Temp": "Cool", "Humidity": "Normal", "Wind": "Weak",   "Play": "Yes"},
    {"Outlook": "Rain",     "Temp": "Mild", "Humidity": "Normal", "Wind": "Weak",   "Play": "Yes"}
]

TARGET = "Play"

# ---------------------------------------
# ENTROPY
# ---------------------------------------

def entropy(data):
    total = len(data)
    counts = Counter(row[TARGET] for row in data)

    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent

# ---------------------------------------
# INFORMATION GAIN
# ---------------------------------------

def information_gain(data, attribute):
    total_entropy = entropy(data)
    total = len(data)

    subsets = defaultdict(list)
    for row in data:
        subsets[row[attribute]].append(row)

    weighted_entropy = 0
    for subset in subsets.values():
        weighted_entropy += (len(subset) / total) * entropy(subset)

    return total_entropy - weighted_entropy

# ---------------------------------------
# ID3 ALGORITHM
# ---------------------------------------

def id3(data, attributes):
    labels = [row[TARGET] for row in data]

    if labels.count(labels[0]) == len(labels):
        return labels[0]

    if not attributes:
        return Counter(labels).most_common(1)[0][0]

    gains = {attr: information_gain(data, attr) for attr in attributes}
    best_attr = max(gains, key=gains.get)

    tree = {best_attr: {}}

    values = set(row[best_attr] for row in data)

    for value in values:
        subset = [row for row in data if row[best_attr] == value]
        remaining_attrs = [a for a in attributes if a != best_attr]
        tree[best_attr][value] = id3(subset, remaining_attrs)

    return tree

# ---------------------------------------
# RUN DECISION TREE
# ---------------------------------------

attributes = ["Outlook", "Temp", "Humidity", "Wind"]
decision_tree = id3(data, attributes)

print("\nDECISION TREE OUTPUT:\n")
print(decision_tree)



EXAMPLE 2



import math
from collections import Counter, defaultdict

# -----------------------------
# STEP 1: DATASET (QUESTION)
# -----------------------------

data = [
    {'Q1':'True',  'Q2':'Hot',  'Q3':'High',   'Class':'No'},
    {'Q1':'True',  'Q2':'Hot',  'Q3':'High',   'Class':'No'},
    {'Q1':'False', 'Q2':'Hot',  'Q3':'High',   'Class':'Yes'},
    {'Q1':'False', 'Q2':'Cool', 'Q3':'Normal', 'Class':'Yes'},
    {'Q1':'False', 'Q2':'Cool', 'Q3':'Normal', 'Class':'Yes'},
    {'Q1':'False', 'Q2':'Cool', 'Q3':'High',   'Class':'No'},
    {'Q1':'True',  'Q2':'Hot',  'Q3':'High',   'Class':'No'},
    {'Q1':'True',  'Q2':'Hot',  'Q3':'Normal', 'Class':'Yes'},
    {'Q1':'False', 'Q2':'Cool', 'Q3':'Normal', 'Class':'Yes'},
    {'Q1':'False', 'Q2':'Cool', 'Q3':'High',   'Class':'Yes'}
]

TARGET = 'Class'

# -----------------------------
# STEP 2: ENTROPY
# -----------------------------

def entropy(data):
    total = len(data)
    counts = Counter(row[TARGET] for row in data)

    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent

# -----------------------------
# STEP 3: INFORMATION GAIN
# -----------------------------

def information_gain(data, attribute):
    total_entropy = entropy(data)
    total = len(data)

    subsets = defaultdict(list)
    for row in data:
        subsets[row[attribute]].append(row)

    weighted_entropy = 0
    for subset in subsets.values():
        weighted_entropy += (len(subset) / total) * entropy(subset)

    return total_entropy - weighted_entropy

# -----------------------------
# STEP 4: ID3 ALGORITHM
# -----------------------------

def id3(data, attributes):
    labels = [row[TARGET] for row in data]

    # All same class
    if labels.count(labels[0]) == len(labels):
        return labels[0]

    # No attributes left
    if not attributes:
        return Counter(labels).most_common(1)[0][0]

    # Choose best attribute
    gains = {attr: information_gain(data, attr) for attr in attributes}
    best_attr = max(gains, key=gains.get)

    tree = {best_attr: {}}
    remaining_attrs = [a for a in attributes if a != best_attr]

    values = set(row[best_attr] for row in data)
    for value in values:
        subset = [row for row in data if row[best_attr] == value]
        tree[best_attr][value] = id3(subset, remaining_attrs)

    return tree

# -----------------------------
# STEP 5: BUILD TREE
# -----------------------------

attributes = ['Q1', 'Q2', 'Q3']
decision_tree = id3(data, attributes)

# -----------------------------
# STEP 6: PRINT TREE
# -----------------------------

def print_tree(tree, indent=""):
    if not isinstance(tree, dict):
        print(indent + "→", tree)
        return
    for key in tree:
        for value in tree[key]:
            print(indent + f"[{key} = {value}]")
            print_tree(tree[key][value], indent + "  ")

print("\nDECISION TREE (ID3):\n")
print_tree(decision_tree)
