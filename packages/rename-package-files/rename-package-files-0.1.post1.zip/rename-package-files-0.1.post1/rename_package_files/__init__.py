import fnmatch
import logging

from path_helpers import path
# TODO Remove dependency on `pandas`
import pandas as pd


logger = logging.getLogger(__name__)


def rename_package_files(package_dir, old_name, new_name, exclude=None):
    '''
    Rename all occurrences of ``old_name`` to ``new_name`` in all files in
    package.

    Renaming includes:

     - Filenames
     - Occurrences in file contents

    Note that all ``CamelCase``, ``-``-separated, and ``_``-separated
    occurrences of ``old_name`` are replaced with the respective form of
    ``new_name``.

    Parameters
    ==========
    package_dir
        Root directory of package
    old_name
        Original (``-``-separated) package name
    new_name
        New (``-``-separated) package name
    '''
    if exclude is None:
        exclude = lambda old_name_i: False
    elif not callable(exclude):
        exclude_list = [exclude] if isinstance(exclude, str) else exclude
        exclude = lambda old_name_i: any(fnmatch.fnmatch(old_name_i, exclude_i)
                                         for exclude_i in exclude_list)

    names = pd.Series([old_name, new_name], index=['old', 'new'])
    underscore_names = names.map(lambda v: v.replace('-', '_'))
    camel_names = names.str.split('-').map(lambda x: ''.join([y.title()
                                                              for y in x]))

    # Replace all occurrences of provided original name with new name, and all
    # occurrences where dashes (i.e., '-') are replaced with underscores.
    #
    # Dashes are used in Python package names, but underscores are used in
    # Python module names.
    for p in path(package_dir).walkfiles():
        if exclude(p):
            logger.debug('.. skipping contents rename of %s', p)
            continue
        data = p.bytes()
        if '.git' not in p and (names.old in data or
                                underscore_names.old in data or
                                camel_names.old in data):
            logger.debug('.. rename contents of %s', p)
            p.write_bytes(data.replace(names.old, names.new)
                          .replace(underscore_names.old, underscore_names.new)
                          .replace(camel_names.old, camel_names.new))

    def rename_path(p):
        if '.git' in p:
            return
        if underscore_names.old in p.name:
            p.rename(p.parent.joinpath(p.name.replace(underscore_names.old,
                                                      underscore_names.new)))
        if camel_names.old in p.name:
            p.rename(p.parent.joinpath(p.name.replace(camel_names.old,
                                                      camel_names.new)))

    # Rename all files/directories containing original name with new name, and
    # all occurrences where dashes (i.e., '-') are replaced with underscores.
    #
    # Process list of paths in *reverse order* to avoid renaming parent
    # directories before children.
    for p in sorted(list(path(package_dir).walkdirs()))[-1::-1]:
        rename_path(p)

    for p in path(package_dir).walkfiles():
        if exclude(p):
            logger.debug('.. skipping rename of %s', p)
        else:
            logger.debug('.. rename %s', p)
            rename_path(p)
