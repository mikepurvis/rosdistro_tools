
import argparse

argument_parser = argparse.ArgumentParser(prog="rosdistro %s" % __name__,
        description="Freeze devel branches in a rosdistro.")

argument_parser.add_argument('--release-tag', dest='release_tag', action='store_true',
                             help='Transform all source/doc branch references to the upstream tags.')
argument_parser.add_argument('--source-commit', dest='source_commit', action='store_true',
                             help='Transform all source/doc branch references to the current hash.')

def main(options):
    if not options.release_tag and not options.source_commit:
        print "Must specify one of --release-tag or --source-commit."


