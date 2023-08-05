def sort_table_columns_by_numbers(table):
    # Find the indices of the columns based on the numeric values in the first non-header row
    first_row = table[1][1:]  # Skip the first column ('Model / Color')
    numeric_indices = sorted(range(len(first_row)), key=lambda i: int(''.join(filter(str.isdigit, first_row[i]))))

    # Rearrange the table columns based on the numeric indices
    sorted_table = []
    for row in table:
        sorted_row = [row[0]] + [row[i + 1] for i in numeric_indices]
        sorted_table.append(sorted_row)

    return sorted_table


def create_table_from_dict(data_dict):
    # Create the header row for the table
    header_row = [1, "Model / Color"]
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

    return


def generate_markdown_file(tables, title, filename):
    markdown_content = f"# {title}\n\n"

    markdown_content += "## In the Wild\n\n"
    markdown_content += "## Pricing / Availability\n\n"
    markdown_content += "## Compatibility\n\n"
    markdown_content += "## Part numbers\n\n"

    for table in tables:
        table_data = sort_table_columns_by_numbers(table)

        # Generate the Markdown table
        table_content = "|" + "|".join(table_data[0]) + "|\n"
        table_content += "|" + "|".join(":--" for _ in table_data[0]) + "|\n"
        for row in table_data[1:]:
            table_content += "|" + "|".join(row) + "|\n"

        markdown_content += table_content
        markdown_content += "\n\n"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(markdown_content)


year_2004 = {
    "M9720G/B": "iPod Socks 6 pack"
}

year_2010 = {
    "MC361ZM/B": ["iPad Case", "Black"],  # april?
    "MC668ZM/B": ["iPhone 4 Bumper", "White"],  # june?
    "MC669ZM/B": ["iPhone 4 Bumper", "Pink"],
    "MC670ZM/B": ["iPhone 4 Bumper", "Blue"],
    "MC671ZM/B": ["iPhone 4 Bumper", "Green"],
    "MC672ZM/B": ["iPhone 4 Bumper", "Orange"],
    "MC839ZM/B": ["iPhone 4 Bumper", "Black"]
}

Spring_2011 = {
    "MC939LL/A": ["iPad Smart Cover", "Gray"],
    "MC941LL/A": ["iPad Smart Cover", "Pink"],
    "MC942LL/A": ["iPad Smart Cover", "Blue"],
    "MC944LL/A": ["iPad Smart Cover", "Green"],
    "MC945LL/A": ["iPad Smart Cover", "Orange"],

    "MC947LL/A": ["iPad Leather Smart Cover", "Black"],
    "MC948LL/A": ["iPad Leather Smart Cover", "Tan"],
    "MC949LL/A": ["iPad Leather Smart Cover", "Navy"],
    "MC952LL/A": ["iPad Leather Smart Cover", "Cream"]
}

Autumn_2011 = {
    # now colored on the inside! all of them! neat!
    "MD306LL/A": ["iPad Smart Cover", "Dark Gray"],
    "MD307LL/A": ["iPad Smart Cover", "Light Gray"],
    "MD308LL/A": ["iPad Smart Cover", "Pink"],
    "MD309LL/A": ["iPad Smart Cover", "Green"],
    "MD310LL/A": ["iPad Smart Cover", "Blue"],
    # no orange though...

    "MD301LL/A": ["iPad Leather Smart Cover", "Black"],
    "MD302LL/A": ["iPad Leather Smart Cover", "Tan"],
    "MD303LL/A": ["iPad Leather Smart Cover", "Navy"],
    "MD304LL/A": ["iPad Leather Smart Cover", "Red"],  # new color!
    "MD305LL/A": ["iPad Leather Smart Cover", "Cream"]
}

Spring_2012 = {
    "MD454LL/A": ["iPad Smart Case", "Dark Gray"],
    "MD455LL/A": ["iPad Smart Case", "Light Gray"],
    "MD456LL/A": ["iPad Smart Case", "Pink"],
    "MD457LL/A": ["iPad Smart Case", "Green"],  # as seen on DankPods!
    "MD458LL/A": ["iPad Smart Case", "Blue"],
    "MD579LL/A": ["iPad Smart Case", "Red"]
}

Autumn_2012 = {
    "MD963LL/A": ["iPad Mini Smart Cover", "Dark Gray"],
    "MD967LL/A": ["iPad Mini Smart Cover", "Light Gray"],
    "MD968LL/A": ["iPad Mini Smart Cover", "Pink"],
    "MD969LL/A": ["iPad Mini Smart Cover", "Green"],
    "MD970LL/A": ["iPad Mini Smart Cover", "Blue"],
    "MD828LL/A": ["iPad Mini Smart Cover", "Red"],

    "MD829LL/A": ["iPod Touch Loop", "Red"],
    "MD971LL/A": ["iPod Touch Loop", "Black"],
    "MD972LL/A": ["iPod Touch Loop", "Pink"],
    "MD973LL/A": ["iPod Touch Loop", "Yellow"],
    "MD974LL/A": ["iPod Touch Loop", "Blue"]
}

ipad2013_cover = [
    ['Model / Color', 'Blue', 'Green', 'Pink', 'Red', 'Yellow', 'Black'],
    ['iPad Air Smart Cover', 'MF054LL/A', 'MF056LL/A', 'MF055LL/A', 'MF058LL/A', 'MF057LL/A', 'MF053LL/A'],
    ['iPad Mini Smart Cover', 'MF060LL/A', 'MF062LL/A', 'MF061LL/A', 'MF394LL/A', 'MF063LL/A', 'MF059LL/A'],
]

ipad2013_case = [
    ['Model / Color', 'Brown', 'Blue', 'Red', 'Beige', 'Yellow', 'Black'],
    ['iPad Air Smart Case', 'MF047LL/A', 'MF050LL/A', 'MF052LL/A', 'MF048LL/A', 'MF049LL/A', 'MF051LL/A'],
    ['iPad Mini Smart Case', 'ME706LL/A', 'ME709LL/A', 'ME711LL/A', 'ME707LL/A', 'ME708LL/A', 'ME710LL/A'],
]

iphone5c = [
    ['Model / Color', 'White', 'Black', 'Yellow', 'Pink', 'Green', 'Blue'],
    ['iPhone 5c Case', 'MF039ZM/A', 'MF040ZM/A', 'MF038ZM/A', 'MF036ZM/A', 'MF037ZM/A', 'MF035ZM/A'],
]

iphone5s = [
    ['Model / Color', 'Red', 'Black', 'Yellow', 'Beige', 'Blue', 'Brown'],
    ['iPhone 5s Case', 'MF046LL/A', 'MF045LL/A', 'MF043LL/A', 'MF042LL/A', 'MF044LL/A', 'MF041LL/A']
]

tables = [ipad2013_case, ipad2013_cover]
generate_markdown_file(tables, "iPad Air & mini 2", "ipad.md")
generate_markdown_file([iphone5s], "iPhone 5s Leather Case", "5s.md")
generate_markdown_file([iphone5c], "iPhone 5c Silicone Case", "5c.md")

year_2014 = {
    "MF631ZM/A": ["iPod Touch Loop", "Space Gray"]
}

iphone6_silicone = [
    ['Model / Color', 'Black', 'Green', 'White', '(PRODUCT)RED', 'Blue', 'Pink'],
    ['iPhone 6 Silicone Case', 'MGQF2ZM/A', 'MGXU2ZM/A', 'MGQG2ZM/A', 'MGQH2ZM/A', 'MGQJ2ZM/A', 'MGXT2ZM/A'],
    ['iPhone 6 Plus Silicone Case', 'MGR92ZM/A', 'MGXX2ZM/A', 'MGRF2ZM/A', 'MGRG2ZM/A', 'MGRH2ZM/A', 'MGXW2ZM/A'],

]
iphone6_leather = [
    ['Model / Color', 'Black', 'Olive Brown', 'Soft Pink', '(PRODUCT)RED', 'Midnight Blue'],
    ['iPhone 6 Leather Case', 'MGR62ZM/A', 'MGR22ZM/A', 'MGR52ZM/A', 'MGR82ZM/A', 'MGR32ZM/A'],
    ['iPhone 6 Plus Leather Case', 'MGQX2ZM/A', 'MGQR2ZM/A', 'MGQW2ZM/A', 'MGQY2ZM/A', 'MGQV2ZM/A'],

]
ipad2014_case = [
    ['Model / Color', 'Black', 'Olive Brown', 'Soft Pink', '(PRODUCT)RED', 'Midnight Blue'],
    ['iPad Air 2 Smart Case', 'MGTV2ZM/A', 'MGTR2ZM/A', 'MGTU2ZM/A', 'MGTW2ZM/A', 'MGTT2ZM/A'],
    ['iPad mini Smart Case', 'MGN62ZM/A', 'MGMN2ZM/A', 'MGN32ZM/A', 'MGND2ZM/A', 'MGMW2ZM/A'],
]
ipad2014_cover = [
    ['Model / Color', 'Black', 'Green', 'Yellow', 'White', '(PRODUCT)RED', 'Blue', 'Pink'],
    ['iPad Air Smart Cover', 'MGTM2ZM/A', 'MGXL2ZM/A', 'MGXN2ZM/A', 'MGTN2ZM/A', 'MGTP2ZM/A', 'MGTQ2ZM/A', 'MGXK2ZM/A'],
    ['iPad mini Smart Cover', 'MGNC2ZM/A', 'MGNQ2ZM/A', 'MGNT2ZM/A', 'MGNK2ZM/A', 'MGNL2ZM/A', 'MGNM2ZM/A',
     'MGNN2ZM/A'],
]

Autumn_2015 = {
    "MKXX2ZM/A": ["iPhone 6s Leather Case", "(PRODUCT)RED"],
    # both released a bit later in 2015
    "MKXG2ZM/A": ["iPhone 6s Plus Leather Case", "(PRODUCT)RED"],

    "MGQM2LL/A": ["iPhone 6s Smart Battery Case", "White"],
    # first ever
    "MGQL2LL/A": ["iPhone 6s Smart Battery Case", "Charcoal Gray"],

    "MKXW2ZM/A": ["iPhone 6s Leather Case", "Black"],
    "MKXR2ZM/A": ["iPhone 6s Leather Case", "Brown"],
    "MKXU2ZM/A": ["iPhone 6s Leather Case", "Midnight Blue"],
    "MKXV2ZM/A": ["iPhone 6s Leather Case", "Rose Gray"],
    "MKXT2ZM/A": ["iPhone 6s Leather Case", "Saddle Brown"],

    "MKXF2ZM/A": ["iPhone 6s Plus Leather Case", "Black"],
    "MKX92ZM/A": ["iPhone 6s Plus Leather Case", "Brown"],
    "MKXD2ZM/A": ["iPhone 6s Plus Leather Case", "Midnight Blue"],
    "MKXE2ZM/A": ["iPhone 6s Plus Leather Case", "Rose Gray"],
    "MKXC2ZM/A": ["iPhone 6s Plus Leather Case", "Saddle Brown"],

    "MLCX2ZM/A": ["iPhone 6s Silicone Case", "Antique White"],
    "MKY52ZM/A": ["iPhone 6s Silicone Case", "Blue"],
    "MKY02ZM/A": ["iPhone 6s Silicone Case", "Charcoal Gray"],
    "MLCV2ZM/A": ["iPhone 6s Silicone Case", "Lavender"],
    "MKY22ZM/A": ["iPhone 6s Silicone Case", "Midnight Blue"],
    "MKY62ZM/A": ["iPhone 6s Silicone Case", "Orange"],
    "MLCU2ZM/A": ["iPhone 6s Silicone Case", "Pink"],
    "MKY32ZM/A": ["iPhone 6s Silicone Case", "(PRODUCT)RED"],
    "MKY42ZM/A": ["iPhone 6s Silicone Case", "Stone"],
    "MLCW2ZM/A": ["iPhone 6s Silicone Case", "Turquoise"],
    "MKY12ZM/A": ["iPhone 6s Silicone Case", "White"],

    "MLD22ZM/A": ["iPhone 6s Plus Silicone Case", "Antique White"],
    "MKXP2ZM/A": ["iPhone 6s Plus Silicone Case", "Blue"],
    "MKXJ2ZM/A": ["iPhone 6s Plus Silicone Case", "Charcoal Gray"],
    "MLD02ZM/A": ["iPhone 6s Plus Silicone Case", "Lavender"],
    "MKXL2ZM/A": ["iPhone 6s Plus Silicone Case", "Midnight Blue"],
    "MKXQ2ZM/A": ["iPhone 6s Plus Silicone Case", "Orange"],
    "MLCY2ZM/A": ["iPhone 6s Plus Silicone Case", "Pink"],
    "MKXM2ZM/A": ["iPhone 6s Plus Silicone Case", "(PRODUCT)RED"],
    "MKXN2ZM/A": ["iPhone 6s Plus Silicone Case", "Stone"],
    "MLD12ZM/A": ["iPhone 6s Plus Silicone Case", "Turquoise"],
    "MKXK2ZM/A": ["iPhone 6s Plus Silicone Case", "White"],

    "MLD32ZM/A": ["iPad mini 4 Silicone Case", "Blue"],
    "MKLK2ZM/A": ["iPad mini 4 Silicone Case", "Charcoal Gray"],
    "MLD62ZM/A": ["iPad mini 4 Silicone Case", "Lavender"],
    "MKLM2ZM/A": ["iPad mini 4 Silicone Case", "Midnight Blue"],
    "MLD42ZM/A": ["iPad mini 4 Silicone Case", "Orange"],
    "MLD52ZM/A": ["iPad mini 4 Silicone Case", "Pink"],
    "MKLN2ZM/A": ["iPad mini 4 Silicone Case", "(PRODUCT)RED"],
    "MKLP2ZM/A": ["iPad mini 4 Silicone Case", "Stone"],
    "MLD72ZM/A": ["iPad mini 4 Silicone Case", "Turquoise"],
    "MKLL2ZM/A": ["iPad mini 4 Silicone Case", "White"],

    "MKM12ZM/A": ["iPad mini 4 Smart Cover", "Blue"],
    "MKLV2ZM/A": ["iPad mini 4 Smart Cover", "Charcoal Gray"],
    "MKM42ZM/A": ["iPad mini 4 Smart Cover", "Lavender"],
    "MKLX2ZM/A": ["iPad mini 4 Smart Cover", "Midnight Blue"],
    "MKM22ZM/A": ["iPad mini 4 Smart Cover", "Orange"],
    "MKM32ZM/A": ["iPad mini 4 Smart Cover", "Pink"],
    "MKLY2ZM/A": ["iPad mini 4 Smart Cover", "(PRODUCT)RED"],
    "MKM02ZM/A": ["iPad mini 4 Smart Cover", "Stone"],
    "MKM52ZM/A": ["iPad mini 4 Smart Cover", "Turquoise"],
    "MKLW2ZM/A": ["iPad mini 4 Smart Cover", "White"],

    "MK0D2ZM/A": ["iPad Pro Silicone Case", "Charcoal Gray"],
    "MK0E2ZM/A": ["iPad Pro Silicone Case", "White"],
    "MK0L2ZM/A": ["iPad Pro Smart Cover", "Charcoal Gray"],
    "MLJK2ZM/A": ["iPad Pro Smart Cover", "White"]
}

early_2016 = {  # first ever spring drop!

    "MMM22ZM/A": ["iPhone 6s Leather Case", "Marigold"],
    "MM4G2ZM/A": ["iPhone 6s Leather Case", "Marine Blue"],
    "MM4D2ZM/A": ["iPhone 6s Leather Case", "Storm Gray"],

    "MMM32ZM/A": ["iPhone 6s Plus Leather Case", "Marigold"],
    "MM362ZM/A": ["iPhone 6s Plus Leather Case", "Marine Blue"],
    "MM322ZM/A": ["iPhone 6s Plus Leather Case", "Storm Gray"],

    "MM642ZM/A": ["iPhone 6s Silicone Case", "Apricot"],
    "MM622ZM/A": ["iPhone 6s Silicone Case", "Lavender"],
    "MM682ZM/A": ["iPhone 6s Silicone Case", "Light Pink"],
    "MM672ZM/A": ["iPhone 6s Silicone Case", "Mint"],
    "MM632ZM/A": ["iPhone 6s Silicone Case", "Royal Blue"],
    "MM662ZM/A": ["iPhone 6s Silicone Case", "Yellow"],

    "MM6F2ZM/A": ["iPhone 6s Plus Silicone Case", "Apricot"],
    "MM6D2ZM/A": ["iPhone 6s Plus Silicone Case", "Lavender"],
    "MM6A2ZM/A": ["iPhone 6s Plus Silicone Case", "Light Pink"],
    "MM692ZM/A": ["iPhone 6s Plus Silicone Case", "Mint"],
    "MM6E2ZM/A": ["iPhone 6s Plus Silicone Case", "Royal Blue"],
    "MM6H2ZM/A": ["iPhone 6s Plus Silicone Case", "Yellow"],

    "MMHH2ZM/A": ["iPhone SE Leather Case", "Black"],
    "MMHG2ZM/A": ["iPhone SE Leather Case", "Midnight Blue"],

    "MM3L2ZM/A": ["iPad mini 4 Silicone Case", "Light Pink"],
    "MMM42ZM/A": ["iPad mini 4 Silicone Case", "Lilac"],
    "MMJY2ZM/A": ["iPad mini 4 Silicone Case", "Mint"],
    "MM3M2ZM/A": ["iPad mini 4 Silicone Case", "Royal Blue"],
    "MM3Q2ZM/A": ["iPad mini 4 Silicone Case", "Yellow"],
    "MM3N2ZM/A": ["iPad mini 4 Silicone Case", "Apricot"],

    "MM2V2ZM/A": ["iPad mini 4 Smart Cover", "Apricot"],
    "MM2T2ZM/A": ["iPad mini 4 Smart Cover", "Light Pink"],
    "MMJW2ZM/A": ["iPad mini 4 Smart Cover", "Lilac"],
    "MMJV2ZM/A": ["iPad mini 4 Smart Cover", "Mint"],
    "MM2U2ZM/A": ["iPad mini 4 Smart Cover", "Royal Blue"],
    "MM2X2ZM/A": ["iPad mini 4 Smart Cover", "Yellow"],

    "MM262AM/A": ["iPad Pro 9.7″ Silicone Case", "Apricot"],
    "MM242AM/A": ["iPad Pro 9.7″ Silicone Case", "Light Pink"],
    "MMG52AM/A": ["iPad Pro 9.7″ Silicone Case", "Lilac"],
    "MMG42AM/A": ["iPad Pro 9.7″ Silicone Case", "Mint"],
    "MM252AM/A": ["iPad Pro 9.7″ Silicone Case", "Royal Blue"],
    "MM282AM/A": ["iPad Pro 9.7″ Silicone Case", "Yellow"],

    "MM2H2AM/A": ["iPad Pro 9.7″ Smart Cover", "Apricot"],
    "MM2F2AM/A": ["iPad Pro 9.7″ Smart Cover", "Light Pink"],
    "MMG72AM/A": ["iPad Pro 9.7″ Smart Cover", "Lilac"],
    "MMG62AM/A": ["iPad Pro 9.7″ Smart Cover", "Mint"],
    "MM2G2AM/A": ["iPad Pro 9.7″ Smart Cover", "Royal Blue"],
    "MM2K2AM/A": ["iPad Pro 9.7″ Smart Cover", "Yellow"],

    "MM222AM/A": ["iPad Pro 9.7″ Silicone Case", "(PRODUCT)RED"],
    "MM1Y2AM/A": ["iPad Pro 9.7″ Silicone Case", "Charcoal Grey"],
    "MM272AM/A": ["iPad Pro 9.7″ Silicone Case", "Lavender"],
    "MM212AM/A": ["iPad Pro 9.7″ Silicone Case", "Midnight Blue"],
    "MM232AM/A": ["iPad Pro 9.7″ Silicone Case", "Stone"],
    "MM202AM/A": ["iPad Pro 9.7″ Silicone Case", "White"],

    "MM2D2AM/A": ["iPad Pro 9.7″ Smart Cover", "(PRODUCT)RED"],
    "MM292AM/A": ["iPad Pro 9.7″ Smart Cover", "Charcoal Grey"],
    "MM2J2AM/A": ["iPad Pro 9.7″ Smart Cover", "Lavender"],
    "MM2C2AM/A": ["iPad Pro 9.7″ Smart Cover", "Midnight Blue"],
    "MM2E2AM/A": ["iPad Pro 9.7″ Smart Cover", "Stone"],
    "MM2A2AM/A": ["iPad Pro 9.7″ Smart Cover", "White"],

}

Autumn_2016 = {
    "MMY62ZM/A": ["iPhone 7 Leather Case", "(PRODUCT)RED"],
    "MMY52ZM/A": ["iPhone 7 Leather Case", "Black"],
    "MMY32ZM/A": ["iPhone 7 Leather Case", "Midnight Blue"],
    "MMY22ZM/A": ["iPhone 7 Leather Case", "Saddle Brown"],
    "MMY42ZM/A": ["iPhone 7 Leather Case", "Sea Blue"],
    "MMY12ZM/A": ["iPhone 7 Leather Case", "Storm Gray"],
    "MMY72ZM/A": ["iPhone 7 Leather Case", "Tan"],

    "MMWN2ZM/A": ["iPhone 7 Silicone Case", "(PRODUCT)RED"],
    "MMW82ZM/A": ["iPhone 7 Silicone Case", "Black"],
    "MMX22ZM/A": ["iPhone 7 Silicone Case", "Cocoa"],
    "MMWK2ZM/A": ["iPhone 7 Silicone Case", "Midnight Blue"],
    "MMWW2ZM/A": ["iPhone 7 Silicone Case", "Ocean Blue"],
    "MMX12ZM/A": ["iPhone 7 Silicone Case", "Pink Sand"],
    "MMX02ZM/A": ["iPhone 7 Silicone Case", "Sea Blue"],
    "MMWR2ZM/A": ["iPhone 7 Silicone Case", "Stone"],
    "MMWF2ZM/A": ["iPhone 7 Silicone Case", "White"],

    "MN002LL/A": ["iPhone 7 Smart Battery Case", "Black"],
    "MN012LL/A": ["iPhone 7 Smart Battery Case", "White"],

    "MMYK2ZM/A": ["iPhone 7 Plus Leather Case", "(PRODUCT)RED"],
    "MMYJ2ZM/A": ["iPhone 7 Plus Leather Case", "Black"],
    "MMYG2ZM/A": ["iPhone 7 Plus Leather Case", "Midnight Blue"],
    "MMYF2ZM/A": ["iPhone 7 Plus Leather Case", "Saddle Brown"],
    "MMYH2ZM/A": ["iPhone 7 Plus Leather Case", "Sea Blue"],
    "MMYE2ZM/A": ["iPhone 7 Plus Leather Case", "Storm Gray"],
    "MMYL2ZM/A": ["iPhone 7 Plus Leather Case", "Tan"],

    "MMQR2ZM/A": ["iPhone 7 Plus Silicone Case", "Black"],
    "MMT12ZM/A": ["iPhone 7 Plus Silicone Case", "Cocoa"],
    "MMQU2ZM/A": ["iPhone 7 Plus Silicone Case", "Midnight Blue"],
    "MMQX2ZM/A": ["iPhone 7 Plus Silicone Case", "Ocean Blue"],
    "MMT02ZM/A": ["iPhone 7 Plus Silicone Case", "Pink Sand"],
    "MMQV2ZM/A": ["iPhone 7 Plus Silicone Case", "PRODUCT(RED)"],
    "MMQY2ZM/A": ["iPhone 7 Plus Silicone Case", "Sea Blue"],
    "MMQW2ZM/A": ["iPhone 7 Plus Silicone Case", "Stone"],
    "MMQT2ZM/A": ["iPhone 7 Plus Silicone Case", "White"],

    # at a bit later date
    "MN022LL/A": ["iPhone 7 Smart Battery Case", "(PRODUCT)RED"],
    # at a bit later date
    "MNYV2ZM/A": ["iPhone SE Leather Case", "(PRODUCT)RED"],

    "MNNE2ZM/A": ["iPad mini 4 Silicone Case", "Cocoa"],
    "MN2N2ZM/A": ["iPad mini 4 Silicone Case", "Ocean Blue"],
    "MNND2ZM/A": ["iPad mini 4 Silicone Case", "Pink Sand"],
    "MN2P2ZM/A": ["iPad mini 4 Silicone Case", "Sea Blue"],

    "MNN52ZM/A": ["iPad mini 4 Smart Cover", "Cocoa"],
    "MN092ZM/A": ["iPad mini 4 Smart Cover", "Ocean Blue"],
    "MNN32ZM/A": ["iPad mini 4 Smart Cover", "Pink Sand"],
    "MN0A2ZM/A": ["iPad mini 4 Smart Cover", "Sea Blue"],

    "MNN82ZM/A": ["iPad Pro 9.7″ Silicone Case", "Cocoa"],
    "MN2F2ZM/A": ["iPad Pro 9.7″ Silicone Case", "Ocean Blue"],
    "MNN72ZM/A": ["iPad Pro 9.7″ Silicone Case", "Pink Sand"],
    "MN2G2ZM/A": ["iPad Pro 9.7″ Silicone Case", "Sea Blue"],

    "MNNC2ZM/A": ["iPad Pro 9.7″ Smart Cover", "Cocoa"],
    "MN462ZM/A": ["iPad Pro 9.7″ Smart Cover", "Ocean Blue"],
    "MNN92ZM/A": ["iPad Pro 9.7″ Smart Cover", "Pink Sand"],
    "MN472ZM/A": ["iPad Pro 9.7″ Smart Cover", "Sea Blue"]

}

early_2017 = {
    "MPVG2ZM/A": ["iPhone 7 Leather Case", "Berry"],
    "MPT92ZM/A": ["iPhone 7 Leather Case", "Sapphire"],
    "MPT62ZM/A": ["iPhone 7 Leather Case", "Taupe"],

    "MQ0J2ZM/A": ["iPhone 7 Silicone Case", "Azure"],
    "MQ0K2ZM/A": ["iPhone 7 Silicone Case", "Camellia"],
    "MQ0L2ZM/A": ["iPhone 7 Silicone Case", "Pebble"],

    "MPVU2ZM/A": ["iPhone 7 Plus Leather Case", "Berry"],
    "MPTF2ZM/A": ["iPhone 7 Plus Leather Case", "Sapphire"],
    "MPTC2ZM/A": ["iPhone 7 Plus Leather Case", "Taupe"],

    "MQ0N2ZM/A": ["iPhone 7 Plus Silicone Case", "Camellia"],
    "MQ0P2ZM/A": ["iPhone 7 Plus Silicone Case", "Pebble"],

    "MNYW2ZM/A": ["iPhone SE Leather Case", "Saddle Brown"],
    # TODO check/fix color years?
    "MQ4L2ZM/A": ["iPad Smart Cover", "Charcoal Gray"],
    "MQ4P2ZM/A": ["iPad Smart Cover", "Midnight Blue"],
    "MQ4Q2ZM/A": ["iPad Smart Cover", "Pink Sand"],
    "MQ4M2ZM/A": ["iPad Smart Cover", "White"],
    "MQ4N2ZM/A": ["iPad Smart Cover", "(PRODUCT)RED"],
}

wwdc_2017 = {
    "MPU62ZM/A": ["iPad Pro 10.5″ Leather Sleeve", "Black"],
    "MPU22ZM/A": ["iPad Pro 10.5″ Leather Sleeve", "Midnight Blue"],
    "MPU12ZM/A": ["iPad Pro 10.5″ Leather Sleeve", "Saddle Brown"],
    "MPU02ZM/A": ["iPad Pro 10.5″ Leather Sleeve", "Taupe"],

    "MPUD2ZM/A": ["iPad Pro 10.5″ Leather Smart Cover", "Black"],
    "MPUA2ZM/A": ["iPad Pro 10.5″ Leather Smart Cover", "Midnight Blue"],
    "MPU92ZM/A": ["iPad Pro 10.5″ Leather Smart Cover", "Saddle Brown"],
    # yes really lol
    "MPU82ZM/A": ["iPad Pro 10.5″ Leather Smart Cover", "Taupe"],
    # also fits iPad Air 3, obv

    "MQ082ZM/A": ["iPad Pro 10.5″ Smart Cover", "Charcoal Gray"],
    "MQ4U2ZM/A": ["iPad Pro 10.5″ Smart Cover", "Flamingo"],
    "MQ092ZM/A": ["iPad Pro 10.5″ Smart Cover", "Midnight Blue"],
    "MQ4T2ZM/A": ["iPad Pro 10.5″ Smart Cover", "Mist Blue"],
    "MQ0E2ZM/A": ["iPad Pro 10.5″ Smart Cover", "Pink Sand"],
    "MQ4V2ZM/A": ["iPad Pro 10.5″ Smart Cover", "Pollen"],
    "MPQM2ZM/A": ["iPad Pro 10.5″ Smart Cover", "White"],
    "MQ0G2ZM/A": ["iPad Pro 12.9″ Smart Cover", "Charcoal Gray"],
    "MQ0H2ZM/A": ["iPad Pro 12.9″ Smart Cover", "White"],

    "MQ0U2ZM/A": ["iPad Pro 12.9″ Leather Sleeve", "Black"],
    "MQ0T2ZM/A": ["iPad Pro 12.9″ Leather Sleeve", "Midnight Blue"],
    "MQ0Q2ZM/A": ["iPad Pro 12.9″ Leather Sleeve", "Saddle Brown"],

    "MPV62ZM/A": ["iPad Pro 12.9″ Leather Smart Cover", "Black"],
    "MPV22ZM/A": ["iPad Pro 12.9″ Leather Smart Cover", "Midnight Blue"],
    "MPV12ZM/A": ["iPad Pro 12.9″ Leather Smart Cover", "Saddle Brown"],

    # SKUs are different from the 2015 ones!

    "MQ0X2ZM/A": ["Apple Pencil Case", "Black"],
    "MQ0W2ZM/A": ["Apple Pencil Case", "Midnight Blue"],
    "MQ0V2ZM/A": ["Apple Pencil Case", "Saddle Brown"],
    "MPQL2ZM/A": ["Apple Pencil Case", "Taupe"],

    "MQ5F2ZM/A": ["iPhone 7 Leather Case", "Geranium"],
    "MQ5G2ZM/A": ["iPhone 7 Leather Case", "Sunflower"],

    "MQ592ZM/A": ["iPhone 7 Silicone Case", "Flamingo"],
    "MQ582ZM/A": ["iPhone 7 Silicone Case", "Mist Blue"],
    "MQ5A2ZM/A": ["iPhone 7 Silicone Case", "Pollen"],

    "MQ5H2ZM/A": ["iPhone 7 Plus Leather Case", "Geranium"],
    "MQ5J2ZM/A": ["iPhone 7 Plus Leather Case", "Sunflower"],

    "MQ5D2ZM/A": ["iPhone 7 Plus Silicone Case", "Flamingo"],
    "MQ5C2ZM/A": ["iPhone 7 Plus Silicone Case", "Mist Blue"],
    "MQ5E2ZM/A": ["iPhone 7 Plus Silicone Case", "Pollen"],
}

Autumn_2017 = {
    "MQHA2ZM/A": ["iPhone 8 / 7 Leather Case", "(PRODUCT)RED"],
    "MQH92ZM/A": ["iPhone 8 / 7 Leather Case", "Black"],
    "MQH82ZM/A": ["iPhone 8 / 7 Leather Case", "Midnight Blue"],
    "MQH72ZM/A": ["iPhone 8 / 7 Leather Case", "Saddle Brown"],
    "MQH62ZM/A": ["iPhone 8 / 7 Leather Case", "Taupe"],
    "MQHF2ZM/A": ["iPhone 8 / 7 Leather Case", "Cosmos Blue"],

    "MQGP2ZM/A": ["iPhone 8 / 7 Silicone Case", "(PRODUCT)RED"],
    "MQGK2ZM/A": ["iPhone 8 / 7 Silicone Case", "Black"],
    "MQGM2ZM/A": ["iPhone 8 / 7 Silicone Case", "Midnight Blue"],
    "MQGQ2ZM/A": ["iPhone 8 / 7 Silicone Case", "Pink Sand"],
    "MQGL2ZM/A": ["iPhone 8 / 7 Silicone Case", "White"],
    # something else maybe?

    "MQHN2ZM/A": ["iPhone 8 Plus / 7 Plus Leather Case", "(PRODUCT)RED"],
    "MQHM2ZM/A": ["iPhone 8 Plus / 7 Plus Leather Case", "Black"],
    "MQHL2ZM/A": ["iPhone 8 Plus / 7 Plus Leather Case", "Midnight Blue"],
    "MQHK2ZM/A": ["iPhone 8 Plus / 7 Plus Leather Case", "Saddle Brown"],
    "MQHJ2ZM/A": ["iPhone 8 Plus / 7 Plus Leather Case", "Taupe"],
    "MQHR2FE/A": ["iPhone 8 Plus / 7 Plus Leather Case", "Cosmos Blue"],

    "MQH12ZM/A": ["iPhone 8 Plus / 7 Plus Silicone Case", "(PRODUCT)RED"],
    "MQGW2ZM/A": ["iPhone 8 Plus / 7 Plus Silicone Case", "Black"],
    "MQGY2ZM/A": ["iPhone 8 Plus / 7 Plus Silicone Case", "Midnight Blue"],
    "MQH22ZM/A": ["iPhone 8 Plus / 7 Plus Silicone Case", "Pink Sand"],
    "MQGX2ZM/A": ["iPhone 8 Plus / 7 Plus Silicone Case", "White"],

    "MQTE2ZM/A": ["iPhone X Leather Case", "(PRODUCT)RED"],
    "MQTD2ZM/A": ["iPhone X Leather Case", "Black"],
    "MQTC2ZM/A": ["iPhone X Leather Case", "Midnight Blue"],
    "MQTA2ZM/A": ["iPhone X Leather Case", "Saddle Brown"],
    "MQT92ZM/A": ["iPhone X Leather Case", "Taupe"],

    # TODO there are more!!
    "MQRV2ZM/A": ["iPhone X Leather Folio", "Black"],

    "MQT52ZM/A": ["iPhone X Silicone Case", "(PRODUCT)RED"],
    "MQT12ZM/A": ["iPhone X Silicone Case", "Black"],
    "MQT32ZM/A": ["iPhone X Silicone Case", "Midnight Blue"],
    "MQT62ZM/A": ["iPhone X Silicone Case", "Pink Sand"],
    "MQT22ZM/A": ["iPhone X Silicone Case", "White"],

    "MR5L2ZM/A": ["iPad Pro 10.5″ Leather Sleeve", "(PRODUCT)RED"],
    "MR5G2ZM/A": ["iPad Pro 10.5″ Leather Smart Cover", "(PRODUCT)RED"],
    "MR592ZM/A": ["iPad Pro 10.5″ Smart Cover", "(PRODUCT)RED"],

    "MQG02ZM/A": ["Leather Sleeve for 12-inch MacBook", "Midnight Blue"],
    "MQG12ZM/A": ["Leather Sleeve for 12-inch MacBook", "Saddle Brown"]
}

spring_2018 = {
    "MRG82ZM/A": ["iPhone 8 / 7 Leather Case", "Bright Orange"],
    "MRG52ZM/A": ["iPhone 8 / 7 Leather Case", "Electric Blue"],
    "MRG62ZM/A": ["iPhone 8 / 7 Leather Case", "Soft Pink"],
    "MRG72ZM/A": ["iPhone 8 / 7 Leather Case", "Spring Yellow"],

    "MRFR2ZM/A": ["iPhone 8 / 7 Silicone Case", "Denim Blue"],
    "MRFU2ZM/A": ["iPhone 8 / 7 Silicone Case", "Lemonade"],
    "MRFQ2ZM/A": ["iPhone 8 / 7 Silicone Case", "Red Raspberry"],

    "MRGD2ZM/A": ["iPhone 8 Plus / 7 Plus Leather Case", "Bright Orange"],
    "MRG92ZM/A": ["iPhone 8 Plus / 7 Plus Leather Case", "Electric Blue"],
    "MRGA2ZM/A": ["iPhone 8 Plus / 7 Plus Leather Case", "Soft Pink"],
    "MRGC2ZM/A": ["iPhone 8 Plus / 7 Plus Leather Case", "Spring Yellow"],

    "MRFX2ZM/A": ["iPhone 8 Plus / 7 Plus Silicone Case", "Denim Blue"],
    "MRFY2ZM/A": ["iPhone 8 Plus / 7 Plus Silicone Case", "Lemonade"],
    "MRFW2ZM/A": ["iPhone 8 Plus / 7 Plus Silicone Case", "Red Raspberry"],

    "MRGK2ZM/A": ["iPhone X Leather Case", "Bright Orange"],
    "MRGG2ZM/A": ["iPhone X Leather Case", "Electric Blue"],
    "MRGH2ZM/A": ["iPhone X Leather Case", "Soft Pink"],
    "MRGJ2ZM/A": ["iPhone X Leather Case", "Spring Yellow"],

    "MRGE2ZM/A": ["iPhone X Leather Folio", "Electric Blue"],
    "MRGF2ZM/A": ["iPhone X Leather Folio", "Soft Pink"],
    "MRQD2ZM/A": ["iPhone X Leather Folio", "(PRODUCT)RED"],

    "MRG22ZM/A": ["iPhone X Silicone Case", "Denim Blue"],
    "MRG32ZM/A": ["iPhone X Silicone Case", "Lemonade"],
    "MRG12ZM/A": ["iPhone X Silicone Case", "Red Raspberry"],

    "MRFL2ZM/A": ["iPad Pro 10.5″ Leather Sleeve ", "Electric Blue"],
    "MRFM2ZM/A": ["iPad Pro 10.5″ Leather Sleeve ", "Soft Pink"],
    "MRFJ2ZM/A": ["iPad Pro 10.5″ Leather Smart Cover", "Electric Blue"],
    "MRFK2ZM/A": ["iPad Pro 10.5″ Leather Smart Cover", "Soft Pink"],
    "MRFG2ZM/A": ["Smart Cover for 10.5‐inch iPad Pro", "Lemonade"],
    "MRFF2ZM/A": ["Smart Cover for 10.5‐inch iPad Pro", "Raspberry"]
    # no iPad Pro 12.9 covers back because...
}

wwdc_2018 = {
    "MRR72ZM/A": ["iPhone 8 / 7 Silicone Case", "Marine Green"],
    "MRR52ZM/A": ["iPhone 8 / 7 Silicone Case", "Peach"],
    "MRR62ZM/A": ["iPhone 8 / 7 Silicone Case", "Sky Blue"],

    "MRRA2ZM/A": ["iPhone 8 Plus / 7 Plus Silicone Case", "Marine Green"],
    "MRR82ZM/A": ["iPhone 8 Plus / 7 Plus Silicone Case", "Peach"],
    "MRR92ZM/A": ["iPhone 8 Plus / 7 Plus Silicone Case", "Sky Blue"],

    "MRRE2ZM/A": ["iPhone X Silicone Case", "Marine Green"],
    "MRRC2ZM/A": ["iPhone X Silicone Case", "Peach"],
    "MRRD2ZM/A": ["iPhone X Silicone Case", "Sky Blue"],
}

late_2018 = {
    # https://www.macrumors.com/2018/09/12/apple-releases-iphone-xs-xs-max-cases/
    # + XR Clear Case
}

# https://www.macrumors.com/2019/03/20/spring-colors-cases-bands/
