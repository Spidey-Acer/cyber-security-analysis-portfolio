"""
Convert US17502-TASK3-CONTENT.md to HTML for PDF conversion
This creates a professionally formatted HTML that can be easily converted to PDF
"""

import re
import os

# Read the markdown file
with open('US17502-TASK3-CONTENT.md', 'r', encoding='utf-8') as f:
    content = f.read()

# HTML template with professional academic styling
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Activity 3: SIEM-Based Attack Simulation and Detection - US17502</title>
    <style>
        @page {
            size: A4;
            margin: 2.54cm;
        }
        
        body {
            font-family: 'Times New Roman', Times, serif;
            font-size: 12pt;
            line-height: 1.5;
            color: #000;
            max-width: 21cm;
            margin: 0 auto;
            padding: 20px;
            background: white;
        }
        
        h1 {
            font-size: 16pt;
            font-weight: bold;
            margin-top: 24pt;
            margin-bottom: 12pt;
            color: #000;
            page-break-after: avoid;
        }
        
        h2 {
            font-size: 14pt;
            font-weight: bold;
            margin-top: 18pt;
            margin-bottom: 10pt;
            color: #000;
            page-break-after: avoid;
        }
        
        h3 {
            font-size: 12pt;
            font-weight: bold;
            margin-top: 12pt;
            margin-bottom: 8pt;
            color: #000;
            page-break-after: avoid;
        }
        
        p {
            margin: 0 0 12pt 0;
            text-align: justify;
        }
        
        ul, ol {
            margin: 0 0 12pt 0;
            padding-left: 40pt;
        }
        
        li {
            margin-bottom: 6pt;
        }
        
        code {
            font-family: 'Courier New', Courier, monospace;
            font-size: 10pt;
            background-color: #f5f5f5;
            padding: 2px 4px;
            border-radius: 3px;
        }
        
        pre {
            font-family: 'Courier New', Courier, monospace;
            font-size: 10pt;
            background-color: #f5f5f5;
            padding: 12pt;
            border-left: 3pt solid #ccc;
            margin: 12pt 0;
            overflow-x: auto;
            page-break-inside: avoid;
        }
        
        pre code {
            background: none;
            padding: 0;
        }
        
        .figure-caption {
            font-weight: bold;
            color: #333;
            font-style: italic;
            margin: 12pt 0;
            padding: 8pt;
            background-color: #f9f9f9;
            border-left: 3pt solid #666;
            page-break-inside: avoid;
        }
        
        .header-info {
            text-align: left;
            margin-bottom: 24pt;
            font-size: 11pt;
        }
        
        hr {
            border: none;
            border-top: 1px solid #ccc;
            margin: 18pt 0;
        }
        
        strong {
            font-weight: bold;
        }
        
        em {
            font-style: italic;
        }
        
        blockquote {
            margin: 12pt 0 12pt 40pt;
            padding-left: 12pt;
            border-left: 3pt solid #ccc;
            font-style: italic;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 12pt 0;
            page-break-inside: avoid;
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 8pt;
            text-align: left;
        }
        
        th {
            background-color: #f5f5f5;
            font-weight: bold;
        }
        
        .page-break {
            page-break-before: always;
        }
        
        @media print {
            body {
                margin: 0;
                padding: 0;
            }
            
            .no-print {
                display: none;
            }
        }
    </style>
</head>
<body>
{CONTENT}
</body>
</html>
"""

def convert_markdown_to_html(md_content):
    """
    Convert markdown to HTML with basic formatting
    """
    html = md_content
    
    # Convert headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    
    # Convert horizontal rules
    html = re.sub(r'^---+$', r'<hr>', html, flags=re.MULTILINE)
    
    # Convert bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # Convert italic
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Convert figure captions (special formatting)
    html = re.sub(r'\*\*\[Figure (\d+): ([^\]]+)\]\*\*', 
                  r'<div class="figure-caption"><strong>Figure \1:</strong> \2</div>', html)
    
    # Convert code blocks
    html = re.sub(r'```(\w+)?\n(.*?)```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Convert lists (simplified)
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', html, flags=re.DOTALL)
    html = html.replace('</ul>\n<ul>', '\n')  # Merge consecutive lists
    
    # Convert numbered lists
    html = re.sub(r'^\d+\. (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    
    # Convert paragraphs (lines that don't start with HTML tags)
    lines = html.split('\n')
    new_lines = []
    in_tag = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            new_lines.append(line)
        elif stripped.startswith('<') or in_tag:
            new_lines.append(line)
            if '<pre>' in line:
                in_tag = True
            if '</pre>' in line:
                in_tag = False
        else:
            new_lines.append(f'<p>{line}</p>')
    
    html = '\n'.join(new_lines)
    
    return html

# Convert content
html_content = convert_markdown_to_html(content)

# Insert into template
final_html = html_template.replace('{CONTENT}', html_content)

# Write HTML file
output_file = 'US17502-TASK3-TEMP.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"✓ HTML file created: {output_file}")
print("\n" + "="*70)
print("NEXT STEPS TO CREATE PDF:")
print("="*70)
print("\nOption 1 - Using Microsoft Word (RECOMMENDED):")
print("  1. Open US17502-TASK3-TEMP.html in Microsoft Word")
print("  2. File → Save As")
print("  3. File name: US17502-TASK3.pdf")
print("  4. Save as type: PDF")
print("  5. Click Save")
print("\nOption 2 - Using Chrome/Edge Browser:")
print("  1. Open US17502-TASK3-TEMP.html in Chrome or Edge")
print("  2. Press Ctrl+P (Print)")
print("  3. Destination: Save as PDF")
print("  4. File name: US17502-TASK3.pdf")
print("  5. Click Save")
print("\nOption 3 - Using Online Converter:")
print("  1. Visit: https://www.html2pdf.com/")
print("  2. Upload US17502-TASK3-TEMP.html")
print("  3. Download as US17502-TASK3.pdf")
print("\n" + "="*70)
print("\nAfter creating PDF:")
print("  - Delete US17502-TASK3-TEMP.html")
print("  - Add screenshots to PDF if needed")
print("  - Verify US17502-TASK3.pdf looks correct")
print("="*70)
