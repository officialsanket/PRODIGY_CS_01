  def caesar_cipher(text, shift, mode='encrypt'):
  result = ""
  shift = shift if mode == 'encrypt' else -shift
  for char in text:
      if char.isalpha():
          base = 65 if char.isupper() else 97
          result += chr((ord(char) - base + shift) % 26 + base)
      else:
          result += char
  return result

def main():
  choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (E/D): ").strip().upper()
  message = input("Enter your message: ")
  shift = int(input("Enter the shift value: "))

  if choice == 'E':
      print("Encrypted Message:", caesar_cipher(message, shift, 'encrypt'))
  elif choice == 'D':
      print("Decrypted Message:", caesar_cipher(message, shift, 'decrypt'))
  else:
      print("Invalid choice. Please enter 'E' or 'D'.")

if __name__ == "__main__":
  main()
