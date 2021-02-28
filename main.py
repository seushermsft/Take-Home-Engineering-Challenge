import sys
from importlib import import_module


def main(argv):
    target = argv[1]
    params = dict(arg.split('=')[:2] for arg in argv[2:])
    run_calls = []

    submodule = import_module('nytransport.{}'.format(target))

    run_calls.append(submodule.run)

    for run_call in run_calls:
        run_call(**params)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)
