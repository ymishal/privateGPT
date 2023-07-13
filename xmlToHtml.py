import xml.etree.ElementTree as ET


def parse_xml(xml_root):
    html_content = ""

    for element in xml_root:
        tag = element.tag
        text = element.text
        html_content += f"<{tag}>{text}</{tag}>\n"

        # Recursive call for child elements
        html_content += parse_xml(element)

    return html_content


def main():
    # Define file paths
    input_file = "source_documents\\simplewiki-latest-pages-articles-multistream.xml"
    output_file = "source_documents\\simplewiki-latest-pages-articles-multistream.html"

    # Parse the XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Convert XML to HTML
    html_content = parse_xml(root)

    # Wrap content in HTML tags
    html_content = f"<html>\n<head>\n<title>Converted XML</title>\n</head>\n<body>\n{html_content}</body>\n</html>"

    # print first 4 words
    print(f"{html_content.split()[:4]}done!")
    # Write the HTML content to a file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)


if __name__ == "__main__":
    main()
