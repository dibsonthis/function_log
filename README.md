# Function Log Documentation

Logging and timing tests for Python functions.

# Installation

	pip install function_log


# Usage

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
