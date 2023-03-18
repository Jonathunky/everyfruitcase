import json
import os


def normalize_filename(filename):
	# Remove any braces
	filename = filename.replace('(', '').replace(')', '')

	# Replace any spaces with underscores
	filename = filename.replace(' ', '_')

	return filename


colors = {  # let's use colors as a baseline! I'm a fucking genius!!! Hell yes!
	# TODO 2010, 2011, 2012 iPad Smart covers and Smart Cases!
	# There were leather and silicone iPad 4 smart covers
	"Late 2013": {
		# https://www.macrumors.com/2013/10/22/apples-smart-covers-and-smart-cases-updated-for-new-ipads/
		"Beige": ["iphone_5s_leather", "ipad_2013_smart_case"],
		"Black": ["iphone_5s_leather", "ipad_2013_smart_case", "ipad_2013_cover", "iphone_5c_case"],
		"Blue": ["iphone_5s_leather", "ipad_2013_smart_case", "ipad_2013_cover", "iphone_5c_case"],
		"Brown": ["iphone_5s_leather", "ipad_2013_smart_case"],
		"Yellow": ["iphone_5s_leather", "ipad_2013_smart_case", "ipad_2013_cover", "iphone_5c_case"],
		"(PRODUCT)RED": ["iphone_5s_leather", "ipad_2013_smart_case", "ipad_2013_cover"],
		"Pink": ["ipad_2013_cover", "iphone_5c_case"],
		"Green": ["ipad_2013_cover", "iphone_5c_case"],
		"White": ["iphone_5c_case"]
	},
	"Late 2014": {
		# https://www.macrumors.com/2014/09/09/apple-iphone-6-cases/
		# https://www.macrumors.com/2014/10/16/apple-new-smart-cases/
		"(PRODUCT)RED": ["iphone_6_leather", "iphone_6_silicone", "ipad_2014_cover", "ipad_2014_smart_case"],
		"Black": ["iphone_6_leather", "iphone_6_silicone", "ipad_2014_cover", "ipad_2014_smart_case"],
		"Midnight Blue": ["iphone_6_leather", "ipad_2014_smart_case"],
		"Olive Brown": ["iphone_6_leather", "ipad_2014_smart_case"],
		"Soft Pink": ["iphone_6_leather", "ipad_2014_smart_case"],
		"Blue": ["iphone_6_silicone", "ipad_2014_cover"],
		"Pink": ["iphone_6_silicone", "ipad_2014_cover"],
		"Green": ["iphone_6_silicone", "ipad_2014_cover"],
		"White": ["iphone_6_silicone", "ipad_2014_cover"],
		"Yellow": ["ipad_2014_cover"]
	},
	"Late 2015": {
		"Lavender": ["ipad_2015_weirdness", "iphone_6s_silicone"],
		"Orange": ["ipad_2015_weirdness", "iphone_6s_silicone"],
		"White": ["ipad_2015_weirdness", "iphone_6s_silicone", "ipad_pro_2015", "iphone_6s_battery"],
		"Midnight Blue": ["ipad_2015_weirdness", "iphone_6s_silicone", "iphone_6s_leather"],
		"Blue": ["ipad_2015_weirdness", "iphone_6s_silicone"],
		"Light Pink": ["ipad_2015_weirdness", "iphone_6s_silicone"],
		"(PRODUCT)RED": ["ipad_2015_weirdness", "iphone_6s_silicone"],
		"Charcoal Gray": ["ipad_2015_weirdness", "iphone_6s_silicone", "ipad_pro_2015_smart_keyboard", "iphone_6s_battery"],
		"Stone": ["ipad_2015_weirdness", "iphone_6s_silicone"],
		"Antique White": ["ipad_2015_weirdness", "iphone_6s_silicone"],
		"Turquoise": ["ipad_2015_weirdness", "iphone_6s_silicone"],
		"Black": ["iphone_6s_leather"],
		"Saddle Brown": ["iphone_6s_leather"],
		"Rose Gray": ["iphone_6s_leather"],
		"Brown": ["iphone_6s_leather"]
	},
	"Early 2016": {
		'Yellow': ["iphone_6s_silicone", "ipad_2015_weirdness"],
		'Royal Blue': ["iphone_6s_silicone", "ipad_2015_weirdness"],
		'Apricot': ["iphone_6s_silicone", "ipad_2015_weirdness"],
		'Lilac': ["iphone_6s_silicone", "ipad_2015_weirdness"],
		'Mint': ["iphone_6s_silicone", "ipad_2015_weirdness"],
		'Marine Blue': ["iphone_6s_leather"],
		'Storm Gray': ["iphone_6s_leather"],
		'Marigold': ["iphone_6s_leather"]
	},
	#TODO
	"Late 2016": {
		# iPhone 7 and iPhone 7 Plus cases
		"Black": ["iphone_7_leather", "iphone_7_silicone"],
		"Midnight Blue": ["iphone_7_leather", "iphone_7_silicone"],
		"Sea Blue": ["iphone_7_leather"],
		"Saddle Brown": ["iphone_7_leather"],
		"Storm Gray": ["iphone_7_leather"],
		"Rose Gray": ["iphone_7_leather"],
		"Marine Blue": ["iphone_7_silicone"],
		"Ocean Blue": ["iphone_7_silicone"],
		"Stone": ["iphone_7_silicone"],
		"Turquoise": ["iphone_7_silicone"],
		"Antique White": ["iphone_7_silicone"],
		"Lilac": ["iphone_7_silicone"],
		"Mist Blue": ["iphone_7_silicone"],
		"Bright Pink": ["iphone_7_silicone"],
		"Apricot": ["iphone_7_silicone"],
		"Light Pink": ["iphone_7_silicone"],
		"Yellow": ["iphone_7_silicone"],
		"Orange": ["iphone_7_silicone"],
		"Charcoal Gray": ["iphone_7_silicone"],
		"Lavender": ["iphone_7_silicone"]
	},
	"Early 2017": {
			"Camellia": ["iphone_7_leather", "iphone_7_silicone"],
			"Berry": ["iphone_7_leather", "iphone_7_silicone"],
			"Azure": ["iphone_7_leather", "iphone_7_silicone"],
			"Pebble": ["iphone_7_leather", "iphone_7_silicone"]
		},
	"Late 2017": {
		"Cosmos Blue": ["iphone_2017_leather", "iphone_x_folio"],
		"Saddle Brown": ["iphone_2017_leather", "iphone_x_folio"],
		"Taupe": ["iphone_2017_leather", "iphone_x_folio"],
		"Black": ["iphone_2017_leather", "iphone_x_folio", "iphone_2017_silicone"],
		"Midnight Blue": ["iphone_2017_leather", "iphone_x_folio", "iphone_2017_silicone"],
		"(PRODUCT)RED": ["iphone_2017_leather", "iphone_2017_silicone"],
		"Pink Sand": ["iphone_2017_silicone"],
		"White": ["iphone_2017_silicone"],
		"Yellow": ["iphone_2017_silicone"],
		"Blue Cobalt": ["iphone_2017_silicone"],
	},
	"Early 2018": {
		# https://www.macstories.net/news/apple-introduces-new-spring-colors-for-iphone-and-ipad-accessories-space-gray-mac-accessories-now-available/
		"Electric Blue": ["iphone_x_folio", "iphone_2017_leather"],
		"Soft Pink": ["iphone_x_folio", "iphone_2017_leather"],
		"Spring Yellow": ["iphone_2017_leather"],
		"Bright Orange": ["iphone_2017_leather"],
		"Red Raspberry": ["iphone_2017_silicone"],
		"Lemonade": ["iphone_2017_silicone"],
		"Denim Blue": ["iphone_2017_silicone"]
	},
	"Late 2018": {
		"Peony Pink": ["iphone_xs_leather", "iphone_xs_folio"],
		"Cape Cod Blue": ["iphone_xs_leather", "iphone_xs_folio"],
		"Forest Green": ["iphone_xs_leather", "iphone_xs_folio"],
		"Taupe": ["iphone_xs_leather"],
		"Midnight Blue": ["iphone_xs_leather", "iphone_xs_silicone"],
		"Saddle Brown": ["iphone_xs_leather"],
		"Black": ["iphone_xs_leather", "iphone_xs_folio", "iphone_xs_silicone", "iphone_xs_battery",
							"iphone_xr_battery"],
		"(PRODUCT)RED": ["iphone_xs_leather", "iphone_xs_folio", "iphone_xs_silicone"],
		"Nectarine": ["iphone_xs_silicone"],
		"Lavender Gray": ["iphone_xs_silicone"],
		"Blue Horizon": ["iphone_xs_silicone"],
		"Stone": ["iphone_xs_silicone"],
		"Pink Sand": ["iphone_xs_silicone"],
		"White": ["iphone_xs_silicone", "iphone_xs_battery", "iphone_xr_battery"],
		"Clear": ["iphone_xr"]
	},
	"Early 2019": {
		# https://www.macrumors.com/2019/03/20/spring-colors-cases-bands/
		"Spearmint": ["iphone_xs_silicone"],
		"Papaya": ["iphone_xs_silicone"],
		"Delft Blue": ["iphone_xs_silicone"],
		"Cornflower": ["iphone_xs_leather", "iphone_xs_folio"],
		"Sunset": ["iphone_xs_leather", "iphone_xs_folio"],
		"Lilac": ["iphone_xs_leather", "iphone_xs_folio"],
		"Pink Sand": ["iphone_xs_battery", "iphone_xr_battery"]
	},
	"Late 2019": {
		# https://www.macrumors.com/2019/09/10/new-cases-for-iphone-11/
		"Meyer Lemon": ["iphone_2019_leather"],
		"Forest Green": ["iphone_2019_leather"],
		"Midnight Blue": ["iphone_2019_leather", "iphone_2019_silicone"],
		"Saddle Brown": ["iphone_2019_leather"],
		"Black": ["iphone_2019_leather", "iphone_11_silicone", "iphone_11_battery"],
		"(PRODUCT)RED": ["iphone_2019_leather", "iphone_2019_silicone"],
		"Clementine": ["iphone_2019_silicone"],
		"Pine Green": ["iphone_2019_silicone"],
		"Alaskan Blue": ["iphone_2019_silicone"],
		"Pink Sand": ["iphone_2019_silicone", "iphone_2019_battery"],
		"White": ["iphone_11_silicone", "iphone_11_battery"],
		"Aubergine": ["iphone_2019_folio"],
		"Clear": ["iphone_2019_clear"]
	},
	"Early 2020": {
		# https://www.macrumors.com/2020/03/18/apple-cases-spring-color-options/
		"Peacock": ["iphone_2019_folio"],
		"Cactus": ["iphone_11_silicone"],
		"Grapefruit": ["iphone_11_silicone"],
		"Surf Blue": ["iphone_11_silicone"]
	},
	"Late 2020": {
		"Black": ["iphone_2020_leather", "iphone_2020_silicone"],
		"Saddle Brown": ["iphone_2020_leather", "iphone_2020_sleeve", "magsafe_wallet"],
		"(PRODUCT)RED": ["iphone_2020_leather", "iphone_2020_sleeve", "iphone_2020_silicone"],
		"Blue": ["iphone_2020_leather"],
		"California Poppy": ["iphone_2020_leather", "magsafe_wallet"],
		"Baltic Blue": ["iphone_2020_sleeve", "magsafe_wallet"],
		"Pink Citrus": ["iphone_2020_sleeve", "iphone_2020_silicone"],
		"White": ["iphone_2020_silicone"],
		"Deep Navy": ["iphone_2020_silicone"],
		"Cyprus Green": ["iphone_2020_silicone"],
		"Kumquat": ["iphone_2020_silicone"],
		"Plum": ["iphone_2020_silicone"],
		"Clear": ["iphone_2020_clear"]
	},
	"Early 2021": {
		"Arizona": ["iphone_2020_leather"],
		"Baltic Blue": ["iphone_2020_leather"],
		"California Poppy": ["iphone_2020_leather"],
		"Golden Brown": ["iphone_2020_leather"],
		"Red": ["iphone_2020_leather"],
		"Amethyst": ["iphone_2020_silicone"],
		"Cantaloupe": ["iphone_2020_silicone"],
		"Capri Blue": ["iphone_2020_silicone"],
		"Pistachio": ["iphone_2020_silicone"],
		"Sunflower": ["iphone_2020_silicone"]
	}
	# TODO there were also Early 2021 wallets!!
	# TODO Late 2021, Early 2022, Late 2022, Early 2023
	# TODO iPads, AirTag loops, Dock stations and such
}

models = {
	"iphone_5s_leather": "iPhone 5s Leather Case",
	"iphone_5c_case": "iPhone 5c Case",
	"ipad_2013_smart_case": "iPad Air & Mini 2 Smart Case",
	"ipad_2013_cover": "iPad Air & Mini 2 Smart Cover",

	"iphone_6_leather": "iPhone 6 / 6 Plus Leather Case",
	"iphone_6_silicone": "iPhone 6 / 6 Plus Silicone Case",
	"ipad_2014_cover": "iPad Air 2 & Mini 3 Smart Cover",
	"ipad_2014_smart_case": "iPad Air 2 & Mini 3 Smart Case",

	"ipad_2016_weirdness": "iPad mini 4 Smart Cover & Silicone Case",
	"iphone_6s_silicone": "iPhone 6s / 6s Plus Silicone Case",
	"iphone_6s_leather": "iPhone 6s / 6s Plus Leather Case",
	"iphone_6s_battery": "iPhone 6s Smart Battery Case",
	"ipad_pro_2015": "iPad Pro 12.9\u2033 Silicone Case",
	"ipad_pro_2015_smart_keyboard": "iPad Pro 12.9\u2033 Smart Keyboard & Silicone Case",
	"ipad_2015_weirdness": "iPad Pro 9.7\u2033, iPad Mini 4 Smart Cover & Silicone Case",

	"iphone_7_leather": "iPhone 7 / 7 Plus Leather Case",
	"iphone_7_silicone": "iPhone 7 / 7 Plus Silicone Case",

	"iphone_x_folio": "iPhone X Leather Folio",
	"iphone_2017_leather": "iPhone X / 8 / 8 Plus Leather Case",
	"iphone_2017_silicone": "iPhone X / 8 / 8 Plus Silicone Case",

	"ipad_pro_105_leather": "iPad Pro 10.5\u2033 Leather Cover",
	"ipad_pro_105_sleeve": "iPad Pro 10.5\u2033 Leather Sleeve",
	"ipad_pro_105_silicone": "iPad Pro 10.5\u2033 Smart Cover",

	"iphone_xs_leather": "iPhone Xs / Xs Max Leather Case",
	"iphone_xs_folio": "iPhone Xs / Xs Max Leather Folio",
	"iphone_xs_silicone": "iPhone Xs / Xs Max Silicone Case",
	"iphone_xr": "iPhone Xr Clear Case",
	"iphone_xs_battery": "iPhone Xs / Xs Max Battery Case",
	"iphone_xr_battery": "iPhone Xr Battery Case",

	"iphone_2019_leather": "iPhone 11 Pro / Max Leather Case",
	"iphone_2019_folio": "iPhone 11 Pro / Max Leather Folio",
	"iphone_2019_silicone": "iPhone 11 Pro / Max Silicone Case",
	"iphone_11_silicone": "iPhone 11 / Pro / Max Silicone Case",
	"iphone_2019_battery": "iPhone 11 Pro / Max Smart Battery Case",
	"iphone_11_battery": "iPhone 11 / Pro / Max Smart Battery Case",
	"iphone_2019_clear": "iPhone 11 / Pro / Max Clear Case",

	"iphone_2020_leather": "iPhone 12 series Leather Case with MagSafe",
	"iphone_2020_sleeve": "iPhone 12 series Leather Sleeve with MagSafe",
	"iphone_2020_silicone": "iPhone 12 series Silicone Case with MagSafe",
	"iphone_2020_clear": "iPhone 12 series Clear Case with MagSafe",

	"magsafe_wallet": "iPhone Leather Wallet with MagSafe",
	"magsafe_wallet_findmy": "iPhone Leather Wallet with MagSafe"
}

# Year / Color / Device
for drop, drop_data in colors.items():
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
