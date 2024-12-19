#aminoacids
import requests
import matplotlib.pyplot as plt
# Dictionary to map 3-letter amino acid codes to 1-letter codes
AMINO_ACIDS = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C",
    "GLU": "E", "GLN": "Q", "GLY": "G", "HIS": "H", "ILE": "I",
    "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P",
    "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V",
    "SEC": "U", "PYL": "O"  # Selenocysteine and Pyrrolysine
}

def fetch_pdb_file(pdb_id):
    """Fetch the PDB file from the RCSB PDB database."""
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise ValueError(f"Failed to fetch PDB file for ID {pdb_id}")

def parse_chain_a_sequence(pdb_data):
    """Parse the PDB data and extract the amino acid sequence for chain A."""
    sequence = []
    current_residue = None

    for line in pdb_data.splitlines():
        if line.startswith("ATOM"):  # Focus on ATOM records
            chain_id = line[21].strip()  # Chain identifier
            res_name = line[17:20].strip()  # Residue name
            res_seq = line[22:26].strip()  # Residue sequence number

            # Only consider Chain A
            if chain_id == "A" and res_seq != current_residue:
                current_residue = res_seq
                if res_name in AMINO_ACIDS:
                    sequence.append(AMINO_ACIDS[res_name])

    return "".join(sequence)

# Main script block
if __name__ == "__main__":
    pdb_id = input("Enter the PDB ID of the enzyme (e.g., 1AKE): ").strip().upper()
    try:
        # Fetch the PDB file
        pdb_data = fetch_pdb_file(pdb_id)
        
        # Extract and store the sequence for Chain A
        chain_a_sequence = parse_chain_a_sequence(pdb_data)
        
        if chain_a_sequence:
            print(f"Sequence for Chain A of PDB ID {pdb_id}:")
            print(chain_a_sequence)
            
            # Chain A sequence is now stored as a variable
            # You can directly use `chain_a_sequence` in your program
        else:
            print(f"No sequence found for Chain A in PDB ID {pdb_id}.")
    except ValueError as e:
        print(e)


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getLetterCount(message):
    """Returns a dictionary with keys of single letters and values of their count in the message."""
    # Initialize the letter count dictionary
    letterCount = {letter: 0 for letter in LETTERS}

    # Convert the message to uppercase and count valid letters
    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
    
    return letterCount

def plotHistogram(letterCount):
    """Plots a histogram of the letter frequencies."""
    letters = list(letterCount.keys())
    frequencies = list(letterCount.values())

    # Create the histogram
    plt.figure(figsize=(10, 6))
    plt.bar(letters, frequencies, color='skyblue', edgecolor='black')

    # Add titles and labels
    plt.title("Aminoacids Frequency Histogram", fontsize=16)
    plt.xlabel("Aminoacids", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Show the plot
    plt.tight_layout()
    plt.show()

def displayFrequencyTable(letterCount):
    """Displays a frequency table."""
    print("\nFrequency Table:")
    print(f"{'Aminoacid':<12}{'Frequency':<10}")
    print("-" * 25)
    for letter, count in letterCount.items():
        if count > 0:  # Only display letters with non-zero frequency
            print(f"{letter:<12}{count:<10}")
    print("-" * 25)

def displayAsciiHistogram(letterCount):
    """Displays an ASCII histogram of the letter frequencies."""
    print("\nASCII Histogram:")
    for letter, count in sorted(letterCount.items(), key=lambda x: x[1], reverse=True):
        if count > 0:  # Only display letters with non-zero frequency
            print(f"{letter}: {'*' * count}")

# Assume chain_a_sequence is already defined
# Example: chain_a_sequence = "MADTEYVQAK... (sequence)"

sequence = getLetterCount(chain_a_sequence)

# Display frequency table
displayFrequencyTable(sequence)

# Display ASCII histogram
displayAsciiHistogram(sequence)

# Plot graphical histogram
plotHistogram(sequence)
