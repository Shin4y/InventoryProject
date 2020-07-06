from django import template

register = template.Library()

def getDictItems(value): #returns the dict item for iterating through values for showing inventory values in displayAll
	return value.__dict__.items()


register.filter('getDictItems', getDictItems)