
__author__ = 'Geon'
__version__ = '1.0.0'

from ConfigParser import SafeConfigParser
import os.path


"""
Default configuration.

Optionally, user can specify the file location manually using an Environment variable called TARIC_BOOKS_SETTINGS_FILE.
"""


if os.environ.get("TARIC_BOOKS_SETTINGS_FILE"):
    cfg_filename = os.environ.get("TARIC_BOOKS_SETTINGS_FILE")

cfg_defaults = {
    'port':   5000,                   # port of web application
    'APIKey':    '',                   # API Key for ISBNdb requests
    'name':         'taric_books',  # name of the server
    'logLevel':     'INFO',
    'logFormat':    '%(asctime)s %(levelname)s taric_books %(message)s'
}

cfg_loggers_defaults = {
    'keys':   'root'
}

cfg_handlers_defaults = {
    'keys':   'console, file'
}

cfg_formatters_defaults = {
    'keys':   'standard',
}

cfg_formatter_standard_defaults = {
    'class':   'logging.Formatter',
    'format':    '%(asctime)s %(levelname)s taric_books %(message)s',
}

cfg_logger_root_defaults = {
    'level':   'INFO',
    'handlers':    'console, file'
}

cfg_handler_console_defaults = {
    'level':   'DEBUG',
    'class':    'StreamHandler',
    'formatter':    'standard',
    'args': '(sys.stdout,)',
}

cfg_handler_file_defaults = {
    'level':   'DEBUG',
    'class':    'handlers.RotatingFileHandler',
    'formatter':    'standard',
    'logFilePath':    '/var/log/taric_books',
    'logFileName':    'access.log',
    'logMaxFiles':    3,
    'logMaxSize':    '5*1024*1024  ; 5 MB',
    'args': "('%(logFilePath)s/%(logFileName)s', 'a', %(logMaxSize)s, %(logMaxFiles)s)",
}

config = SafeConfigParser(cfg_defaults)

# Create the common section in the same way that we have in the configuration file: fiware-facts.cfg
config.add_section('common')
config.add_section('mysql')
config.add_section('loggers')
config.add_section('handlers')
config.add_section('formatters')
config.add_section('formatter_standard')
config.add_section('logger_root')
config.add_section('handler_console')
config.add_section('handler_file')


# Initialize the content of the config parameters
for key, value in cfg_defaults.items():
    config.set('common', key, str(value))

for key, value in cfg_loggers_defaults.items():
    config.set('loggers', key, str(value))

for key, value in cfg_handlers_defaults.items():
    config.set('handlers', key, str(value))

for key, value in cfg_formatters_defaults.items():
    config.set('formatters', key, str(value))

for key, value in cfg_formatter_standard_defaults.items():
    config.set('formatter_standard', key, str(value))

for key, value in cfg_logger_root_defaults.items():
    config.set('logger_root', key, str(value))

for key, value in cfg_handler_console_defaults.items():
    config.set('handler_console', key, str(value))

for key, value in cfg_handler_file_defaults.items():
    config.set('handler_file', key, str(value))

config.set('common', 'cfg_file_path', str(cfg_filename))
