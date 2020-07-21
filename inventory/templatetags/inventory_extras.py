from django import template

register = template.Library()

def getDictItems(value): #returns the dict item for iterating through values for showing inventory values in displayAll
	return value.__dict__.items()

def dontEdit(key):
	if key.name != 'commonobject_ptr' and key.name != 'slug' and key.name != 'token' and key.name != 'lastUpdatedUser' and key.name != 'dateLastModified' and key.name != 'id':
		return False

	return True


register.filter('getDictItems', getDictItems)
register.filter('dontEdit', dontEdit)