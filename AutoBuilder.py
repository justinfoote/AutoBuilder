import sublime
import sublime_plugin
import subprocess
import threading

settings = sublime.load_settings("AutoBuilder.sublime-settings")


class AutoBuilder(sublime_plugin.EventListener):

    def on_post_save(self, view):
        def do():
            commands = settings.get('autobuild_command')
            fileName = view.file_name()
            command = commands.get(fileName[fileName.rfind('.') + 1:])
            if command:
                subprocess.Popen(command, shell = True, 
                        stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
                
        threading.Thread(target = do).start()