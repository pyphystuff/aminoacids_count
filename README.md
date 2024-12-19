# aminoacids_count
# Amino Acid Frequency Analysis from PDB Files

This Python script allows you to fetch a PDB file from the RCSB database using the PDB ID, extract the amino acid sequence for **Chain A**, and analyze the frequency of amino acids. The analysis includes displaying a frequency table, an ASCII histogram, and a graphical histogram using `matplotlib`.

## Features:
- Fetch PDB file from RCSB database.
- Parse amino acid sequence from **Chain A**.
- Count amino acid frequencies and visualize data using:
  - Frequency table.
  - ASCII histogram.
  - Graphical histogram (with `matplotlib`).

## Requirements:
- Python 3.x
- `requests` library for fetching PDB files.
- `matplotlib` library for plotting histograms.

## Installation:

### 1. Clone the Repository:
```bash
git clone https://github.com/yourusername/amino-acid-frequency-analysis.git
cd amino-acid-frequency-analysis
