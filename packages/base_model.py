from tortoise import Model

class BaseModel(Model):
	class Meta:
		abstract = True
  
	def to_dict(self, exclude: set = None) -> dict:
		exclude = exclude or set()
		return {
			field: getattr(self, field)
			for field in self._meta.fields_map.keys()
			if field not in exclude
		}
      