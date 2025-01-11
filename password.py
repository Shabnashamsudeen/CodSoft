import random
import string

def generate_password(length, complexity):
 
  characters = string.ascii_letters  

  if complexity == 'medium':
    characters += string.digits 

  if complexity == 'high':
    characters += string.punctuation 

  password = ''.join(random.choice(characters) for _ in range(length))
  return password

if __name__ == "__main__":
  length = int(input("Enter the desired password length: "))
  complexity = input("Enter complexity level (low, medium, high): ").lower()

  if complexity not in ('low', 'medium', 'high'):
    print("Invalid complexity level. Using 'low' as default.")
    complexity = 'low'

  password = generate_password(length, complexity)
  print("Generated Password:", password)
  