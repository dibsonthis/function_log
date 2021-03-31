import datetime
import json
import sys
import time
from functools import wraps

__all__ = ['time_this', 'log_this', 'show_log', 'time_log']


def time_this(times, function, *args, **kwargs):
    '''Timing function - prints function time without logging -- /time_this(times, function, *args, **kwargs)/'''

    time_list = []

    print('\n### Calculating Average Function Time ###')

    for i in range(times):
        t1 = time.process_time()
        result = function(*args, **kwargs)
        t2 = time.process_time()
        # print(t2-t1)
        time_list.append(t2 - t1)

    average_time = sum(time_list) / len(time_list)

    print('\n[Executed: {} - Average Time: {}]\n'.format(times, average_time))

    return average_time


def _get_filename_log(path_log, filename_log):
    if filename_log is None:
        filename_log = sys.argv[0][:-3] + '_log.json'

    return path_log + filename_log


def log_this(logfuncarguments=True, filename_log=None, path_log='', printupdates=False):
    '''Logging decorator - Logs function name, args, kwargs, first encountered error, function time and execution time to filename_log if log file exists. If log file does not exist, it creates one'''

    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):

            timestamp = datetime.datetime.now()
            timestamp = '{}/{}/{} - {}:{}:{}'.format(timestamp.year, timestamp.month, timestamp.day, timestamp.hour,
                                                     timestamp.minute, timestamp.second)

            try:
                t1 = time.time()
                result = function(*args, **kwargs)
                t2 = time.time()
                error = None
                timed = t2 - t1

            except Exception as e:
                error = type(e).__name__
                timed = None

            arguments = {

                'name': function.__name__,
                'error': error,
                'timer': timed,
                'timestamp': timestamp
            }

            if logfuncarguments:
                arguments['args'] = args
                arguments['kwargs'] = kwargs

            filename_log_updated = _get_filename_log(path_log, filename_log)
            with open(filename_log_updated, 'a') as logger:
                json.dump(arguments, logger)
                logger.write('\n')

            if printupdates:
                print(f"\n[Logged {function.__name__} in {filename_log_updated}]\n")

            return function(*args, **kwargs)

        return wrapper

    return inner_function


def show_log(errors=False, path_log='', filename_log=None):
    '''Returns current log file contents. If errors argument is True, returns only log file contents with encountered errors'''

    arguments = []
    error_list = []

    try:
        filename_log = _get_filename_log(path_log, filename_log)
        with open(filename_log) as log:

            for i in log:
                arguments.append(json.loads(i))

        if errors == True:
            for i, v in enumerate(arguments):
                if v['error'] != None:
                    error_list.append(v)

                    print('\n {} - {} \n'.format(i, v))

            return error_list

        else:
            for i, v in enumerate(arguments):
                print('\n {} - {} \n'.format(i, v))

            return arguments

    except FileNotFoundError:

        print(
            '\nError: No log file at path {} exists.\nMake sure the "log_this" decorator is being used on at least one function within this file. If it is, make sure to run at least one instance of the function to initiate the creation of the log file.\n'.format(
                sys.argv[0][:-3] + '_log.json'))


def time_log(sort=False, path_log='', filename_log=None):
    '''Calculates mean time of each function and returns a dictionary of functions with function time and number of function iterations. If sort argument is True, returns a sorted dictionary of functions from fastest to slowest -- /function: [mean_time, instances of function]/'''

    arguments = []
    function_dict = {}

    try:
        filename_log = _get_filename_log(path_log, filename_log)
        with open(filename_log) as log:

            for i in log:
                arguments.append(json.loads(i))

        for i, v in enumerate(arguments):

            if v['name'] in function_dict:
                function_dict[v['name']].append(v['timer'])
            else:
                function_dict[v['name']] = [v['timer']]

        for i in function_dict:

            function_dict[i] = [x for x in function_dict[i] if x != None]

            if sort == False:

                function_dict[i] = [sum(function_dict[i]) / len(function_dict[i]), len(function_dict[i])]

            else:

                # function_dict[i] = sum(function_dict[i])/len(function_dict[i])
                function_dict[i] = [sum(function_dict[i]) / len(function_dict[i]), len(function_dict[i])]

        if sort == True:

            sorted_list = []
            sorted_dict = {}

            for i, v in function_dict.items():
                sorted_list.append([v, i])

            sorted_list = sorted(sorted_list)

            for i in sorted_list:
                sorted_dict[i[1]] = i[0]

            for i, v in sorted_dict.items():
                print('{}: {}'.format(i, v))

            return sorted_dict

        else:

            for i, v in function_dict.items():
                print('{}: {}'.format(i, v))

            return function_dict



    except FileNotFoundError:

        print(
            '\nError: No log file at path {} exists.\nMake sure the "log_this" decorator is being used on at least one function within this file. If it is, make sure to run at least one instance of the function to initiate the creation of the log file.\n'.format(
                filename_log))
