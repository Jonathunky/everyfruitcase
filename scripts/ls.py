import os


def list_markdown_files(directory, output_file="models.txt"):
    md_files = []

    # Walk through directory including its subdirectories
    for dirpath, dirnames, filenames in os.walk(directory):
        # Check if "ipad" is in the directory path
        if "ipad_pro4" in dirpath.lower():
            for filename in filenames:
                if filename.endswith(".md"):
                    # Append only the file name without extension
                    md_files.append(os.path.splitext(filename)[0])

    with open(output_file, "w") as f:
        f.write("everyphone:\n")
        for file_name in md_files:
            f.write(file_name + "_AV01\n")
            f.write(file_name + "_AV1\n")
            f.write(file_name + "_AV02\n")
            f.write(file_name + "_AV2\n")
            f.write(file_name + "_AV03\n")
            f.write(file_name + "_AV3\n")
            f.write(file_name + "_AV04\n")
            f.write(file_name + "_AV4\n")

            f.write(file_name + "_AV01_SILVER\n")
            f.write(file_name + "_AV1_SILVER\n")
            f.write(file_name + "_AV02_SILVER\n")
            f.write(file_name + "_AV2_SILVER\n")
            f.write(file_name + "_AV03_SILVER\n")
            f.write(file_name + "_AV3_SILVER\n")
            f.write(file_name + "_AV04_SILVER\n")
            f.write(file_name + "_AV4_SILVER\n")

    # Join file names with a newline and return
    return "\n".join(md_files)


# Example usage:
directory_path = "./pages"  # Replace with your folder path
list_markdown_files(directory_path)
