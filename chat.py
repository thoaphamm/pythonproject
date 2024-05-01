import requests

url = "https://api.openai.com/v1/completions"
api_key = ""

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

prompt = "CÂU HỎI Ở ĐÂY"
data = {
    "model": "gpt-3.5-turbo",
    "prompt": prompt,
    "max_tokens": 50
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    completion = response.json()["choices"][0]["text"]
    print(completion)
    #CÂU TRẢ LỜI
else:
    print("Error:", response.status_code)