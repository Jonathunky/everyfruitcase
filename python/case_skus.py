def sort_table_columns(table):
    # Find the indices of the columns based on alphabetical order in the first non-header row
    first_row = table[1][1:]  # Skip the first column ('Model / Color')
    alpha_indices = sorted(range(len(first_row)), key=lambda i: first_row[i])

    # Rearrange the table columns based on the sorted indices
    sorted_table = []
    for row in table:
        sorted_row = [row[0]] + [row[i + 1] if i + 1 < len(row) else "" for i in alpha_indices]
        sorted_table.append(sorted_row)

    return sorted_table


def create_table_from_dict(data_dict):
    # Create the header row for the table
    header_row = [1, "      "]
    colors = list(set(color for _, color in data_dict.values()))
    header_row.extend(colors)
    table_data = [header_row]

    # Create a list of unique models
    models = list(set(model for model, _ in data_dict.values()))

    # Create rows for each model
    for idx, model in enumerate(models, start=2):
        row_data = [idx, model]
        for color in colors:
            for key, value in data_dict.items():
                if value == [model, color]:
                    row_data.append(key)
        table_data.append(row_data)

    table_data = [row[1:] for row in table_data]
    # Print the table
    print("table = [")
    for row in table_data:
        print(row, end="")
        print(',')
    print("]")

    return table_data


def generate_markdown_file(tables, title, filename):
    markdown_content = "import Image from \"next/image\"\n\n"

    markdown_content += f"# {title}\n\n"

    markdown_content += "## In the Wild\n\n"
    markdown_content += "## Pricing / Availability\n\n"
    markdown_content += "## Compatibility\n\n"
    markdown_content += "## Part numbers\n\n"

    for table in tables:
        table_data = sort_table_columns(table)

        # Generate the Markdown table
        table_content = "|" + "|".join(table_data[0]) + "|\n"
        table_content += "|" + "|".join(":--" for _ in table_data[0]) + "|\n"
        for row in table_data[1:]:
            table_content += "|" + "|".join(row) + "|\n"

        markdown_content += table_content
        markdown_content += "\n\n"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(markdown_content)


early_2011 = {
    "MC360ZM/A": "iPad Dock",
    "MC531ZM/A": "iPad Camera Connection Kit",
    "MC533LL/B": "iPad Keyboard Dock",
    "MC552ZM/B": "iPad Dock connector to VGA adapter",
    "MC940ZM/A": "iPad 2 Dock",
}

# table2 = [create_table_from_dict(ipad129), create_table_from_dict(ipadleather)]
# generate_markdown_file(table2, "iPad Pro 12.9", "ipadpro.mdx")
# table3 = [create_table_from_dict(summeriphone), create_table_from_dict(summersili)]


sleeve = {
    "MQG02ZM/A": ["Leather Sleeve for 12-inch MacBook", "Midnight Blue"],
    "MQG12ZM/A": ["Leather Sleeve for 12-inch MacBook", "Saddle Brown"],

}
spring_folio = {

    "MRGE2ZM/A": ["iPhone X Leather Folio", "Electric Blue"],
    "MRGF2ZM/A": ["iPhone X Leather Folio", "Soft Pink"],
    "MRQD2ZM/A": ["iPhone X Leather Folio", "(PRODUCT)RED"],

    # no iPad Pro 12.9 covers back because...
}

leather_pad = {

    "MRFL2ZM/A": ["iPad Pro 10.5″ Leather Sleeve ", "Electric Blue"],
    "MRFM2ZM/A": ["iPad Pro 10.5″ Leather Sleeve ", "Soft Pink"],
    "MRFJ2ZM/A": ["iPad Pro 10.5″ Leather Smart Cover", "Electric Blue"],
    "MRFK2ZM/A": ["iPad Pro 10.5″ Leather Smart Cover", "Soft Pink"],
}

sili_pad = {

    "MRFG2ZM/A": ["Smart Cover for 10.5‐inch iPad Pro", "Lemonade"],
    "MRFF2ZM/A": ["Smart Cover for 10.5‐inch iPad Pro", "Raspberry"]
}

generate_markdown_file([create_table_from_dict(spring_folio)], "iPhone Folio",
                       "iphone.mdx")
generate_markdown_file(
    [create_table_from_dict(sleeve), create_table_from_dict(leather_pad), create_table_from_dict(sili_pad)],
    "iPad 10.5 Spring",
    "ipad.mdx")

late_2018 = {
    #
    # + XR Clear Case
}

#
