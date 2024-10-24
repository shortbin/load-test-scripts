import pandas as pd
import random
import string

def generate_random_email():
  """Generates a random email address."""
  letters = string.ascii_lowercase
  return ''.join(random.choice(letters) for i in range(8)) + '@g.g'

def generate_random_data(num_rows):
  data = []
  for _ in range(num_rows):
    email = generate_random_email()
    user_id = str(random.randint(100, 10000))
    data.append([email, user_id])
  return data

if __name__ == "__main__":
  num_rows = 1000 # Number of rows to generate
  data = generate_random_data(num_rows)
  df = pd.DataFrame(data, columns=['email', 'id'])
  df.to_csv('fake_users.csv', index=False)
  print("fake_users.csv created")
