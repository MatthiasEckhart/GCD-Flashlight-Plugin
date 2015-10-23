from fractions import gcd

def results(fields, original_query):
	message = fields['message']
	numbers = message.split()
	if len(numbers) != 2:
		return {
			"title": "Please specify 'a' and 'b'.",
			"run_args": [message]
		}
	try:
		a = int(numbers[0])
		b = int(numbers[1])
		result = gcd(a, b)
		return {
			"title": "Greatest Common Divisor of {0} and {1} is {2}.".format(numbers[0], numbers[1], result),
			"run_args": [message]
		}
	except ValueError:
		return {
			"title": "Could not calculate Greatest Common Divisor. Wrong types.",
			"run_args": [message]
		}