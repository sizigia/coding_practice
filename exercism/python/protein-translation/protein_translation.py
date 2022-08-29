CODONS = {'AUG': 'Methionine',
          'UUU': 'Phenylalanine',
          'UUC': 'Phenylalanine',
          'UUA': 'Leucine',
          'UUG': 'Leucine',
          'UCU': 'Serine',
          'UCC': 'Serine',
          'UCA': 'Serine',
          'UCG': 'Serine',
          'UAU': 'Tyrosine',
          'UAC': 'Tyrosine',
          'UGU': 'Cysteine',
          'UGC': 'Cysteine',
          'UGG': 'Tryptophan',
          'UAA': 'STOP',
          'UAG': 'STOP',
          'UGA': 'STOP'}


def proteins(strand):
    n = 3
    codons = [(strand[i:i + n]) for i in range(0, len(strand), n)]

    proteins = []

    for codon in codons:
        if codon in ['UAA', 'UAG', 'UGA']:
            break
        else:
            proteins.append(CODONS[codon])

    return proteins
