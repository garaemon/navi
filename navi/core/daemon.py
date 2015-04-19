# navi.core.daemon

from plugin import PluginManager

class NaviDaemon:
    """
    Application class for daemon process of navi
    """
    def __init__(self):
        self.plugin_manager = PluginManager()
        self.plugin_manager.loadBasePlugins()
    def run(self):
        print "Hello, World!"

def main():
    daemon = NaviDaemon()
    daemon.run()


