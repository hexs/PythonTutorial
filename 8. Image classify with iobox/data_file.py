import configparser
from typing import Union

BLACK = '\033[90m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
ENDC = '\033[0m'
BOLD = '\033[1m'
ITALICIZED = '\033[3m'
UNDERLINE = '\033[4m'


def ini_str_to_python_variable(string: str) -> Union[str, int, float, list, dict, tuple, set]:
    try:
        return eval(string)
    except Exception as e:
        return string


def ini_str_to_python_variable_and_print(string: str):
    try:
        re_turn = eval(string)
        return f'{re_turn} {CYAN}{type(re_turn)}{ENDC}'
    except Exception as e:
        return YELLOW + string + ENDC


def ini_to_dict(filename, show=None):
    config = configparser.ConfigParser()
    config.read(filename)
    ini_dict = {}
    for section in config.sections():
        section_dict = {}
        for option in config.options(section):
            section_dict[option] = ini_str_to_python_variable(config.get(section, option))
        ini_dict[section] = section_dict
    if show:
        ini_dict_for_print = {}
        for section in config.sections():
            section_dict = {}
            for option in config.options(section):
                section_dict[option] = ini_str_to_python_variable_and_print(config.get(section, option))
            ini_dict_for_print[section] = section_dict
        for k, v in ini_dict_for_print.items():
            print(f'{k}')
            key_len = 0
            for kk in v.keys():
                if key_len < len(kk):
                    key_len = len(kk)
            for kk, vv in v.items():
                print(f'    {kk:{key_len}}, {vv}')
    return ini_dict


if __name__ == '__main__':
    d = ini_to_dict('model_position.ini', True)
