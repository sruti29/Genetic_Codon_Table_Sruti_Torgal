import pandas as pd

codon_table = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine",
    "TTA": "Leucine", "TTG": "Leucine",
    "TCT": "Serine", "TCC": "Serine",
    "TCA": "Serine", "TCG": "Serine",
    "TAT": "Tyrosine", "TAC": "Tyrosine",
    "TAA": "Stop", "TAG": "Stop",
    "TGT": "Cysteine", "TGC": "Cysteine",
    "TGA": "Stop", "TGG": "Tryptophan",
    
    "CTT": "Leucine", "CTC": "Leucine",
    "CTA": "Leucine", "CTG": "Leucine",
    "CCT": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",
    "CAT": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGT": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",

    "ATT": "Isoleucine", "ATC": "Isoleucine",
    "ATA": "Isoleucine", "ATG": "Methionine",
    "ACT": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",
    "AAT": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "AGT": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GTT": "Valine", "GTC": "Valine",
    "GTA": "Valine", "GTG": "Valine",
    "GCT": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",
    "GAT": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",
    "GGT": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}

#Print the total number of codons.

print("Total number of codons:", len(codon_table))

#DNA/RNA Sequence input
sequence = input("Enter a DNA or RNA sequence: ").upper().strip()

#Sequence validation
if sequence == "":
    print("Error: Sequence cannot be empty.")

elif not all(base in "ATGC" for base in sequence) and \
     not all(base in "AUGC" for base in sequence):
    print("Error: Enter only A, T, G, C for DNA or A, U, G, C for RNA.")

else:
    print("Sequence accepted:", sequence)

#DNA/RNA Acceptance check
if sequence != "" and (
    all(base in "ATGC" for base in sequence) or
    all(base in "AUGC" for base in sequence)
):
    dna_sequence = sequence.replace("U", "T")

    codons = []

#Split the DNA Sequence into codon
for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i+3]
        codons.append(codon)

    incomplete_codon = dna_sequence[len(codons) * 3:]

    print("Codons:", codons)if incomplete_codon:
        print("Incomplete codon:", incomplete_codon)

#Translate the sequences into amini acid sequence
if sequence != "" and (
    all(base in "ATGC" for base in sequence) or
    all(base in "AUGC" for base in sequence)
):
    amino_acids = []

    for codon in codons:
        amino_acid = codon_table[codon]
        amino_acids.append(amino_acid)

    print("Amino acids:", amino_acids)

#Start and Stop codon
if sequence != "" and (
    all(base in "ATGC" for base in sequence) or
    all(base in "AUGC" for base in sequence)
):
    start_codons = []
    stop_codons = []

    for codon in codons:
        if codon == "ATG":
            start_codons.append(codon)

        if codon in ["TAA", "TAG", "TGA"]:
            stop_codons.append(codon)

    print("Start codons:", start_codons if start_codons else "None found")
    print("Stop codons:", stop_codons if stop_codons else "None found")

#Translation dataframe
if sequence != "" and (
    all(base in "ATGC" for base in sequence) or
    all(base in "AUGC" for base in sequence)
):
    translation_df = pd.DataFrame({
        "Codon": codons,
        "Amino Acid": amino_acids
    })

    print(translation_df)

#GC Content
def gc_content(dna_sequence):
    """Return GC content as a percentage (0.0 – 100.0)."""
    if not dna_sequence:
        return 0.0
    gc = sum(1 for base in dna_sequence if base in "GC")
    return gc / len(dna_sequence) * 100

dna_sequence = sequence.replace("U", "T")
codons = []
...
print("Amino acids:", amino_acids)

print(f"GC content: {gc_content(dna_sequence):.2f}%")

#CODON FREQUENCY COUNTER
from collections import Counter

codon_counts = Counter(codons)
print("\n=== Codon Frequencies ===")
for codon, count in codon_counts.most_common():
    print(f"{codon}: {count}")

#Amino acid frequency counter
aa_counts = Counter(amino_acids)
print("\n=== Amino Acid Frequencies ===")
for aa, count in aa_counts.most_common():
    print(f"{aa}: {count}")

#protein molecular weight estimate
AA_MASS = {
    "Alanine": 89.1, "Arginine": 174.2, "Asparagine": 132.1,
    "Aspartic acid": 133.1, "Cysteine": 121.2, "Glutamine": 146.2,
    "Glutamic acid": 147.1, "Glycine": 75.1, "Histidine": 155.2,
    "Isoleucine": 131.2, "Leucine": 131.2, "Lysine": 146.2,
    "Methionine": 149.2, "Phenylalanine": 165.2, "Proline": 115.1,
    "Serine": 105.1, "Threonine": 119.1, "Tryptophan": 204.2,
    "Tyrosine": 181.2, "Valine": 117.1, "Stop": 0.0,
}

def protein_mass(amino_acids):
    """Rough estimate of molecular weight in Daltons (excludes Stop)."""
    mass = sum(AA_MASS.get(aa, 0) for aa in amino_acids)
    # subtract water per peptide bond
    return mass - (max(len(amino_acids) - 1, 0) * 18.0)

print(f"Estimated protein mass: {protein_mass(amino_acids):.1f} Da")

#Complementary DNA strand
complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
comp_strand = "".join(complement[b] for b in dna_sequence)
print("Complement strand:", comp_strand)

#Reverse complement
reverse_complement = comp_strand[::-1]
print("Reverse complement:", reverse_complement)






