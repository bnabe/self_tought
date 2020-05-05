class PubliPrivateExample:
	def __init__(self):
		self.public = "safe"
		self._unsafe = "unsafe"

	def public_method(self):
		pass

	def _unsafe_method(self):
		pass

