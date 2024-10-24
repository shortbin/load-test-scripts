import pandas as pd
import jwt
import datetime


secret_key = 'sahdfbadfhblsbfasilb'

def generate_jwt_token(email, user_id, type):
  """Generates a JWT token with email, user ID, type as payload."""
  payload = {
      'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
      "payload" :{
          'email': email,
          'id': user_id,
          "type": "x-" + type
      },
  }
  token = jwt.encode(payload, secret_key, algorithm='HS256')
  return token


def main():
  """Reads email and ID from a CSV, generates JWT tokens, and creates a new CSV."""
  df = pd.read_csv('fake_users.csv')
  new_data = []

  for idx, row in df.iterrows():
    email = row['email']
    user_id = row['id']

    access_token = generate_jwt_token(email, user_id, "access")
    refresh_token = generate_jwt_token(email, user_id, "refresh")
    reset_token = generate_jwt_token(email, user_id, "reset")

    new_data.append([email, access_token, refresh_token, reset_token])

  new_df = pd.DataFrame(new_data, columns=['email', 'access_token', 'refresh_token', 'reset_token'])

  new_df.to_csv('users_creds.csv', index=False)

  print("users_creds.csv created")


if __name__ == "__main__":
  main()
