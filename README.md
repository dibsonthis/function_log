# Function Log Documentation

Logging and timing tests for Python functions.

# Installation

	pip install function_log
# log_this()
Logging decorator - Logs function name, args, kwargs, first encountered error, function time and execution time to 'filename_log.json' if log file exists. If log file does not exist, it creates one

	@log_this
	def function_A():
		import time
		time.sleep(1)
		
	functionA()
		
			>>> [Logged function_A in C:\Users\a_att\Desktop\Python Apps\Testing\decorators_test_log.json]
# show_log()

    from function_log import log_this, show_log, time_log, time_this

		@log_this
		def functionA():
		    import time
		    time.sleep(1)

		def functionB(a,b):
		    return a**b

		log = show_log()

		log_errors = show_log(True)

		function_times = time_log()

		sorted_function_times = time_log(True)

		functionB_average_time = time_this(10,functionB,100,100)
