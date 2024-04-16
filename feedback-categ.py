from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "you are an expert system that categorizes customer feedback in a bank.\n\ncategories:\n- negative\n- positive\n\nGive me the answer as json format."},
    {"role": "user", "content": "I've been a customer with this bank for over 10 years and their customer service has always been outstanding. Whenever I've had issues, they were resolved quickly and efficiently"}
  ]
)

print(completion.choices[0].message)

