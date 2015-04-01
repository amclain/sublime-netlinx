import sublime, sublime_plugin, os

class NetlinxGenerateWorkspace(sublime_plugin.TextCommand):
    def run(self, edit):
        path = self.view.file_name()
        while os.path.dirname(path) != path:
            path = os.path.dirname(path)
            if os.path.isfile(path + "\\" + "workspace.config.yaml"):
                from subprocess import call
                call(["netlinx-workspace", "-g"], shell = True, cwd = path)
                break
