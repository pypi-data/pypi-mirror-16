import threading
import os
try:
    from collections import OrderedDict
except ImportError:
    from .packages.ordereddict import OrderedDict

from .pgcompleter import PGCompleter
from .pgexecute import PGExecute


class CompletionRefresher(object):

    refreshers = OrderedDict()

    def __init__(self):
        self._completer_thread = None
        self._restart_refresh = threading.Event()

    def refresh(self, executor, special, callbacks, history=None,
      settings=None):
        """
        Creates a PGCompleter object and populates it with the relevant
        completion suggestions in a background thread.

        executor - PGExecute object, used to extract the credentials to connect
                   to the database.
        special - PGSpecial object used for creating a new completion object.
        settings - dict of settings for completer object
        callbacks - A function or a list of functions to call after the thread
                    has completed the refresh. The newly created completion
                    object will be passed in as an argument to each callback.
        """
        if self.is_refreshing():
            self._restart_refresh.set()
            return [(None, None, None, 'Auto-completion refresh restarted.')]
        else:
            self._completer_thread = threading.Thread(
                target=self._bg_refresh,
                args=(executor, special, callbacks, history, settings),
                name='completion_refresh')
            self._completer_thread.setDaemon(True)
            self._completer_thread.start()
            return [(None, None, None,
                     'Auto-completion refresh started in the background.')]

    def is_refreshing(self):
        return self._completer_thread and self._completer_thread.is_alive()

    def _bg_refresh(self, pgexecute, special, callbacks, history=None,
      settings=None):
        completer = PGCompleter(smart_completion=True, pgspecial=special,
            settings=settings)

        # Create a new pgexecute method to popoulate the completions.
        e = pgexecute
        executor = PGExecute(e.dbname, e.user, e.password, e.host, e.port, e.dsn)

        # If callbacks is a single function then push it into a list.
        if callable(callbacks):
            callbacks = [callbacks]

        while 1:
            for refresher in self.refreshers.values():
                refresher(completer, executor)
                if self._restart_refresh.is_set():
                    self._restart_refresh.clear()
                    break
            else:
                # Break out of while loop if the for loop finishes natually
                # without hitting the break statement.
                break

            # Start over the refresh from the beginning if the for loop hit the
            # break statement.
            continue

        # Load history into pgcompleter so it can learn user preferences
        n_recent = 100
        if history:
            for recent in history[-n_recent:]:
                completer.extend_query_history(recent, is_init=True)

        for callback in callbacks:
            callback(completer)


def refresher(name, refreshers=CompletionRefresher.refreshers):
    """Decorator to populate the dictionary of refreshers with the current
    function.
    """
    def wrapper(wrapped):
        refreshers[name] = wrapped
        return wrapped
    return wrapper

@refresher('schemata')
def refresh_schemata(completer, executor):
    completer.set_search_path(executor.search_path())
    completer.extend_schemata(executor.schemata())

@refresher('tables')
def refresh_tables(completer, executor):
    completer.extend_relations(executor.tables(), kind='tables')
    completer.extend_columns(executor.table_columns(), kind='tables')
    completer.extend_foreignkeys(executor.foreignkeys())

@refresher('views')
def refresh_views(completer, executor):
    completer.extend_relations(executor.views(), kind='views')
    completer.extend_columns(executor.view_columns(), kind='views')

@refresher('functions')
def refresh_functions(completer, executor):
    completer.extend_functions(executor.functions())

@refresher('types')
def refresh_types(completer, executor):
    completer.extend_datatypes(executor.datatypes())

@refresher('databases')
def refresh_databases(completer, executor):
    completer.extend_database_names(executor.databases())

@refresher('casing')
def refresh_casing(completer, executor):
    casing_file = completer.casing_file
    if not casing_file:
        return
    generate_casing_file = completer.generate_casing_file
    if generate_casing_file and not os.path.isfile(casing_file):
        casing_prefs = '\n'.join(executor.casing())
        with open(casing_file, 'w') as f:
            f.write(casing_prefs)
    if os.path.isfile(casing_file):
        with open(casing_file, 'r') as f:
            completer.extend_casing([line.strip() for line in f])
