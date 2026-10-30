# Codon Table Generator
Sruti Torgal
MSc. Bioinformatics & Biotechnology
Chanakya university


A Python program that takes a DNA or RNA sequence and translates it into the corresponding amino acid sequence using the standard genetic code. Along with translation, it reports GC content, codon and amino acid frequencies, estimated protein mass, complement strands, and open reading frames (ORFs).

Built as part of my MSc coursework to practise dictionaries, string processing, input validation, and pandas DataFrames.

---

## Features

- Full 64-codon standard genetic code table
- Accepts DNA (A, T, G, C) or RNA (A, U, G, C) sequences
- Input validation — rejects empty input, mixed T/U sequences, and invalid characters
- Splits the sequence into codons (triplets of three)
- Translates each codon into its corresponding amino acid
- Detects start codons (`ATG`) and stop codons (`TAA`, `TAG`, `TGA`)
- Reports any incomplete trailing codon
- Counts codon frequencies
- Counts amino acid frequencies
- Estimates protein molecular weight in Daltons
- Displays the complement and reverse complement strands
- Calculates GC content as a percentage
- Finds open reading frames (ORFs)
- Displays the final translation as a pandas DataFrame

---

## Requirements

- Python 3.x
- pandas

Install pandas if you don't have it:

```bash
pip install pandas


## How to Run — Step by Step
Step 1 — Open a terminal in the project folder
The folder should contain main.py. On Windows, you can open a terminal in that folder by right-clicking and choosing "Open in Terminal" (or typing cmd in the address bar of File Explorer). On Mac/Linux, cd into the folder.

To confirm you're in the right place, run:

bash
ls
You should see main.py listed.

Step 2 — Install the dependency
bash
pip install pandas
You only need to do this once. If pandas is already installed, pip will say "Requirement already satisfied" — that's fine.

Step 3 — Run the program
bash
python main.py
(On some systems you may need python3 main.py instead of python main.py.)

Step 4 — Enter a sequence when prompted
The program will first print the codon count and then wait for your input:

text
Total number of codons: 64
Enter a DNA or RNA sequence: 
Type a sequence (e.g. ATGAAATAAGGG) and press Enter.

Step 5 — Read the output
The program prints all analysis sections in order, then exits. Nothing is saved to disk.

To run again, repeat Step 3.

## EXAMPLE OUTPUT
For input ATGAAATAAGGG:

text
Total number of codons: 64
Sequence accepted: ATGAAATAAGGG
Codons: ['ATG', 'AAA', 'TAA', 'GGG']
Amino acids: ['Methionine', 'Lysine', 'Stop', 'Glycine']
Start codons: ['ATG']
Stop codons: ['TAA']

=== Codon Frequencies ===
ATG: 1
AAA: 1
TAA: 1
GGG: 1

=== Amino Acid Frequencies ===
Methionine: 1
Lysine: 1
Stop: 1
Glycine: 1

Estimated protein mass: 418.5 Da
Complement strand: TACTTTATTCCC
Reverse complement: CCCTTAATTTAT
GC content: 25.00%

=== Open Reading Frames (ORFs) ===
ORF at 1-9: ATGAAATAA
  Amino acids: ['Methionine', 'Lysine', 'Stop']

=== Translation Table ===
  Codon     Amino Acid
0   ATG     Methionine
1   AAA         Lysine
2   TAA           Stop
3   GGG        Glycine

## VALID INPUT EXAMPLES
Input	Type	Result
ATGTTTGGT	DNA	Translates normally
AUGUUUGGU	RNA	Translates normally (same result)
atgtttggt	DNA (lowercase)	Converted to uppercase and translated
ATGAAATAAGGG	DNA	Full output with ORFs detected
GGGCCC	DNA	GC content 100.00%
(blank)	—	Error: sequence cannot be empty
ATTGCATGCATUCG	Mixed	Error: contains both T and U
ATGXYZ	Invalid	Error: invalid characters

## HOW IT WORKS
Codon table — a dictionary maps each of the 64 codons to its amino acid name. Lookup is O(1) per codon.

Input validation — the raw input is uppercased and checked to confirm it's pure DNA or pure RNA (no mixing, no invalid characters).

Normalisation — RNA sequences have U converted to T so one dictionary serves both.

Codon splitting — the sequence is sliced into groups of three. Any trailing one or two bases are reported as an incomplete codon.

Translation — each codon is looked up to get its amino acid.

Analysis features — start/stop codons, frequencies, protein mass, complement strands, GC content, and ORFs are all computed from the translated sequence.

Output — printed section by section, ending with a pandas DataFrame of the codon-to-amino-acid mapping.

## LIMITATIONS
Only the first reading frame is translated (positions 1, 4, 7, …). Other frames aren't analysed.

Uses the standard genetic code only — mitochondrial or bacterial variants aren't supported.

Protein mass is a rough estimate using average residue masses, not exact molecular weights.

Doesn't stop translating at the first stop codon — every complete codon is translated.

Input is interactive only. No command-line arguments or file input.

No automated test suite; testing was done manually.

## FUTURE IMPROVEMENT
Translate in all three reading frames

Export results to CSV

Support variant genetic codes

Add command-line arguments with argparse

Add automated unit tests with unittest

Plot codon usage as a bar chart with matplotlib

## Project Structure
codon-table-generator/
├── main.py
├── README.md
└── REPORT.md   (optional — full project report)

## Reference





---
