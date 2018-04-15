def is_negated(x):
	return x & 1

def literal_to_variable(x):
	return x >> 1

def negate(x):
	return x ^ 1

def variable_to_literal(x, negated=False):
    negated = int(negated)	
    return (x << 1) | negated

