import sublime, sublime_plugin, os, threading

class NetlinxLaunchDiagnostics(sublime_plugin.TextCommand):
    exe = 'NLDiagsPgm.exe'
    
    def run(self, edit):
        # Check for 64-bit O/S path.
        path = "C:\\Program Files (x86)\\AMX Control Disc\\NetLinx Diagnostics"
        exe_exists = os.path.isfile(path + "\\" + self.exe)
        
        if exe_exists == False:
            path = "C:\\Program Files\\AMX Control Disc\\NetLinx Diagnostics"
            exe_exists = os.path.isfile(path + "\\" + self.exe)
        
        if exe_exists:
            t = threading.Thread(target = self.launch, args = [path])
            t.start()
        else:
            print("Could not find the NetLinx Diagnostics executable.")
    
    def launch(self, path):
        from subprocess import call
        call(path + "\\" + self.exe)