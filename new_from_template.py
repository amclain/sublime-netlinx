import sublime, sublime_plugin, os

# NetLinx Standard Template
class NetlinxNewFromTemplateStandard(sublime_plugin.TextCommand):
    def run(self, edit):
        template_name = 'Netlinx Standard.axs'
        
        # Read in the template.
        f = open(os.path.join(os.path.dirname(__file__), 'templates', template_name))
        content = f.read()
        f.close()
        
        # Create a new view (tab) and fill it with the template text.
        v = self.view.window().new_file()
        v.insert(edit, 0, content)
        v.set_syntax_file('Packages/NetLinx/NetLinx.tmLanguage')

# NetLinx Test Suite Template
class NetlinxNewFromTemplateTestSuite(sublime_plugin.TextCommand):
    def run(self, edit):
        template_name = 'Netlinx Test Suite.axs'
        
        # Read in the template.
        f = open(os.path.join(os.path.dirname(__file__), 'templates', template_name))
        content = f.read()
        f.close()
        
        # Create a new view (tab) and fill it with the template text.
        v = self.view.window().new_file()
        v.insert(edit, 0, content)
        v.set_syntax_file('Packages/NetLinx/NetLinx.tmLanguage')
