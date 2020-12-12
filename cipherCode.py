from art import logo
from replit import clear
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_run = True
while should_run:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 25
  def cipher(start_text,shift_number,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
      shift_number *= -1
    for char in start_text:
      if char in alphabet:
        possition = alphabet.index(char)
        new_possition = possition + shift_number
        new_text = alphabet[new_possition]
        end_text += new_text
   
      else:
        end_text += char
    print(f"Your {cipher_direction}d message is ' {end_text} '")
    result = input("Do you want to run the program again 'Yes' or 'No'\n").lower()
    if result == "yes":
      should_run = True
      clear()
    else:
      should_run = False
      print("GoodBye")

  cipher(start_text = text, shift_number=shift,cipher_direction=direction)
