#Programmer: 	Sepideh Zaeri	(Geneticist & Bioinformatician)
#Using Biopython as a library
#Sequence Analysis Script: Counting Nucleotide Frequencies in a DNA Sequence
#Purpose: This script reads a DNA sequence from a FASTA file and counts the frequency of each nucleotide (A, T, C, G).


from Bio import SeqIO

# Read a DNA sequence from a FASTA file
def count_nucleotides(fasta_file):
    nucleotide_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence = record.seq
        for nucleotide in sequence:
            if nucleotide in nucleotide_count:
                nucleotide_count[nucleotide] += 1
    return nucleotide_count

# Example usage
fasta_file = "FTSJ2 Homo sapiens.fasta"  # Replace with your FASTA file path
nucleotide_count = count_nucleotides(fasta_file)
print(nucleotide_count)
