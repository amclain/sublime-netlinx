import sublime, sublime_plugin

class FixNetlinxIndentation(sublime_plugin.TextCommand):
	def run(self, edit):
		old_tab_size = self.view.settings().get("tab_size", 4)
		self.view.settings().set("tab_size", 8)
		self.view.run_command("expand_tabs")
		self.view.settings().set("tab_size", old_tab_size)
