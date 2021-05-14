import kivy
from kivymd.app import MDApp 
from kivy.core.window import Window
from kivy.uix.widget import Widget
import sqlite3

# Root widget defined in kv file
class MainWindow(Widget):
	# DB
	conn = sqlite3.connect("namirnice.db")
	c = conn.cursor()
	c.execute("SELECT * FROM namirnice_kiddy_1")
	sve = c.fetchall()	
	conn.commit()	
	conn.close()

	

# Main app inherits from MDApp (kv file must be "main" to see it)
class MainApp(MDApp):
	# here we override the inherited MDApp class -build function, returning the root widget / layout	
	def build(self): 
		# Set the theme
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "DeepPurple"

		

		# Set App size
		Window.size = (324, 720)

		
		
		# Return root widget
		return MainWindow()


if __name__ == "__main__":
	# Instance of MainApp class
	MA = MainApp()
	# MDApp has a run function
	MA.run()