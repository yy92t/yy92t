import secrets
import string

def generate_password(length=8):
     alphabet = string.ascii_letters + string.digits + string.punctuation
     password = ''.join(secrets.choice(alphabet) for i in range(length))
     return password
 
if __name__ == "__main__":
     password = generate_password(8)
     print(f"Generated Password: {password}")
