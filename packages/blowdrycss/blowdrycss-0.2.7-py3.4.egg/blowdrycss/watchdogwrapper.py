# python 2
from __future__ import absolute_import, unicode_literals, print_function
from builtins import str

# builtins
import logging
from time import sleep

# plugins
from watchdog.events import PatternMatchingEventHandler, FileModifiedEvent
from watchdog.observers import Observer

# custom
from blowdrycss.utilities import print_blow_dryer
from blowdrycss.timing import LimitTimer
from blowdrycss import blowdry
import blowdrycss_settings as settings


class FileEditEventHandler(PatternMatchingEventHandler):
    """ Child of PatternMatchingEventHandler that only runs blowdry.quick_parser() during file 'modified'
    events. The 'modified' case handles both the 'created' and 'moved' case. When a file is
    created or moved/copy/pasted into the project_directory, 'modified' is triggered. This reduces a number
    of unnecessary calls to blowdry.blowdry().

    __init__ override reference:
    https://github.com/gorakhargosh/watchdog/blob/d7ceb7ddd48037f6d04ab37297a63116655926d9/src/watchdog/events.py

    class_set (*set*) -- Keeps track of the current set of css class selectors.

    """
    def __init__(self, patterns=None, ignore_patterns=None, ignore_directories=False, case_sensitive=False):
        self.class_set = set()
        super(PatternMatchingEventHandler, self).__init__()

        self._patterns = patterns
        self._ignore_patterns = ignore_patterns
        self._ignore_directories = ignore_directories
        self._case_sensitive = case_sensitive

    @staticmethod
    def print_status():
        """ Prints the current status of the watchdog process. Lets the user know that the project directory is
        being watched.

        :return: None

        """
        file_types = '(' + ', '.join(settings.file_types) + ')'

        print(' ')
        print('-' * 96)
        print('The blowdrycss watchdog is watching all', file_types, 'files')
        print('in the project directory:', str(settings.project_directory))
        print('-' * 96)
        print('Pressing Ctrl + C stops the process.')
        print(' ')

    @staticmethod
    def excluded(src_path=''):
        """ Returns True if the src_path matches an excluded file. Otherwise, it returns False.

        Reference:
        https://github.com/gorakhargosh/watchdog/blob/c05183a96a5a307f00dd3a775244c98b156fc001/src/watchdog/events.py

        :type src_path: str
        :param src_path: Source path of the file system object that triggered this event.

        :return: (*bool*) -- Return True if ``src_path`` ends with a file in ``excluded_files``

        """
        excluded_files = ('clashing_aliases.html', 'property_aliases.html')
        for excluded_file in excluded_files:
            if src_path.endswith(excluded_file):
                return True
        return False

    def on_modified(self, event):
        """ Called when a file or directory is modified. Only FileModifiedEvents trigger action.

        .. note:: Only parse the modified file(s) ``blowdry(recent=True)`` to enhance efficiency.

        :type event: :class:`watchdog.event.DirModifiedEvent` or :class:`watchdog.event.FileModifiedEvent`
        :param event: Event representing file modification.

        """
        if type(event) == FileModifiedEvent and not self.excluded(src_path=event.src_path):
            logging.debug('File ' + event.event_type + ' --> ' + str(event.src_path))
            self.class_set = blowdry.parse(recent=True, class_set=self.class_set)
            self.print_status()


def main():
    """ If ``settings.auto_generate == True`` indefinitely run blowdrycss inside of the watchdog wrapper.
    The wrapper creates and attaches an file event handler to an observer. When a file is modified or
    deleted it triggers blowdry.quick_parser().

    Else, blowdry.comprehensive_parser() is run once.

    :return: None

    **Example**

    >>> from blowdrycss import watchdogwrapper
    >>> # blowdrycss_settings.auto_generate = True
    >>> watchdogwrapper.main()
    ------------------------------------------------------------------------------------------------
    blowdry_watchdog is now watching all (.html) files
    in the project directory: <project directory>
    ------------------------------------------------------------------------------------------------
    Pressing Ctrl + C stops the process.
    >>> # blowdrycss_settings.auto_generate = True
    >>> watchdogwrapper.main()
    ~~~ blowdrycss started ~~~
    ...

    """
    blowdry.boilerplate()

    if settings.auto_generate:
        event_handler = FileEditEventHandler(
            patterns=list(settings.file_types),
            ignore_patterns=[],
            ignore_directories=True
        )

        observer = Observer()
        observer.schedule(event_handler, settings.project_directory, recursive=True)
        observer.start()

        event_handler.print_status()

        limit_timer = LimitTimer()

        event_handler.class_set = blowdry.parse(recent=False, class_set=set())          # Full run first. Fill class_set
        event_handler.print_status()

        try:
            while True:
                sleep(1)
                if limit_timer.limit_exceeded:                                          # Periodically parse all files.
                    print('----- Limit timer expired -----')
                    event_handler.class_set = blowdry.parse(recent=False, class_set=set())
                    event_handler.print_status()
                    limit_timer.reset()
                    print('----- Limit timer reset -----')

        except KeyboardInterrupt:
            observer.stop()
            print_blow_dryer()

        observer.join()
    else:
        blowdry.parse(recent=False, class_set=set())


if __name__ == '__main__':
    main()
