from pathlib import Path
from bs4 import BeautifulSoup


folder_path = Path('./inputs') 

for file in folder_path.iterdir():
    if file.is_file():
        current_file = file.name  # Store the file name in a variable
        print(current_file)      
        input_html_file = f"./inputs/{current_file}"
        with open(input_html_file, "r", encoding="utf-8") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, "html.parser")
        text_content = soup.get_text(separator=" ", strip=True)
        text_content=text_content.split("Keywords:")[1]
        with open(f"{current_file[:-5]}.txt", "w") as file:
            file.write(text_content)
    




