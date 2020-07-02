def editObject(original, newData):
	for field in newData:
		fieldname = field.name
		original.fieldname = field.value

	original.save()