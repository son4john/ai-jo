import ollama
import os

model = "llama3.2"
input_file = "./data/grocery_list.txt"
output_file = "./data/categorized_grocery_list.txt"

if not os.path.exists(input_file):
    print(f"Input file {input_file} not found.")
    exit(1)

with open(input_file, "r") as f:
    items = f.read().strip()

prompt = f"""
You are an assistant that categorizes ans sorts grocery items.
Here is a list of grocery items: 
{items}

please:
1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, etc.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear manner, using bullet points or numbering.
"""

#Send the prompt and get the response
try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response","")
    # print(generated_text)

    #Write the categorized list to the output file
    with open(output_file, "w") as f:
        f.write(generated_text.strip())
    
    print(f"Categorized grocery list has been saved to {output_file}")
except Exception as e:
    print("An error occurred", str(e))