from Config.Controller.CoreController import *
from Config.Controller.PluginController import *
from Config.View.Core.MasterView import MakeCoreView
from Config.View.Plugin.MasterView import MakePluginsView

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONFIG_FILE_NAME = 'config.json'


def scaffold_initial_files():
    CoreController(BASE_DIR, CONFIG_FILE_NAME)
    PluginsController(BASE_DIR, CONFIG_FILE_NAME)


def call_plugins_config(event):
    MakePluginsView(BASE_DIR, CONFIG_FILE_NAME)


def call_core_config(event):
    MakeCoreView(BASE_DIR, CONFIG_FILE_NAME)


if __name__ == "__main__":
    print "entered"
