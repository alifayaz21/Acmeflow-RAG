import markdown
from bs4 import BeautifulSoup

def markdown_to_text(md_string: str) -> str:
    # 1. Convert Markdown to HTML
    html = markdown.markdown(md_string)
    
    # 2. Parse HTML with BeautifulSoup and extract plain text
    soup = BeautifulSoup(html, "html.parser")
    plain_text = soup.get_text()
    
    return plain_text

text="{\n  \"product_name\": \"Axionix Pulse Power Bank 04\",\n  \"product_id\": \"PRD-0004\",\n  \"colors_or_finishes\": [\n    \"Graphite\",\n    \"Blue\",\n    \"Black\"\n  ],\n  \"configurations\": [\n    \"10,000 mAh\",\n    \"20,000 mAh\",\n    \"30,000 mAh\"\n  ],\n  \"variants\": [\n    {\n      \"variant_id\": \"VAR-00010\",\n      \"sku\": \"EL04004-V01\",\n      \"color_or_finish\": \"Graphite\",\n      \"configuration\": \"10,000 mAh\"\n    },\n    {\n      \"variant_id\": \"VAR-00011\",\n      \"sku\": \"EL04004-V02\",\n      \"color_or_finish\": \"Blue\",\n      \"configuration\": \"20,000 mAh\"\n    },\n    {\n      \"variant_id\": \"VAR-00012\",\n      \"sku\": \"EL04004-V03\",\n      \"color_or_finish\": \"Black\",\n      \"configuration\": \"30,000 mAh\"\n    }\n  ]\n}"
print(markdown_to_text(text))