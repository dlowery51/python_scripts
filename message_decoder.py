import requests
import re

"""
This program simply acquires a code provided from a webpage and assembles that code into
a two-dimensional graph that reveals a hidden message.
"""

def fetch_unicode_grid_no_lib(url):
    response = requests.get(url)
    html = response.text

    # Extract the table content between <table> and </table>
    table_match = re.search(r'<table.*?>(.*?)</table>', html, re.DOTALL | re.IGNORECASE)
    if not table_match:
        print("No table found in HTML.")
        return []

    table_html = table_match.group(1)

    # Extract rows between <tr> and </tr>
    rows = re.findall(r'<tr.*?>(.*?)</tr>', table_html, re.DOTALL | re.IGNORECASE)

    grid_data = []
    for row in rows:
        # Extract columns between <td> and </td>
        cols = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL | re.IGNORECASE)
        if len(cols) == 3:
            # Clean up HTML entities and whitespace inside each column
            x_str = re.sub(r'<.*?>', '', cols[0]).strip()
            char = re.sub(r'<.*?>', '', cols[1]).strip()
            y_str = re.sub(r'<.*?>', '', cols[2]).strip()

            try:
                x = int(x_str)
                y = int(y_str)
                grid_data.append({'x': x, 'char': char, 'y': y})
            except ValueError:
                # Skip rows with non-integer coordinates
                continue

    return grid_data

# Usage:
url = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
grid = fetch_unicode_grid_no_lib(url)
print(grid[:5])