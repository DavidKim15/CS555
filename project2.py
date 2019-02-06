# Jordan Tantuico
# I pledge my honor that I have abided by the Stevens Honor System

# Stores the file
gedcomFile = open("proj02test.ged")

# Stores all the valid tags at their corresponding levels
tags = {'0': ['HEAD', 'TRLR', 'NOTE'],
		'1': ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'],
		'2': ['DATE']}

specialTags = {'0': ['INDI', 'FAM']}
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
	elif components[0] in specialTags and components[2] in specialTags[components[0]]:
		# valid, tag is third component
		valid = "Y"
		tag = components[2]
		args = components[1]
	else:
		# invalid, not a tag
		pass

	print("<-- " + level + "|" + tag + "|" + valid + "|" + args)





	# if components[0] in tags and components[1] in tags[components[0]] or (len(components) == 3 and components[2] in tags[components[0]]):
	# 	valid = "Y"
	# if len(components) == 3:
	# 	# Special case
	# 	if components[0] in tags and components[2] in tags[components[0]]:
	# 		print("<-- " + components[0] + "|" + components[2] + "|" + valid + "|" + components[1])
	# 	# General case
	# 	else:
	# 		print("<-- " + components[0] + "|" + components[1] + "|" + valid + "|" + components[2])
	# else:
	# 	print("<-- " + components[0] + "|" + components[1] + "|" + valid + "|")