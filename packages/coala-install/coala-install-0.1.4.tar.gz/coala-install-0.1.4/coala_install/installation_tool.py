import argparse
import importlib
import re
import subprocess
import sys

from coala_utils.string_processing.StringConverter import StringConverter
from coala_utils.Question import ask_question
from coalib.collecting.Collectors import get_all_bears_names
from coalib.collecting.Importers import iimport_objects
from coalib.misc.Shell import call_without_output
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from pygments.lexers import SqlLexer
from pyprint.ConsolePrinter import ConsolePrinter


def install_pip_package(package_name):
    """
    Uses ``call`` to install a PyPi package.

    :param package_name: The package to be installed.
    """
    call_without_output([sys.executable, '-m',
                         'pip', 'install', package_name, '--upgrade'])


def get_output(command):
    r"""
    Runs the command and decodes the output and returns it.

    >>> get_output(['echo', '-n', 'word'])
    'word'

    :param command: The command to be run.
    :return:        The output of the command, decoded.
    """
    function = subprocess.Popen(command, stdout=subprocess.PIPE)
    result, *_ = function.communicate()
    return result.decode("utf-8")


def install_requirements(package_name):
    """
    Imports a package and tries installing its requirements.

    :param package_name:        The package to be imported.
    :param package_failed_list: The list with the packages which their
                                requirements failed installing.
    :return:                    A list with the packages which had their
                                requirements failing to be installed.
    """
    package_failed_list = []
    package_object = importlib.import_module(
        'coala' + package_name + '.' + package_name)
    for requirement in getattr(package_object, package_name).REQUIREMENTS:
        try:
            print('The following dependency is installing.. '
                  + str(requirement.package))
            if call_without_output(requirement.install_command()):
                print('The following dependency failed installing: '
                      + str(requirement.package))
                package_failed_list.append(package_name)
            else:
                print('The following dependency was successfully installed: '
                      + str(requirement.package))
        except OSError:
            package_failed_list.append(package_name)
    return package_failed_list


def get_all_bears_names_from_PyPI():
    """
    Gets all the bears names from PyPI, using the link in the description.

    >>> 'PEP8Bear' in get_all_bears_names_from_PyPI()
    True

    :return: A list with all the bear names.
    """
    output = get_output([sys.executable, '-m', 'pip', 'search',
                         "coala.rtfd.org"])
    return re.findall(r"'(\w+)'", output)


def install_bears(bear_names_list, ignore_deps):
    """
    Tries to install each bear from the ``bear_names_list``. Will also check for
    bears which failed to be installed, or their requirements failed to be
    installed.

    :param bear_names_list: The list which contains the names of the bears.
    :param ignore_deps:     An arg which is given to ignore the bears'
                            dependencies.
    """
    bears_failed_list = []
    for bear_name in bear_names_list:
        print('The following bear is installing.. ' + bear_name)
        if not install_pip_package(bear_name):
            print('The following bear has been successfully installed: '
                  + bear_name)
            if not ignore_deps:
                bears_failed_list += install_requirements(bear_name)
        else:
            print('The following bear failed installing: '
                  + str(requirement.package))
            bears_failed_list.append(bear_name)

    return bears_failed_list


def create_arg_parser():
    """
    Creates a parser for command line arguments.

    :return: Parser arguments.
    """
    parser = argparse.ArgumentParser(
        description='Install bears requirements.')
    parser.add_argument('-i', '--ignore',
                        help='Ignore the requirements',
                        action='store_true')
    return parser


def main():
    args = create_arg_parser().parse_args()

    option_completer = WordCompleter(['All', 'Some', 'None'], ignore_case=True)

    # HACK using SqlLexer to color the words which are correct
    # taken from
    # https://github.com/jonathanslenders/python-prompt-toolkit/tree/master/examples/tutorial
    answer = prompt('What bears would you like to install?\n'
                    'All / Some / None\n',
                    lexer=SqlLexer, completer=option_completer).lower()

    if answer == "all":
        print('Great idea, we are installing all the bears right now.')

        install_bears(sorted(get_all_bears_names_from_PyPI()), args.ignore)
        return 0

    elif answer == "some":
        print('This is a list of all the bears you can install:')

        bear_names_list = get_all_bears_names_from_PyPI()
        bear_name_completer = WordCompleter(
            bear_names_list, ignore_case=True)

        for bear_name in sorted(bear_names_list):
            print(bear_name)

        answer = prompt('Which ones? (You can add more, separated by commas)\n',
                        lexer=SqlLexer,
                        completer=bear_name_completer)

        answer = list(StringConverter(answer))

        invalid_answers = set(bear for bear in set(
                                answer) if bear not in bear_names_list)
        valid_answers = set(answer) - invalid_answers

        bears_failed_list = install_bears(valid_answers, args.ignore)

        if bears_failed_list:
            print('Bears that failed installing:\n' + "\n".join(
                bears_failed_list), file=sys.stderr)

        if invalid_answers:
            print('The following inputs were not part of the bears list and '
                  'were therefore not installed:\n'
                  + "\n".join(invalid_answers))
        return 0

    else:
        print('See ya!')
        return 0


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main())
