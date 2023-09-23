'''Complementary DNA'''


def DNA_strand(dna: str) -> str:
    # code here
    replace = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return ''.join([(replace[item]) for item in dna])


print(DNA_strand('AAAA'))     # must be TTTT
print(DNA_strand('ATTGC'))    # must be TAACG
print(DNA_strand('GTAT'))     # must be CATA
