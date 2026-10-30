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


