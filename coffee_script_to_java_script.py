import sublime, sublime_plugin

class CoffeeScriptToJavaScript(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().run_command('exec', {'cmd': ["coffee", "-c", self.view.file_name()]})
