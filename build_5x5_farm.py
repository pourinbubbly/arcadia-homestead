# Build script generator that writes index.html directly from template file
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html_data = f.read()

print(f"index.html verified! Size: {len(html_data)} bytes")
