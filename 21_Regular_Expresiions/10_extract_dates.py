import re

text = "The events are on 12-05-2026 and 25-12-2026."

pattern = r"\b\d{2}-\d{2}-\d{4}\b"

dates = re.findall(pattern, text)

print("Dates found:", dates)
