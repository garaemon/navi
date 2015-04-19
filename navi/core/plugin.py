# navi.core.plugin
from log import LoggingObject

class PluginManager(LoggingObject):
    """
    """
    def __init__(self):
        super(PluginManager, self).__init__()
        
    def loadBasePlugins(self):
        self.logger.debug("Loading basic plugins")
    def instantiatePlugin(klass, name, remapping):
        
