# list of deceased people, returns list
# US29
def listDeceased(individuals):
    deceased_list = []
    for id in individuals:
        if 'DEAT' in individuals[id]:
            deceased_list.append(id)
    return deceased_list
