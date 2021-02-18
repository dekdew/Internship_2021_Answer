'''
    Question: [1] Sorting Acronyms
    Author: Passawit Riewthong
'''

amount = int(input())  # Get number of names
acronymsNames = []  # A list of Acronyms Names

# Get each name and convert to acronyms
for _ in range(amount):
    name = input()  # Get full name
    acronyms = ''.join(word[0]
                       for word in name.split(' ') if word[0].isupper())  # Convert to acronyms
    acronymsNames.append(acronyms)  # Append acronyms to acronyms list

# Sort acronyms list
acronymsNames.sort(key=lambda item: (-len(item), item))

# Print output
for acronyms in acronymsNames:
    print(acronyms)
