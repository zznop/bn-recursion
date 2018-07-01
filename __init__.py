from binaryninja import *
from .recursion import *

def find_recursion(view):
    rec_search = RecursionSearch(view)
    rec_search.start()

PluginCommand.register(
    "Find recursive logic",
    "Search for direct and indirect recursion",
    find_recursion
)
