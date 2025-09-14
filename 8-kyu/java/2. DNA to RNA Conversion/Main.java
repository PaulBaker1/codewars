/**
 * Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems.
 *  It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

    Ribonucleic acid, RNA, is the primary messenger molecule in cells.
    RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

    Create a function which translates a given DNA string into RNA.

    For example:

    "GCAT"  =>  "GCAU"
    The input string can be of arbitrary length - in particular, it may be empty.
    All input is guaranteed to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.
 * 
 */

public class Main {
    public static String toRna(String dna) {
        // Create a StringBuilder to build the RNA sequence
        StringBuilder rna = new StringBuilder();
        
        // Iterate over each character in the DNA string
        for (char base : dna.toCharArray()) {
            // Replace 'T' with 'U'
            if (base == 'T') {
                rna.append('U'); 
            } else {
                rna.append(base);
            }
        }
        return rna.toString();
    }

    public static void main(String[] args) {
        String dna = "GCAT";
        String rna = toRna(dna);
        System.out.println(rna); // Output: GCAU
    }
}
