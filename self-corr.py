from openai import OpenAI
import traceback
import json

client = OpenAI()

error_details = None
success = False

while not success:
    try:
        # Adding error details to the prompt if there were errors in previous runs
        if error_details:
            system_message = f"Original code: {code}   \n\n Please generate clean Python code correcting the following error: {error_details}"
        else:
            system_message = "Generate clean Python code. Only the raw Python code is needed, with no formatting or comments. make a python mistake on purpose"

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": "Write me a python script that prints 'Hello, world!' without any comments or formatting."},
            ]
        )


        # Retrieve the code and clean it from Markdown or other formatting
        code = completion.choices[0].message.content.strip().replace("```python", "").replace("```", "").strip()

        print("code:::")
        print(code)

        # Execute the cleaned code
        exec(code)

        success = True  # Set success to True to break the loop if exec() works

        print("code:")
        print(code)

    except Exception as e:
        error_details = traceback.format_exc()
        print("We got an error. Trying again...")
        print(error_details)
