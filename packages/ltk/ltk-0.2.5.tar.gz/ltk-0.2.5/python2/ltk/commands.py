import click
import sys
python_version = sys.version
# Python 3
# # if python_version[0] < '3':
# #    print('Python 3 is required to run this version of the Lingotek Filesystem connector.\n\nFor other versions and troubleshooting, see: https://github.com/lingotek/filesystem-connector')
# #    exit()
from ltk import actions
import os
from ltk.exceptions import UninitializedError, ResourceNotFound, RequestFailedError, AlreadyExistsError
from ltk.constants import LOG_FN, CONF_DIR
import logging
from ltk.logger import logger, API_LOG_LEVEL, API_RESPONSE_LOG_LEVEL, CustomFormatter

from ltk import __version__
from ltk.watch import WatchAction
from ltk.import_action import ImportAction


def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


def init_logger(path):
    """
    Initializes logger based on path
    """
    logger.setLevel(logging.DEBUG)
    if not path:
        file_handler = logging.FileHandler(LOG_FN)
    else:
        try:
            file_handler = logging.FileHandler(os.path.join(path, CONF_DIR, LOG_FN))
        except IOError:
            # todo error check when running init without existing conf dir
            os.mkdir(os.path.join(path, CONF_DIR))
            file_handler = logging.FileHandler(os.path.join(path, CONF_DIR, LOG_FN))
    console_handler = logging.StreamHandler(sys.stdout)
    file_handler.setLevel(API_LOG_LEVEL)
    file_handler.setFormatter(logging.Formatter('%(asctime)s  %(levelname)s: %(message)s'))
    if quiet:
        console_handler.setLevel(logging.WARNING)
    elif verbosity:
        if verbosity > 1:
            console_handler.setLevel(API_RESPONSE_LOG_LEVEL)
        else:
            console_handler.setLevel(API_LOG_LEVEL)
    else:
        console_handler.setLevel(logging.INFO)
    custom_formatter = CustomFormatter()
    console_handler.setFormatter(custom_formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def print_log(error):
    """
    Prints the error before logger is initialized
    """
    if not len(logger.handlers):
        print ('Error: {0}'.format(error))
        sys.exit()
    return


@click.group()
# Python 2
@click.version_option(version=__version__, message='%(prog)s version %(version)s (Lingotek Filesystem Connector - Python 2)')
# Python 3
# @click.version_option(version=__version__, message='%(prog)s version %(version)s (Lingotek Filesystem Connector - Python 3)')
@click.option('-q', 'is_quiet', flag_value=True, help='Will only show warnings')
@click.option('-v', 'verbosity_lvl', count=True, help='Show API calls. Use -vv for API responses.')
def ltk(is_quiet, verbosity_lvl):
    global quiet, verbosity
    quiet = is_quiet
    verbosity = verbosity_lvl


@ltk.command()
@click.option('--access_token', help='Your access token')
@click.option('--host', type=click.Choice(['myaccount.lingotek.com', 'cms.lingotek.com']), default='myaccount.lingotek.com',
              help='Environment: myaccount for production, cms for sandbox; the default is production')
# @click.option('--host', help='host')
@click.option('--path', type=click.Path(exists=True),
              help='The path to the project directory to be initialized; defaults to the current directory')
@click.option('-n', '--project_name', help='The preferred project name, defaults to the current directory name')
@click.option('-w', '--workflow_id', default='c675bd20-0688-11e2-892e-0800200c9a66',
              help='The id of the workflow to use for this project; defaults to machine translate only.')
@click.option('-l', '--locale', default='en_US', help='The default source locale for the project; defaults to en_US')
@click.option('-d', '--delete', flag_value=True,  # expose_value=False, callback=abort_if_false,
              # prompt='Are you sure you want to delete the current project remotely and re-initialize? '
              #        'Use the -c flag if you only want to change the project.',
              help='Delete the current project remotely and re-initialize')
# todo add a 'change' option so don't delete remote project
# @click.option('-c', '--change', flag_value=True, help='Change the Lingotek project. ')
@click.option('--reset', flag_value=True, help='Reauthorize and reset any stored access tokens')
def init(host, access_token, path, project_name, workflow_id, locale, delete, reset):
    """ Connects a local project to Lingotek """
    try:
        host = 'https://' + host
        if not path:
            path = os.getcwd()
        if not project_name:
            project_name = os.path.basename(os.path.normpath(path))
        init_logger(path)
        actions.init_action(host, access_token, path, project_name, workflow_id, locale, delete, reset)
    except (ResourceNotFound, RequestFailedError) as e:
        print_log(e)
        logger.error(e)
        return


@ltk.command()
#TO-DO: @click.option('-a', '--all', help='List all configuration settings (including access token)')
@click.option('-l', '--locale', help='Change the default source locale for the project')
@click.option('-w', '--workflow_id', help='Change the default workflow id for the project')
@click.option('-d', '--download_folder',
              help='Specify a folder for where downloaded translations should go. Enter -d --default, or -d --same, or leave blank for target translations to be downloaded to the same folder as their corresponding source files.')
@click.option('-f', '--watch_folder',
              help='Specify a folder to watch when running ltk watch. Enter -f --default or leave blank to only watch files explicitly added to the project.')
@click.option('-t', '--target_locales', multiple=True,
              help='Specify target locales that documents in watch_folder should be assigned; may either specify '
                   'with multiple -t flags (ex: -t locale -t locale) or give a list separated by commas and no spaces '
                   '(ex: -t locale,locale)')
def config(locale, workflow_id, download_folder, watch_folder, target_locales):
    """ View or change local configuration """
    try:
        action = actions.Action(os.getcwd())
        init_logger(action.path)
        action.config_action(locale, workflow_id, download_folder, watch_folder, target_locales)
    except (UninitializedError, RequestFailedError) as e:
        print_log(e)
        logger.error(e)
        return


@ltk.command(short_help="Adds content; could be one or more files specified by the Unix shell pattern")
@click.argument('file_names', required=True, nargs=-1)
@click.option('-l', '--locale', help='If source locale is different from the default configuration. Use ltk list -l to see possible locales')
@click.option('-f', '--format',
              help="Format of file; if not specified, will use extension to detect; defaults to plaintext. Use ltk list -f to see possible formats. Files may not be added to Lingotek's system if not formatted correctly according to the specified format")
@click.option('-s', '--srx', type=click.Path(exists=True), help='srx file')
@click.option('-si', '--srx_id', help='srx id')
@click.option('-i', '--its', type=click.Path(exists=True), help='its file')
@click.option('-ii', '--its_id', help='its id')
@click.option('-c', '--charset', help='File encoding')
@click.option('-ff', '--fprm', type=click.Path(exists=True), help='fprm file')
@click.option('-fi', '--fprm_id', help='fprm id')
@click.option('-fs', '--fprm_subfilter', type=click.Path(exists=True), help='fprm subfilter file')
@click.option('-fsi', '--fprm_subfilter_id', help='fprm subfilter id')
@click.option('-v', '--vault_id', help='Save-to TM vault id')
@click.option('-e', '--external_url', help='Source url')
@click.option('-o', '--overwrite', flag_value=True, help='Overwrite previously added file if the file has been modified')
def add(file_names, **kwargs):
    """ Adds content. Could be one or more files specified by a Unix shell pattern """
    try:
        action = actions.Action(os.getcwd())
        init_logger(action.path)
        action.add_action(file_names, **kwargs)
    except (UninitializedError, RequestFailedError, ResourceNotFound, AlreadyExistsError) as e:
        print_log(e)
        logger.error(e)
        return


@ltk.command(short_help="Sends updated content to Lingotek for documents that have been added")
def push():
    """ Sends updated content to Lingotek for documents that have been added """
    try:
        action = actions.Action(os.getcwd())
        init_logger(action.path)
        action.push_action()
    except UninitializedError as e:
        print_log(e)
        logger.error(e)
        return


@ltk.command(short_help="Add targets to document(s) to start translation; defaults to the entire project. Use ltk list -l to see possible locales")
@click.option('-n', '--doc_name', help='The name of the document; specify for one document')
@click.option('-p', '--path', type=click.Path(exists=True), help='A file name or directory for which to request targets')
@click.option('-d', '--delete', 'to_delete', flag_value=True, help='Deletes a specified target locale')
@click.option('--due_date', help='The due date of the translation')
@click.option('-w', '--workflow', help='The workflow of the translation (do "ltk list -w" to see available workflows)')
@click.argument('locales', required=True, nargs=-1)  # can have unlimited number of locales
def request(doc_name, path, locales, to_delete, due_date, workflow):
    """ Add targets to document(s) to start translation; defaults to the entire project. Use ltk list -l to see possible locales """
    try:
        action = actions.Action(os.getcwd())
        init_logger(action.path)
        if isinstance(locales,str):
            locales = [locales]
        action.target_action(doc_name, path, locales, to_delete, due_date, workflow)
    except (UninitializedError, ResourceNotFound, RequestFailedError) as e:
        print_log(e)
        logger.error(e)
        return


# todo add a --all option to see all document ids once only show relative to cwd is implemented
@ltk.command(name='list', short_help='Shows docs, workflows, locales, formats, or filters')
@click.option('-d', '--documents', 'id_type', flag_value='document', help='List added documents')
@click.option('-p', '--path', 'path', flag_value=True, help='List file paths of documents instead of titles')
@click.option('-w', '--workflows', 'id_type', flag_value='workflow', help='List available workflows')
@click.option('-l', '--locales', 'id_type', flag_value='locale', help='List supported locale codes')
@click.option('-f', '--formats', 'id_type', flag_value='format', help='List supported formats')
@click.option('-r', '--remote', 'id_type', flag_value='remote', help='List all project documents on Lingotek Cloud')
@click.option('--filters', 'id_type', flag_value='filter', help='List default and custom filters')
def list_ids(id_type, path):
    """ Shows docs, workflows, locales, formats, or filters """
    try:
        action = actions.Action(os.getcwd())
        init_logger(action.path)
        if id_type == 'workflow':
            action.list_workflow_action()
        elif id_type == 'locale':
            action.list_locale_action()
        elif id_type == 'format':
            action.list_format_action()
        elif id_type == 'filter':
            action.list_filter_action()
        elif id_type == 'remote':
            action.list_remote_action()
        else:
            action.list_ids_action(path)

    except (UninitializedError, RequestFailedError) as e:
        print_log(e)
        logger.error(e)
        return


@ltk.command(short_help="Gets the status of a specific document or all documents")
@click.option('-n', '--doc_name', help='Specific document name to get status of')
@click.option('-d', '--detailed', flag_value=True, help='Detailed status of each locale for the document')
@click.option('-a', '--all', flag_value=True, help='List all project documents on Lingotek Cloud')
def status(**kwargs):
    """ Gets the status of a specific document or all documents """
    try:
        action = actions.Action(os.getcwd())
        init_logger(action.path)
        action.status_action(**kwargs)
    except (UninitializedError, ResourceNotFound) as e:
        print_log(e)
        logger.error(e)
        return


@ltk.command(short_help='Download specified translations')
@click.option('-a', '--auto_format', flag_value=True, help='Flag to auto apply formatting during download')
@click.argument('locales', required=True, nargs=1)
@click.argument('file_names', type=click.Path(exists=True), required=True, nargs=-1)
def download(auto_format, locales, file_names):
    """ Downloads translated content specified by filename for specified locales. For multiple locales give a list separated by commas and no spaces
    (ex: en_US,en_GB)"""
    try:
        action = actions.Action(os.getcwd())
        init_logger(action.path)
        for name in file_names:
            action.download_by_path(name, locales, auto_format)
    except (UninitializedError, ResourceNotFound, RequestFailedError) as e:
        print_log(e)
        logger.error(e)
        return


@ltk.command()
@click.option('-a', '--auto_format', flag_value=True, help='Flag to auto apply formatting during download')
@click.argument('locales', nargs=-1)
def pull(auto_format, locales):
    """ Pulls translations for all added documents for all locales or by specified locales """
    try:
        action = actions.Action(os.getcwd())
        init_logger(action.path)
        if locales:
            for locale in locales:
                action.pull_action(locale, auto_format)
        else:
            action.pull_action(None, auto_format)
    except UninitializedError as e:
        print_log(e)
        logger.error(e)
        return


@ltk.command(short_help="Disassociates local doc(s) from Lingotek Cloud and deletes the remote copy")
@click.argument('file_names', required=False, nargs=-1)
@click.option('-i', '--id', flag_value=True, help='Delete documents with the specified ids (instead of file names) on Lingotek Cloud')
@click.option('-n', '--name', flag_value=True, help='Delete documents with the specified names (instead of file names or paths) on Lingotek Cloud')
@click.option('-a', '--all', flag_value=True, help='Delete all documents from Lingotek Cloud that are found locally')
@click.option('-r', '--remote', flag_value=True, help='When used with -a, deletes all documents from Lingotek Cloud for the current project')
@click.option('-f', '--force', flag_value=True, help='Delete both local and remote files')
def rm(file_names, **kwargs):
    """
    Disassociates local doc(s) from Lingotek Cloud and deletes the remote copy.
    If the remote copy should be kept, please use ltk clean.
    """
    try:
        action = actions.Action(os.getcwd())
        init_logger(action.path)
        if not file_names and not ('all' in kwargs and kwargs['all']):
            logger.info("Usage: ltk rm [OPTIONS] FILE_NAMES...")
            return
        action.rm_action(file_names, **kwargs)
    except (UninitializedError, ResourceNotFound, RequestFailedError) as e:
        print_log(e)
        logger.error(e)
        return


@ltk.command(name='import', short_help="Import docs from Lingotek")
@click.option('-a', '--all', 'import_all', flag_value=True, help='Import all documents from Lingotek Cloud')
@click.option('-f', '--force', flag_value=True, help='Overwrites existing documents without prompt')
@click.option('-p', '--path', type=click.Path(exists=True), help='Import documents to a specified path')
def import_command(import_all, force, path):
    """
    Import documents from Lingotek Cloud, by default downloading to the project's root folder
    """
    # todo import should show all documents
    # add a force option so can import all force -- overwrites all existing documents without prompting
    # check if doc id
    # if exist, prompt for overwrite
    # else automatically re-name
    # possibly have to patch title in Lingotek Cloud?
    try:
        # action = actions.Action(os.getcwd())
        action = ImportAction(os.getcwd())
        init_logger(action.path)
        action.import_action(import_all, force, path)
    except(UninitializedError, RequestFailedError) as e:
        print_log(e)
        logger.error(e)
        return


@ltk.command(short_help="Cleans up the associations between local documents and documents in Lingotek")
@click.option('-a', '--all', 'dis_all', flag_value=True, help='Removes all associations between local and remote')
@click.argument('file_paths', required=False, nargs=-1)
@click.option('-f', '--force', flag_value=True, help='Deletes local documents that no longer exists in Lingotek')
def clean(force, dis_all, file_paths):
    """
    Cleans up the associations between local documents and documents in Lingotek.
    By default, checks that local documents and remote documents line up.
    Use different options for different use cases. Enter file or directory names
    to remove local associations of specific files or directories.
    """
    try:
        action = actions.Action(os.getcwd())
        init_logger(action.path)
        action.clean_action(force, dis_all, file_paths)
    except (UninitializedError, RequestFailedError) as e:
        print_log(e)
        logger.error(e)
        return


@ltk.command(short_help="Watches local and remote files")
@click.option('-p', '--path', type=click.Path(exists=True), help='Specify a folder to watch; defaults to project path')
@click.option('--ignore', multiple=True, help='Specify types of files to ignore')
@click.option('--auto', 'delimiter', help='Automatically detects locale from the file name; specify locale delimiter')
@click.option('-t', '--timeout', type=click.INT, default=60,
              help='The amount of time watch will sleep between polls, in seconds. Defaults to 1 minute')
def watch(path, ignore, delimiter, timeout):
    """
    Watches local files added or imported by ltk, and sends a PATCH when a document is changed.
    Also watches remote files, and automatically downloads finished translations.
    """
    try:
        action = WatchAction(os.getcwd(), timeout)
        init_logger(action.path)
        action.watch_action(path, ignore, delimiter)
    except (UninitializedError, RequestFailedError) as e:
        print_log(e)
        logger.error(e)


if __name__ == '__main__':
    ltk()
