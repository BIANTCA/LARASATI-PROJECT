"""
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload = {
 'chat_id': chat_id,
 'text': message
}
response = requests.post(url, data=payload)
if response.status_code == 200:
  print("Message sent successfully.")
else:
  print(f"Failed to send message. Status code: {response.status_code}")
"""
