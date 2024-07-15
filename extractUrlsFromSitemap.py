import requests
import re

# Regular expression to match content between <loc> and </loc>
pattern = re.compile(r'<loc>(.*?)</loc>')

# Fetch the sitemap XML
sitemap_url = "https://www.techuz.com/sitemap.xml"
response = requests.get(sitemap_url)

# Find all matches
matches = pattern.findall(response.text)

# Print the result
print(matches)
