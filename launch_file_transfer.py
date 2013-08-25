import sublime, sublime_plugin, os, threading

class NetlinxLaunchFileTransfer(sublime_plugin.TextCommand):
    exe = 'FileTransfer2.exe'
    
    def run(self, edit):
        # Check for 64-bit O/S path.
        path = "C:\\Program Files (x86)\\AMX Control Disc\\FileTransfer 2"
        exe_exists = os.path.isfile(path + "\\" + self.exe)
        
        if exe_exists == False:
            path = "C:\\Program Files\\AMX Control Disc\\FileTransfer 2"
            exe_exists = os.path.isfile(path + "\\" + self.exe)
        
        if exe_exists:
            t = threading.Thread(target = self.launch, args = [path])
            t.start()
        else:
            print("Could not find the File Transfer 2 executable.")
    
    def launch(self, path):
        from subprocess import call
        call(path + "\\" + self.exe)