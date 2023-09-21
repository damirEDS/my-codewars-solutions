import pandas as pd
import io
import os

# Load data from Excel
df = pd.read_excel('solutions.xlsx')

# Iterate over rows in Excel
for index, row in df.iterrows():
    title = row['Task Title']  # Task Title column in English
    description = row['Description']  # Description column in English
    solution_code = row['Solution Code']  # Solution Code column in English
    difficulty = row['Difficulty']  # Difficulty column in English
    explanation = row['Explanation']  # Added Explanation field
    examples = row['Examples']  # Added Examples field
    algorithm_complexity = row['Algorithm Complexity']  # Added Algorithm Complexity field

    # Extract kyu level
    level = difficulty.split()[0].lower()

    # Convert task title to a proper file format
    file_name = f'{title.lower().replace(" ", "_")}.md'

    # Generate Markdown content
    markdown_content = f"""# {title}

## Description

{description}

## Solution

```python
{solution_code}
```
##Difficulty
{difficulty}

##Explanation
{explanation} 

##Examples
```python
{examples} 
```
##Algorithm Complexity
{algorithm_complexity} 
"""

    # Define the directory based on the kyu level
    directory = f'kyu_{level}'

    # Check if the directory exists, and create it if it doesn't
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save to file
    with io.open(f'{directory}/{file_name}', 'w', encoding='utf-8') as file:
        file.write(markdown_content)
