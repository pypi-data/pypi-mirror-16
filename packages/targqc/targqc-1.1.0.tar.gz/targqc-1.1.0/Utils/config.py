import socket
from contextlib import contextmanager
from os.path import abspath, expanduser, join, dirname, pardir
from traceback import format_exc

from Utils.logger import info, err, critical, debug, warn
from Utils.file_utils import verify_file, verify_module, adjust_path
from Utils.utils import is_uk, is_us, is_cloud, is_sweden, is_ace, is_china, is_local

from yaml import load as load_yaml
try:
    from yaml import CDumper as Dumper, CLoader as Loader
except ImportError:
    from yaml import Dumper, Loader


def load_yaml_config(fpath):
    verify_file(fpath, is_critical=True)
    try:
        dic = load_yaml(open(fpath), Loader=Loader)
    except:
        err(format_exc())
        critical('Could not parse bcbio YAML ' + fpath)
    else:
        return dic


def fill_dict_from_defaults(cur_cnf, defaults_dict):
    for key in defaults_dict:
        if key in cur_cnf:
            if isinstance(cur_cnf[key], dict) and isinstance(defaults_dict[key], dict):
                fill_dict_from_defaults(cur_cnf[key], defaults_dict[key])
        else:
            cur_cnf[key] = defaults_dict[key]
    return cur_cnf


def _join_parent_conf(child_conf, parent_conf):
    bc = parent_conf.copy()
    bc.update(child_conf)
    child_conf.update(bc)
    return child_conf


@contextmanager
def with_cnf(cnf, **kwargs):
    prev_opts = {k: cnf[k] for k in kwargs.keys()}
    try:
        for k, v in kwargs.items():
            cnf[k] = v
        yield cnf
    finally:
        for k, v in prev_opts.items():
            cnf[k] = v
