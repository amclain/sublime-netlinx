import sublime, sublime_plugin, os

# NetLinx Standard Template
class NetlinxNewFromTemplateStandard(sublime_plugin.TextCommand, NetlinxTemplate):
    def run(self, edit):
        self.load_template(edit, 'Netlinx Standard.axs')
        
# NetLinx Test Suite Template
class NetlinxNewFromTemplateTestSuite(sublime_plugin.TextCommand, NetlinxTemplate):
    def run(self, edit):
        self.load_template(edit, 'Netlinx Test Suite.axs')

class NetlinxTemplate:
    def load_template(self, edit, filename):
        # Read in the template.
        f = open(os.path.join(os.path.dirname(__file__), 'templates', filename))
        content = f.read()
        f.close()
        
        # Create a new view (tab) and fill it with the template text.
        v = self.view.window().new_file()
        v.insert(edit, 0, content)
        v.set_syntax_file('Packages/NetLinx/NetLinx.tmLanguage')