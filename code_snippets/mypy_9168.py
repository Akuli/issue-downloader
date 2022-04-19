if name in ['visible', 'value', 'locked']:
	obj[name] = self.use_var_expr(scope, value)
