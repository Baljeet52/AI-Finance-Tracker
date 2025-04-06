

import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"
openai.api_type = "open_ai"
openai.api_version = None

def categorize_transaction(description):
    print("Entered into function")
    try:
        examples = (
            "Transaction: McDonald's meal\nCategory: Food\n"
            "Transaction: Uber ride to work\nCategory: Transport\n"
            "Transaction: Amazon order for shoes\nCategory: Shopping\n"
            "Transaction: Electricity bill payment\nCategory: Bills\n"
            "Transaction: Movie night tickets\nCategory: Entertainment\n"
        )

        prompt = (
            f"Categorize the following financial transaction description into one of the following categories: "
            f"['Food', 'Transport', 'Shopping', 'Bills', 'Entertainment', 'Other'].\n\n"
            f"{examples}"
            f"Transaction: {description}\nCategory:"
        )

        response = openai.ChatCompletion.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that classifies financial transactions."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=10
        )

        category = response.choices[0].message['content'].strip()
        print(f"Category: {category}")
        return category

    except openai.error.OpenAIError as e:
        print("OpenAI API Error:", e)
        return "Other"
    except Exception as e:
        print("General Error:", e)
        return "Other"
