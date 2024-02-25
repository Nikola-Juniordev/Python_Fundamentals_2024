text = input()

sorted_text = [chr for chr in text if chr.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(sorted_text))