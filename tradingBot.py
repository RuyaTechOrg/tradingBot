import requests

token = 'pk_8b394305e37c44c29b547b0b71a9e9f6'

api_url = f'https://api.iex.cloud/v1/data/core/quote/tsla?token={token}'

data = requests.get(api_url).json() 

print(data)