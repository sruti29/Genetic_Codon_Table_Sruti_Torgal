# Codon Table Generator
Sruti Torgal  
MSc in Bioinformatics and Biotechnology  
Chanakya University

A Python program that accepts a DNA or RNA sequence and translates complete codons using the standard genetic code. It also reports GC content, codon and amino acid frequencies, estimated protein mass, complementary strands, and open reading frames (ORFs).

Built as part of my MSc coursework to practise dictionaries, string processing, input validation, and pandas DataFrames.

---

## Features

- Contains all 64 codons in the standard genetic code.
- Accepts DNA (`A`, `T`, `G`, `C`) or RNA (`A`, `U`, `G`, `C`) sequences.
- Rejects empty input, sequences containing both `T` and `U`, and invalid characters.
- Splits the sequence into codons (groups of three nucleotides).
- Maps each complete codon to its corresponding amino acid or stop signal.
- Identifies `ATG` start codons and `TAA`, `TAG`, and `TGA` stop codons after RNA-to-DNA normalisation.
- Reports incomplete trailing codons.
- Counts codon frequencies and amino acid frequencies.
- Estimates protein molecular mass in daltons (Da).
- Displays the complement and reverse complement.
- Calculates GC content as a percentage.
- Identifies ORFs within the reading frame analysed by the program.
- Displays codon-to-amino-acid mappings in a pandas DataFrame.

## Requirements

- Python 3.x
- pandas

Install pandas using:

```bash
python -m pip install pandas
```

If your system uses `python3` instead of `python`, replace `python` with `python3` in the commands below.

## How to Run

### Step 1: Open a terminal in the project folder

The folder should contain `main.py`. On Windows, open the folder in File Explorer and type `cmd` in the address bar. On macOS or Linux, navigate to the folder using `cd`.

List the files to confirm that `main.py` is present.

On macOS or Linux:

```bash
ls
```

In Windows Command Prompt:

```bat
dir
```

### Step 2: Install the dependency

```bash
python -m pip install pandas
```

Install the dependency in the Python environment you will use to run the program. If it is already installed, pip may display `Requirement already satisfied`.

### Step 3: Run the program

```bash
python main.py
```

### Step 4: Enter a sequence

The program prompts you for a DNA or RNA sequence:

```text
Total number of codons: 64
Enter a DNA or RNA sequence:
```

For example, enter `ATGAAATAAGGG` and press Enter.

### Step 5: Read the output

The program prints the analysis sections and then exits. According to the project description, results are not saved to disk. Repeat Step 3 to analyse another sequence.

## Example Output

For input `ATGAAATAAGGG`, the example below illustrates the documented output. The reverse complement has been corrected. The protein-mass value is omitted because its calculation cannot be verified without `main.py`; actual formatting and behaviour should also be checked against the script.

```text
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

Estimated protein mass: [verify using main.py]
Complement strand: TACTTTATTCCC
Reverse complement: CCCTTATTTCAT
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
```

`Stop` is a termination label, not an amino acid. It is shown in the frequency section to preserve the documented output format.

## Input Examples

| Input | Type | Expected result |
| --- | --- | --- |
| `ATGTTTGGT` | DNA | Translated normally. |
| `AUGUUUGGU` | RNA | Normalised and translated to the same result as the DNA example above. |
| `atgtttggt` | Lowercase DNA | Converted to uppercase and translated. |
| `ATGAAATAAGGG` | DNA | Analysed, including ORF detection. |
| `GGGCCC` | DNA | GC content of 100.00%. |
| Empty input | Empty | Rejected: the sequence cannot be empty. |
| `ATTGCATGCATUCG` | Mixed DNA/RNA | Rejected: contains both `T` and `U`. |
| `ATGXYZ` | Invalid | Rejected: contains invalid characters. |

## How It Works

1. **Codon table:** A dictionary maps each of the 64 DNA codons to an amino acid name or a stop label.
2. **Input validation:** Input is converted to uppercase and checked for empty input, invalid characters, and mixed `T`/`U` sequences.
3. **Normalisation:** RNA bases (`U`) are converted to DNA bases (`T`) so that one codon dictionary can serve both input types.
4. **Codon splitting:** The normalised sequence is divided into groups of three. Any remaining one or two bases are reported as an incomplete codon.
5. **Codon mapping:** Each complete codon is looked up in the dictionary. The documented program continues mapping codons after a stop codon.
6. **Sequence analysis:** Complementary strands and GC content are calculated from the nucleotide sequence. Codon mappings support frequency summaries and the protein-mass estimate. ORFs are identified from nucleotide start and stop codons.
7. **Output:** Results are printed section by section, ending with a pandas DataFrame.

## Limitations

- Only the first reading frame is analysed, beginning at nucleotide positions 1, 4, 7, and so on.
- Only the standard genetic code is supported; alternative genetic-code tables are not implemented.
- The protein-mass estimate is approximate. The mass values used, treatment of water, and handling of stop codons and post-stop residues need to be verified in `main.py`.
- Every complete codon is mapped, including codons after the first stop codon; this output should not be treated as one continuous protein product.
- Input is interactive only; command-line arguments and sequence-file input are not supported.
- Testing was performed manually; no automated test suite is included.

## Future Improvements

- Translate all three forward reading frames and optionally all six reading frames.
- Export results to CSV.
- Support alternative genetic codes.
- Add command-line arguments using `argparse`.
- Add automated unit tests using `unittest`.
- Plot codon usage as a bar chart using matplotlib.
- Document the protein-mass calculation and ORF-detection criteria explicitly.

## Project Structure

```text
codon-table-generator/
├── main.py
├── README.md
└── REPORT.md   # Optional full project report
```
