from google.appengine.ext import ndb

class Note(ndb.Model):
	title = ndb.StringProperty()
	content = ndb.TextProperty(required = True)
	date_created = ndb.DateTimeProperty(auto_now_add=True)
	checklist_items = ndb.KeyProperty("CheckListItem", repeated=True)	
	
	def owner_query(cls, parent_key):
		return cls.query(ancestor=parent_key).order(
			-cls.date_created)

class CheckListItem(ndb.Model):
	title = ndb.StringProperty()
	checked = ndb.BooleanProperty(default=False)

