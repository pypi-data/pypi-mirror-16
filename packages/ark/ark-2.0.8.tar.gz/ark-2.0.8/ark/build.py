# --------------------------------------------------------------------------
# Handles the site building process.
# --------------------------------------------------------------------------

import os

from . import site
from . import utils
from . import pages
from . import records
from . import hooks
from . import loader


# Builds the site.
#
#   1. Copies the site and theme resource files to the output directory.
#   2. Builds the individual record pages.
#   3. Builds the directory index pages.
#
def build_site():

    # Fire the 'init_build' event.
    hooks.event('init_build')

    # Copy the site's resource files to the output directory, i.e. any files
    # in the site's src directory not inside a [type] directory.
    utils.copydir(site.src(), site.out(), skiptypes=True)

    # Copy the theme's resource files to the output directory.
    for name in ('assets', 'resources'):
        if os.path.exists(site.theme(name)):
            utils.copydir(site.theme(name), site.out())

    # Build the individual record pages and directory indexes.
    for path, name in utils.subdirs(site.src()):
        if name.startswith('['):
            build_record_pages(path)
            if site.types(name.strip('[]'), 'indexed'):
                build_directory_indexes(path)

    # Fire the 'exit_build' event.
    hooks.event('exit_build')


# Creates a HTML page for each record file in the source directory.
def build_record_pages(dirpath):

    for fileinfo in loader.srcfiles(dirpath):
        record = records.record(fileinfo.path)
        page = pages.RecordPage(record)
        page.render()

    for dirinfo in utils.subdirs(dirpath):
        build_record_pages(dirinfo.path)


# Creates a paged index for each directory of records.
def build_directory_indexes(dirpath, recursing=False):

    # Determine the record type from the directory path.
    rectype = site.type_from_src(dirpath)

    # Fetch the type's configuration data.
    typedata = site.types(rectype)

    # Assemble a list of records in this directory and any subdirectories.
    reclist = []

    # Process subdirectories first.
    for dirinfo in utils.subdirs(dirpath):
        reclist.extend(build_directory_indexes(dirinfo.path, True))

    # Add any records in this directory to the index.
    for fileinfo in loader.srcfiles(dirpath):
        record = records.record(fileinfo.path)
        if typedata['order_by'] in record:
            reclist.append(record)

    # Are we displaying this index on the homepage?
    if typedata['homepage'] and not recursing:
        slugs = []
    else:
        slugs = site.slugs_from_src(dirpath)

    # Create and render the set of index pages.
    index = pages.Index(rectype, slugs, reclist, typedata['per_index'])
    index['is_dir_index'] = True
    index['srcdir'] = dirpath
    index.render()

    return reclist
