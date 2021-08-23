"""The AVACABA Sequence """

def acaSequence():
    count = 1
    sequence = 'a'
    charnum = 98

    while count != 26:
        sequence = sequence + chr(charnum) + sequence
        count += 1
        charnum += 1
    
    return sequence

output = acaSequence()

print(len(output))