def lookup(d, key):
    '''
    This function finds a match in dictionary and returns the value.
    :param d: dictionary data type
    :param key: key for the dictionary
    :return: value found in the dictionary
    '''
    found = False
    for child in d:
        if found: return child.text
        if child.tag == "key" and child.text == key:
            found = True
    return None
