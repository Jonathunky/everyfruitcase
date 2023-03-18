import json
import os
import colors
from models import models


def normalize_filename(filename):
	# Remove any braces
	filename = filename.replace('(', '').replace(')', '')

	# Replace any spaces with underscores
	filename = filename.replace(' ', '_')

	return filename



# Year / Color / Device
for drop, drop_data in colors.colors.items():
	os.makedirs(normalize_filename(drop), exist_ok=True)  # create Year folder
	color_folders = {}

	# color | released things
	for color, things in drop_data.items():
		if color != "Clear":
		# create folder for each color
			dir = normalize_filename(drop + "/" + color)
			os.makedirs(dir, exist_ok=True)
		# and mark them in a JSON file with color folders
			color_folders[normalize_filename(color)] = color
		else:
			dir = normalize_filename(drop + "/" + color)
			os.makedirs(dir, exist_ok=True)
			print(color)
			color_folders[normalize_filename(color)] = "Clear Case"
			with open(os.path.join(normalize_filename(drop + "/" + "clear.md")), "a+") as f:
				f.seek(0)  # Move the cursor to the beginning of the file
				if len(f.read(1)) == 0:  # Check if the file is empty
					f.write("# You've stumbled upon a placeholder 🫠")

		# now inside of that folder let's generate a json with models
		jsonchik = {}
		for model in things:
			array = dict(title=models[model], href=normalize_filename("/" + drop + "/" + model.split('_')[0] + "_drop"))
			jsonchik[model] = array
			with open(os.path.join(normalize_filename(drop + "/" + model.split('_')[0] + "_drop.md")), "a+") as f:
				f.seek(0)  # Move the cursor to the beginning of the file
				if len(f.read(1)) == 0:  # Check if the file is empty
					f.write("# You've stumbled upon a placeholder 🫠")
			theme = {
				"pagination": False
			}
			array = dict(title=models[model].split(' ')[0] + " Case Drop", display="hidden", theme=theme)
			color_folders[model.split('_')[0] + "_drop"] = array

		# print(json.dumps(jsonchik, indent=4))

		with open(os.path.join(normalize_filename(drop + "/" + color), "_meta.json"), "w") as color_file:
			color_file.write(json.dumps(jsonchik, indent=4))

	with open(os.path.join(normalize_filename(drop + "/"), "_meta.json"), "w") as drop_file:
		drop_file.write(json.dumps(color_folders, indent=4))
		'''
				# JSON generation
		color_folders[normalize_filename(color)] = color
		device_files = {}

		# create markdown file for each model
		for model in things:
			device_files[normalize_filename(model)] = models[model]
			filename = os.path.join(dir, normalize_filename(model) + ".md")
			if os.path.exists(filename):
				with open(filename, "r+") as color_file:
					color_file.seek(0)
					color_file.write("# " + models[model] + " – " + color + "\n")
			else:
				with open(filename, "w") as color_file:
					color_file.write("# " + models[model] + " – " + color + "\n ")


'''
