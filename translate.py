# change the sequence so it has a dna sequence to be translated.

from Bio.SeqUtils import six_frame_translations
sequence = '' 
sequence = sequence.replace(' ', '')
print(six_frame_translations(sequence))
