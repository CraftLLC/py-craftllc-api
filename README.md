# CraftAPI

CraftAPI is a simple-to-use Python library providing a set of tools for interacting with websites and retrieving various types of information, as well as utility functions for variable manipulation and time formatting.

## Installation

Install the package using pip:

```bash
pip install craftllc-api
```

## Usage

### `ReqTools` Class

This class provides methods for web scraping and making HTTP requests.

```python
from craftapi import ReqTools, UnknownMethod

req_tools = ReqTools()

# Get page title
title = req_tools.get_page_title("https://www.python.org/")
print(f"Page Title: {title}")

# Get all links on a page
links = req_tools.get_all_links("https://www.python.org/")
print("All Links:")
for link in links[:5]: # Print first 5 links
    print(link)

# Check HTTP status code
status_code = req_tools.check_http_status("https://www.python.org/")
print(f"HTTP Status Code: {status_code}")

# Extract all paragraphs
paragraphs = req_tools.extract_paragraphs("https://www.python.org/")
print("First Paragraph:")
if paragraphs:
    print(paragraphs[0])

# Get meta tags
meta_tags = req_tools.get_meta_tags("https://www.python.org/")
print("Meta Tags:")
for name, content in meta_tags.items():
    print(f"  {name}: {content}")

# Check SSL certificate (basic check)
ssl_status = req_tools.check_ssl_certificate("https://www.google.com/")
print(f"SSL Status: {ssl_status}")

# Save HTML content to a file
save_status = req_tools.save_html_to_file("https://www.python.org/", "python_org.html")
print(save_status)

# Extract list items
list_items = req_tools.extract_list_items("https://www.python.org/")
print("First List Item:")
if list_items:
    print(list_items[0])

# Get the first H1 tag
h1_tag = req_tools.get_first_h1("https://www.python.org/")
print(f"First H1 Tag: {h1_tag}")

# Get all script URLs
scripts = req_tools.get_all_scripts("https://www.python.org/")
print("First Script URL:")
if scripts:
    print(scripts[0])

# Extract form data
form_data = req_tools.extract_form_data("https://www.w3schools.com/html/html_forms.asp")
print("Form Data (first form):")
if form_data:
    print(form_data[0])

# Get CSS links
css_links = req_tools.get_css_links("https://www.python.org/")
print("First CSS Link:")
if css_links:
    print(css_links[0])

# Find all image URLs
image_urls = req_tools.find_all_images_url("https://www.python.org/")
print("First Image URL:")
if image_urls:
    print(image_urls[0])

# WHOIS lookup
whois_info = req_tools.whois("8.8.8.8")
print("WHOIS Info for 8.8.8.8:")
for key, value in whois_info.items():
    print(f"  {key}: {value}")

# Example of UnknownMethod exception
try:
    req_tools.find_all_images_url("https://example.com", method="INVALID")
except UnknownMethod as e:
    print(f"Caught expected exception: {e}")
```

### `Wordle` Class

This class provides methods related to New York Times games, specifically Wordle.

```python
from craftapi import Wordle

wordle_game = Wordle()

# Get today's Wordle answer
wordle_answer = wordle_game.answer
print(f"Today's Wordle Answer: {wordle_answer}")
```

### `VarTools` Class

This class provides utility methods for variable inspection and time formatting.

```python
from craftapi import VarTools

my_vars = {"name": "CraftAPI", "version": 0.1, "is_active": True}
var_tools = VarTools(my_vars)

# Get variable value
name_value = var_tools.get_var_value("name")
print(f"Value of 'name': {name_value}")

# Clean variable type
name_type = var_tools.clean_type("name")
version_type = var_tools.clean_type("version")
print(f"Type of 'name': {name_type}")
print(f"Type of 'version': {version_type}")

# Format time in seconds
formatted_time_seconds = var_tools.format_time(30)
formatted_time_minutes = var_tools.format_time(150)
formatted_time_hours = var_tools.format_time(7200)
formatted_time_days = var_tools.format_time(90000)
print(f"30 seconds: {formatted_time_seconds}")
print(f"150 seconds: {formatted_time_minutes}")
print(f"7200 seconds: {formatted_time_hours}")
print(f"90000 seconds: {formatted_time_days}")
```

## License

This project is licensed under the MIT License.