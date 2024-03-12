alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction): # caesar cipher function
     end_text = "" # empty variable, to receive letters in the next steps
     if cipher_direction == "decode": 
        shift_amount *= -1 # here, i use the number of shift i want to decipher, and multiplying by -1, it will go backwards
     for char in start_text: # creating a for to iterate in each letter of my input
        if char in alphabet: # have sure that the input is a letter, and not a number or symbol
            position = alphabet.index(char) # with the index function, i get the number of the index of each character in the alphabet list
            new_position = position + shift_amount #calculate the new position, after adding the shift number to the cypher
            end_text += alphabet[new_position] # adds the letters after the new index to my empy variable
        else:
            end_text += char # if theres symbols or numbers, i ignore them and just add the letters in alphabet.
     print(f"The {cipher_direction}d text is {end_text}") # print the result

should_continue = True
while should_continue: # for my app continues asking for cypher, create a while loop.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    result = input("Type yes if you want to go again. Otherwise type no.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")