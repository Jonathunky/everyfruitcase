import os
import re


def extract_tables_from_content(content):
    """Extract markdown tables from content."""
    tables = re.findall(
        r"(\|.*?\|)\s*\n(\|[-:| ]+\|)(.*?)(?=\n\n|\Z)", content, re.DOTALL
    )
    return [table[0] + "\n" + table[1] + table[2] for table in tables]


def process_table(table):
    """Convert a single markdown table into the desired format."""
    lines = table.strip().split("\n")
    headers = [h.strip() for h in lines[1].split("|")[1:-1]]
    items = ['"' + h.split(" ")[1] + '"' for h in headers]

    tab_templates = []
    for idx, header in enumerate(headers, start=1):
        tab_content = [
            "| Color        | {} | Image                           |".format(header),
            "| ------------ | --- | ------------------------------- |",
        ]
        for line in lines[2:]:
            parts = [p.strip() for p in line.split("|")[1:-1]]
            color = parts[0]
            sku = parts[idx]
            image = sku[:-4]  # Removing the "ZM/A" to get the image name
            tab_content.append(
                "| {} | {} | ![Image](/everyphone/{}.png) |".format(color, sku, image)
            )

        tab_template = "<Tabs.Tab>\n{}\n</Tabs.Tab>".format("\n".join(tab_content))
        tab_templates.append(tab_template)

    result = "<Tabs\n  items={[{}]}\n>\n{}\n</Tabs>".format(
        ", ".join(items), "\n".join(tab_templates)
    )
    return result


def convert_md_to_mdx(file_path):
    """Convert markdown tables in a file to the desired format."""
    with open(file_path, "r") as file:
        content = file.read()

    tables = extract_tables_from_content(content)

    for table in tables:
        new_format = process_table(table)
        content = content.replace(table, new_format)

    new_file_path = file_path.replace(".md", ".mdx")
    with open(new_file_path, "w") as file:
        file.write(content)


if __name__ == "__main__":
    folder_name = input("Enter folder name: ")
    for filename in os.listdir(folder_name):
        if filename.endswith(".md"):
            convert_md_to_mdx(os.path.join(folder_name, filename))
