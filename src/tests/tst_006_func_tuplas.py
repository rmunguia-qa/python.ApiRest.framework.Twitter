import objectpath


def new_compare_entity_values(self, path, expected):
	expected = str(expected)

	try:

		tree_obj = objectpath.Tree(self.json_response)
		entity = tuple(tree_obj.execute('$.' + path))
		path_Value = ''.join(entity)

		print(path_Value)

	except SyntaxError:
		path_Value = str(None)

		print("Función new_compare_entity_values: No se ha podido obtener ningún valor en la búsqueda!")

	if expected == "NOT NULL":
		assert str(path_Value) != None, f"El valor de la entidad es NULL: {path_Value} != {expected}"
		return

	if expected == "NULL":
		assert str(path_Value) == None, f"El valor de la entidad no es NULL: {path_Value} != {expected}"
		return

	assert path_Value == expected, f"El valor no es el esperado {path}: {path_Value} != {expected}"