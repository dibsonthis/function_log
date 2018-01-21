from functools import wraps

def time_this(times, function, *args, **kwargs):
    '''Timing function - prints function time without logging -- /time_this(times, function, *args, **kwargs)/'''

    import time

    time_list = []

    print('\n### Calculating Average Function Time ###')

    for i in range(times):
        t1 = time.process_time()
        result = function(*args,**kwargs)
        t2 = time.process_time()
        #print(t2-t1)
        time_list.append(t2-t1)

    average_time = sum(time_list)/len(time_list)

    print('\n[Executed: {} - Average Time: {}]\n'.format(times,average_time))

    return average_time


def log_this(function):
    '''Logging decorator - Logs function name, args, kwargs, first encountered error, function time and execution time to 'filename_log.json' if log file exists. If log file does not exist, it creates one'''

    @wraps(function)
    def wrapper(*args, **kwargs):
        import time
        import json
        import sys
        import datetime

        timestamp = datetime.datetime.now()
        timestamp = '{}/{}/{} - {}:{}:{}'.format(timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second)

        try:
            t1 = time.time()
            result = function(*args,**kwargs)
            t2 = time.time()
            error = None
            timed = t2-t1

        except Exception as e:
            error = type(e).__name__
            timed = None

        arguments = {

                'name': function.__name__,
                'args': args,
                'kwargs': kwargs,
                'error': error,
                'timer': timed,
                'timestamp': timestamp
        }

        with open(sys.argv[0][:-3] + '_log.json', 'a') as logger:
            json.dump(arguments,logger)
            logger.write('\n')

        print('\n[Logged '+ function.__name__ + ' in ' + sys.argv[0][:-3] + '_log.json]\n')

        return function(*args,**kwargs)

    return wrapper

def show_log(errors=False):
    '''Returns current log file contents. If errors argument is True, returns only log file contents with encountered errors'''

    import sys
    import json

    arguments = []
    error_list = []

    try:
        with open(sys.argv[0][:-3] + '_log.json') as log:

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

        print('\nError: No log file at path {} exists.\nMake sure the "log_this" decorator is being used on at least one function within this file. If it is, make sure to run at least one instance of the function to initiate the creation of the log file.\n'.format(sys.argv[0][:-3] + '_log.json'))

def time_log(sort = False):
    '''Calculates mean time of each function and returns a dictionary of functions with function time and number of function iterations. If sort argument is True, returns a sorted dictionary of functions from fastest to slowest -- /function: [mean_time, instances of function]/'''

    import json
    import sys

    arguments = []
    function_dict = {}

    try:
        with open(sys.argv[0][:-3] + '_log.json') as log:

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

                function_dict[i] = [ sum(function_dict[i])/len(function_dict[i]), len(function_dict[i]) ]

            else:

                #function_dict[i] = sum(function_dict[i])/len(function_dict[i])
                function_dict[i] = [ sum(function_dict[i])/len(function_dict[i]), len(function_dict[i]) ]

        if sort == True:

            sorted_list = []
            sorted_dict = {}

            for i,v in function_dict.items():
                sorted_list.append([v,i])

            sorted_list = sorted(sorted_list)

            for i in sorted_list:
                sorted_dict[i[1]] = i[0]

            for i,v in sorted_dict.items():
                print('{}: {}'.format(i,v))

            return sorted_dict

        else:

            for i,v in function_dict.items():
                print('{}: {}'.format(i,v))

            return function_dict



    except FileNotFoundError:

        print('\nError: No log file at path {} exists.\nMake sure the "log_this" decorator is being used on at least one function within this file. If it is, make sure to run at least one instance of the function to initiate the creation of the log file.\n'.format(sys.argv[0][:-3] + '_log.json'))
