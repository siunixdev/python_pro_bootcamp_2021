import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

try_again = True

while try_again == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def caesar(text = text, shift = shift, direction = direction):
    end_text = ""
    for letter in text:
      if letter in alphabet :
        letter_position = alphabet.index(letter)

        if direction == "encode" :
          cipher_position = letter_position + shift

          temp_cipher_position = cipher_position
          num_of_rotation = 0
          while temp_cipher_position > 25 :
            num_of_rotation += 1
            temp_cipher_position = (temp_cipher_position - 25)

          if cipher_position > 25 :
            cipher_position = temp_cipher_position - num_of_rotation

        else :
          cipher_position = letter_position - shift

          temp_cipher_position = cipher_position
          while temp_cipher_position < -26 :
            temp_cipher_position = (temp_cipher_position + 26)

          if cipher_position < -26 :
            cipher_position = temp_cipher_position


        cipher_letter = alphabet[cipher_position]

        end_text += cipher_letter
      else:
        end_text += letter

    print(f"The {direction}d text is {end_text}")

  caesar(text=text, shift=shift, direction=direction)

  try_again_question = input("Do you want to restart the cipher program? \nType 'yes' if you want to go again. Otherwise type 'no' : ").lower()
  if try_again_question == 'no':
    try_again = False