
from rosdistro_tools import verbs
from pkgutil import iter_modules
import sys

def load_available_verbs():
    available_verbs = {}
    for importer, modname, ispkg in iter_modules(verbs.__path__):
        available_verbs[modname] = importer.find_module(modname).load_module(modname)
    return available_verbs

def main():
    available_verbs = load_available_verbs()
    if len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print "Verb help: rosdistro [verb] --help"
        print "Available verbs:"
        for verb_name in available_verbs.keys():
            print "%10s  %s" % (verb_name, available_verbs[verb_name].argument_parser.description)
        print
        exit(0)

    verb_name = sys.argv[1]
    verb_args = sys.argv[2:]

    verb_options = available_verbs[verb_name].argument_parser.parse_args(verb_args)
    available_verbs[verb_name].main(verb_options)
