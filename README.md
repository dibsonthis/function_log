# Function Log Documentation

Logging and timing tests for Python functions.

# Installation

	pip install function_log
	
# Usage

	from function_log import log_this, show_log, time_log, time_this
	
# @log_this()
Logging decorator - Logs function name, args, kwargs, first encountered error, function time and execution time to 'filename_log.json' if log file exists. If log file does not exist, it creates one

	@log_this
	def function_A():
		import time
		time.sleep(1)
		
	@log_this
	def function_B():
		import time
		time.sleep(1)
		
	>>> function_A()
		
	>>> [Logged function_A in path/to/file_log.json]
	
	>>> function_B()
		
	>>> [Logged function_B in path/to/file_log.json]
	
# show_log(errors=False)
Returns current log file contents. If errors argument is True, returns only log file contents with encountered errors

	>>> log = show_log()
    
	>>> 0 - {'name': 'function_A', 'args': [], 'kwargs': {}, 'error': None, 'timer': 1.0011684894561768, 'timestamp': '2018/1/21 - 16:46:21'}
	     1 - {'name': 'function_B', 'args': [], 'kwargs': {}, 'error': None, 'timer': 1.000422716140747, 'timestamp': '2018/1/21 - 16:51:36'}
		

	>>> log
	
	>>> [{'name': 'function_A', 'args': [], 'kwargs': {}, 'error': None, 'timer': 1.0011684894561768, 'timestamp': '2018/1/21 - 16:46:21'}, 			
	     {'name': 'function_B', 'args': [], 'kwargs': {}, 'error': None, 'timer': 1.000422716140747, 'timestamp': '2018/1/21 - 16:51:36'}]
    
 # time_log(sort=False)
 Calculates mean time of each function. If sort argument is True, returns a sorted dictionary of functions from fastest to slowest
 
    
 	>>> function_times = time_log()
	
	>>> function_A: [1.000795602798462, 1]
	    function_B: [1.000351905822754, 1]
	    
	>>> function_times
	
	>>> {'function_A': [1.000795602798462, 1], 'function_B': [1.000351905822754, 1]}
	
	>>> sorted_function_times = time_log(True)
	
	>>> function_B: [1.000351905822754, 1]
	    function_A: [1.000795602798462, 1]
	    
	>>> function_times
	
	>>> {'function_B': [1.000351905822754, 1], 'function_A': [1.000795602798462, 1]}
	
# time_this(times, function, *args, **kwargs)
Timing function - prints function time without logging -- /time_this(times to execute function, function, *args, **kwargs)/

	def function_A(a,b):
		a**b
		
	>>> function_A_time = time_this(10,function_A,100,10000)
	
	>>> ### Calculating Average Function Time ###
	
	    [Executed: 10 - Average Time: 0.0006852515631798894]
	    
	>>> function_A_time
	
	>>> 0.0006852515631798894
