
# Comparing a Custom Codon Table Against Three References

## Overview

This document compares a hardcoded codon table in `main.py` against three GitHub repositories that each approach codon tables from a different angle. The goal is to assess where the custom table fits, where it falls short, and what changes would make it more compatible with existing tools.

## The References

1. **linsalrob/genetic_codes** — A Python library that exposes all 26 NCBI genetic code tables, including Standard, Mitochondrial, and Bacterial. It allows querying any codon against any official table.
2. **Edinburgh-Genome-Foundry/python_codon_tables** — Provides codon *usage frequency* dictionaries for different organisms, sourced from Kazusa. Returns data shaped like `{'K': {'AAA': 0.76, 'AAG': 0.24}}`.
3. **mt1022/cubar** — An R package with a `create_codon_table()` function for building custom genetic codes. It expects structured tabular input with amino acid and codon columns.

## Comparison

### vs. linsalrob/genetic_codes

The custom table matches NCBI Table 1 exactly — all 64 codons map to the correct amino acids, and the stop codons are in the right places. That correctness is worth noting: the translation logic produces the right protein for any standard DNA sequence.

Beyond that, the similarities end. The reference library covers 26 NCBI tables, handles start codons as a separate built-in list, and treats stop codons as their own set. The custom code has none of this. It checks for `"ATG"` manually later in the script and treats `"Stop"` as just another amino acid value. The result is a script that works correctly for standard DNA but would silently produce wrong answers if given a mitochondrial sequence.

**What is done well:** the codon dictionary itself is accurate and easy to read. The one-to-one mapping is unambiguous, and the grouping by first base (T-block, C-block, A-block, G-block) makes it straightforward to spot-check against a reference. That organizational choice is genuinely helpful.

**What needs work:** the code around the table is less careful than the table itself. Start and stop codons are not treated as first-class concepts, and there is no fallback for codons outside the table. The table is solid; the logic built on top of it is where the gaps are.

### vs. python_codon_tables

This comparison is less about correctness and more about different purposes. The custom table maps `"TTT"` to `"Phenylalanine"` — it translates. The reference library maps `"F"` to `{"TTT": 0.57, "TTC": 0.43}` — it optimizes. They solve different problems.

**What is done well:** the custom table is self-contained and has no external dependencies beyond pandas. For a translation-only use case, that simplicity is an advantage. The U-to-T normalization is handled early, before codon splitting, which is the right place for it.

**What needs work:** the table has no room for frequency data at all. If codon optimization were ever needed, the table would require a full rewrite. The reference library also handles U-to-T conversion natively, while the custom code performs a manual `.replace("U", "T")` before splitting. It works, but it reads as a workaround rather than a design choice. The custom table is a translation table, and that is fine — as long as that scope is intentional.

### vs. cubar custom table support

The comparison here is mostly structural. cubar's `create_codon_table()` expects a data frame with clean columns and uses three-letter or one-letter amino acid codes. The custom table is a plain Python dict using full names like `"Aspartic acid"` and `"Glutamic acid"`.

**What is done well:** the full amino acid names are readable in output. When the script prints a translation dataframe or a list of amino acids, a reader immediately understands what they are looking at. That readability has real value for teaching or debugging.

**What needs work:** the naming choice means no other tool will accept the table without a conversion layer. cubar also supports non-standard genetic codes, which the custom code does not. The table is human-friendly but machine-unfriendly — a tradeoff that was made without much thought at the time. Using full names for display and one-letter codes for storage would give both benefits without the compatibility cost.

## What Works and What Does Not

**Works well:**
- The codon-to-amino-acid mapping is correct for NCBI Table 1.
- The dictionary is organized by first base, which makes it easy to scan and verify.
- U-to-T normalization happens before codon splitting, which is the correct order.
- The script is self-contained for translation-only use.

**Needs improvement:**
- No error handling for unexpected codons — `codon_table[codon]` will throw a `KeyError`.
- Start and stop codons are not treated as separate concepts.
- Full amino acid names block compatibility with other tools.
- No support for alternative genetic codes.
- No frequency data, so the table cannot be extended into codon optimization.

## Recommended Changes

The first fix is error handling. Currently, `codon_table[codon]` throws a `KeyError` on anything unexpected. At minimum, it should use `codon_table.get(codon, "Unknown")`. The second change is separating stop codons into their own set — this is cleaner than treating `"Stop"` as an amino acid value and matches how Biopython and linsalrob/genetic_codes handle it. The third change is switching to one-letter amino acid codes internally while keeping full names only for display. That would make the table compatible with cubar and python_codon_tables without needing a translation layer. None of these fixes are difficult, but they matter if the code is ever meant to be more than a learning exercise.
