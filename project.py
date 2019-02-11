# Jordan Tantuico, David Kim, Philip Cho
# I pledge my honor that I have abided by the Stevens Honor System

# Individuals (ids, name) in order of id
# Families (ids, hubby, wifey) in order of id

# Stores the file
gedcomFile = open("projectTest.ged")

# Stores all the valid tags at their corresponding levels
tags = {'0': ['HEAD', 'TRLR', 'NOTE'],
		'1': ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'],
		'2': ['DATE']}
specialTags = {'0': ['INDI', 'FAM']}

# Dictionary of Individuals
individuals = {}
# Dictionary of Families
families = {}

indi_or_fam = 'indi'
birt_or_deat = 'BIRT'
marr_or_div = 'MARR'
current_id = ''
# Reads each line in the file
for line in gedcomFile:
	line = line.rstrip("\r\n")
	print("--> " + line)

	components = line.split(" ",2)
	# in case there's only 2 args
	if len(components) == 2:
		components.append("")
	# default input
	level = components[0]
	tag = components[1]
	args = components[2]
	valid = "N"
	# Checks whether the tag is valid
	if components[0] not in tags:
		# invalid, level doesn't exist
		pass
	elif components[1] in tags[components[0]]:
		# valid, general case
		valid = "Y"
		if level == '0':
			pass
		elif tag == 'DATE':
			if indi_or_fam == 'indi':
				individuals[current_id][birt_or_deat] = args
			else:
				families[current_id][marr_or_div] = args
		elif indi_or_fam == 'indi':
			if tag == 'BIRT' or tag == 'DEAT':
				birt_or_deat = tag
			else:
				individuals[current_id][tag] = args
		elif indi_or_fam == 'fam':
			if tag == 'MARR' or tag == 'DIV':
				marr_or_div = tag
			else:
				families[current_id][tag] = args
	elif components[0] in specialTags and components[2] in specialTags[components[0]]:
		# valid, tag is third component
		valid = "Y"
		tag = components[2]
		args = components[1]
		if tag == 'INDI' :
			individuals[args] = {}
			indi_or_fam = 'indi'
		else :
			families[args] = {}
			indi_or_fam = 'fam'
		current_id = args
	else:
		# invalid, not a tag
		pass
	print("<-- " + level + "|" + tag + "|" + valid + "|" + args)

print("Individuals:")
for id in sorted(individuals.iterkeys()):
    print("IndivID: " + id + " Name: " + individuals[id]['NAME'])

print("\nFamilies:")
for id in sorted(families.iterkeys()):
	hubbyname = individuals[families[id]['HUSB']]['NAME']
	wifeyname = individuals[families[id]['WIFE']]['NAME']
	print("FamilyID: " + id + " Husband: " + hubbyname + " Wife: " + wifeyname)
