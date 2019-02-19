# Jordan Tantuico, David Kim, Philip Cho
# I pledge my honor that I have abided by the Stevens Honor System

# Individuals (ids, name) in order of id
# Families (ids, hubby, wifey) in order of id

import sys 
from us03birthBeforeDeath import birthBeforeDeath
from us21correctGenderRoles import correctGenderRoles
from us16maleLastNames import maleLastName
from us29listDeceased import listDeceased

# Stores the file, assumes there is a command line argument with the file name
gedcomFile = open(sys.argv[1])

# Stores all the valid tags at their corresponding levels
tags = {'0': ['HEAD', 'TRLR', 'NOTE'],
		'1': ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'],
		'2': ['DATE']}
specialTags = {'0': ['INDI', 'FAM']}

# Dictionary of Individuals
individuals = {}
# Dictionary of Families
# Structure of families: { fid: {HUSB: hid, WIFE: wid, CHIL: [cid1,cid2,...],
# MARR: '1 FEB 2019', DIV: '3 FEB 2019'}, ...}
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
			if tag == 'CHIL':
				if 'CHIL' in families[current_id]:
					families[current_id][tag].append(args)
				else:
					families[current_id][tag] = [args]
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
for id in sorted(individuals.keys()):
    print("IndivID: " + id + " Name: " + individuals[id]['NAME'])

print("\nFamilies:")
for id in sorted(families.keys()):
	hubbyname = individuals[families[id]['HUSB']]['NAME']
	wifeyname = individuals[families[id]['WIFE']]['NAME']
	print("FamilyID: " + id + " Husband: " + hubbyname + " Wife: " + wifeyname)

print()
# Checks US03 on all individuals (birth before death), assumes person has BIRT
# tag, otherwise will print an error message
for id in individuals:
	if not birthBeforeDeath(individuals[id]):
		# Check out these fancy f-strings, ohoho
		print("Error US03: Birth date of {individuals[id]['NAME']}({id}) occurs after his death date.")

# Checks US21 on all families (correct gender roles), assume marriage partners
# exist
for id in families:
	husbandId = families[id]['HUSB']
	wifeId = families[id]['WIFE']
	roles = correctGenderRoles(families[id],individuals)
	# Prints error for husband
	if not roles[0]:
		print("Error US21: Gender role of husband {individuals[husbandId]['NAME']} ({husbandId}) of family {id} is female, instead of male.")
	# Prints error for wife
	if not roles[1]:
		print("Error US21: Gender role of wife {individuals[wifeId]['NAME']} ({wifeId}) of family {id} is male, instead of female.")

for id in families:
	if not maleLastName(families[id],individuals):
		husb = False
		chil = []
		if 'HUSB' in families[id]:
			husb = True
		if 'CHIL' in families[id]:
			for cid in families[id]['CHIL']:
				chil.append(cid)
		print("Anomaly US16: Family " + id + " contains males with different last names:")
		if husb:
			print("HUSBAND: " + individuals[families[id]['HUSB']]['NAME'] + " (" + families[id]['HUSB']+ ")")
		for cid in chil:
			print("CHILD: " + individuals[cid]['NAME']+ " (" + cid+ ")")
print()
print("List of Deceased (US29):")
for id in listDeceased(individuals):
	print(individuals[id]['NAME'] + " (" + id+ ")")
