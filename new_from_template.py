import sublime, sublime_plugin, os

class NetlinxTemplate:
    def load_template(self, edit, filename):
        # Read in the template.
        f = open(os.path.join(os.path.dirname(__file__), 'templates', filename))
        content = f.read()
        f.close()
        
        # Fill a view (tab) with the template text.
        # Will fill the current view if it's empty, otherwise a new view
        # is created. This is to support right clicking the side bar to
        # create a new file in a specific folder.
        v = self.view.window().new_file() if self.view.size() > 0 else self.view
        
        v.insert(edit, 0, content)
        v.set_syntax_file('Packages/NetLinx/NetLinx.tmLanguage')

# NetLinx Standard Template
class NetlinxNewFromTemplateStandard(sublime_plugin.TextCommand, NetlinxTemplate):
    def run(self, edit):
        self.load_template(edit, 'Netlinx Standard.axs')
        
# NetLinx Test Suite Template
class NetlinxNewFromTemplateTestSuite(sublime_plugin.TextCommand, NetlinxTemplate):
    def run(self, edit):
        self.load_template(edit, 'Netlinx Test Suite.axs')

# NetLinx Include (.axi) Template
class NetlinxNewFromTemplateInclude(sublime_plugin.TextCommand, NetlinxTemplate):
    def run(self, edit):
        self.load_template(edit, 'Netlinx Include.axs')

# NetLinx Overview Template
class NetlinxNewFromTemplateOverview(sublime_plugin.TextCommand, NetlinxTemplate):
    def run(self, edit):
        self.load_template(edit, 'Netlinx Overview.axs')