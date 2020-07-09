def dontEdit(key):
	if key.name != 'commonobject_ptr' and key.name != 'slug' and key.name != 'token' and key.name != 'lastUpdatedUser' and key.name != 'dateLastModified' and key.name != 'id':
		return False

	return True