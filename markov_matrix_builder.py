import csv

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
    transitions = {}
    page_counts = {}
    
    # Count transitions and page occurrences
    for i in range(1, len(click_data)):
        source_page = click_data[i - 1]
        target_page = click_data[i]
        
        if source_page not in transitions:
            transitions[source_page] = {}
            page_counts[source_page] = 0
        
        if target_page not in transitions[source_page]:
            transitions[source_page][target_page] = 0
        
        transitions[source_page][target_page] += 1
        page_counts[source_page] += 1
    
    # Calculate transition probabilities
    transition_probabilities = {}
    for source_page, target_pages in transitions.items():
        total_transitions = page_counts[source_page]
        probabilities = {target_page: count / total_transitions for target_page, count in target_pages.items()}
        transition_probabilities[source_page] = probabilities
    
    return transition_probabilities

# Function to build the Markov Matrix
def build_markov_matrix(transition_probabilities):
    pages = sorted(transition_probabilities.keys())
    num_pages = len(pages)
    markov_matrix = [[0] * (num_pages + 1) for _ in range(num_pages + 1)]
    
    # Add labels for rows and columns
    markov_matrix[0][0] = "Pages"
    for i in range(1, num_pages + 1):
        markov_matrix[i][0] = pages[i - 1]
        markov_matrix[0][i] = pages[i - 1]
    
    for i, source_page in enumerate(pages):
        for j, target_page in enumerate(pages):
            if target_page in transition_probabilities[source_page]:
                markov_matrix[i + 1][j + 1] = transition_probabilities[source_page][target_page]
    
    return markov_matrix

# Read click data from CSV file
click_data = read_click_data('click_data.csv')

# Compute transition probabilities
transition_probabilities = compute_transition_probabilities(click_data)

# Build the Markov Matrix
markov_matrix = build_markov_matrix(transition_probabilities)

# Print the Markov Matrix
print("Markov Matrix:")
for row in markov_matrix:
    print(row)