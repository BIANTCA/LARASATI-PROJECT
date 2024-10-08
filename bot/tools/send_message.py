{
    "code": "url = f\"https://api.telegram.org/bot{bot_token}/sendMessage\"\n"
            "payload = {'chat_id': chat_id, 'text': message}\n"
            "response = requests.post(url, data=payload)\n"
            "if response.status_code == 200:\n"
            "    print(\"Message sent successfully.\")\n"
            "else:\n"
            "    print(f\"Failed to send message. Status code: {response.status_code}\")"
}
