import csv
from collections import defaultdict

# Function to read click data from CSV file
def read_click_data(filename):
    click_data = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            click_data.append(row['page'])
    return click_data

# Function to compute transition probabilities
def compute_transition_probabilities(click_data):
    transitions = defaultdict(lambda: defaultdict(int))
    page_counts = defaultdict(int)
    
    # Treat "home.html" as the starting point for all transitions
    transitions['home.html'] = defaultdict(int)
    page_counts['home.html'] = len(click_data)  # Count the number of transitions from "home.html"
    
    # Count transitions and page occurrences
    for i in range(1, len(click_data)):
        transitions[click_data[i - 1]][click_data[i]] += 1
        page_counts[click_data[i - 1]] += 1
    
    # Calculate transition probabilities
    transition_probabilities = {}
    for source_page, target_pages in transitions.items():
        total_transitions = page_counts[source_page]
        probabilities = {target_page: count / total_transitions for target_page, count in target_pages.items() if target_page != 'home.html'}
        transition_probabilities[source_page] = probabilities
    
    return transition_probabilities

# Function to print Probability Matrix
def print_probability_matrix(transition_probabilities):
    print("Probability Matrix:")
    for source_page, probabilities in transition_probabilities.items():
        print(f"From {source_page}:")
        for target_page, probability in probabilities.items():
            print(f"  To {target_page}: Probability = {probability:.4f}")
        print()

# Read click data from CSV file
click_data = read_click_data('click_data.csv')

# Compute transition probabilities
transition_probabilities = compute_transition_probabilities(click_data)

# Print Probability Matrix
print_probability_matrix(transition_probabilities)