# Ref. https://docs.python.org/zh-tw/3/library/subprocess.html#using-the-subprocess-module

import subprocess

# ---------------------------------
# Method 1
# ---------------------------------
# Most recommend - high level
# wait for the result, and will capture multiple information
# ('check_returncode', 'returncode', 'stderr', 'stdout')
result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


# ---------------------------------
# Method 2
# ---------------------------------
# wait for the result, and will capture ONLY output (stdout)
output = subprocess.check_output(["ls", "-l"], text=True)



# ---------------------------------
# Method 3
# ---------------------------------
# Low level usage
# Will NOT wait for the result
process = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


"""
It doesn't wait for the subprocess to complete by default; you need to explicitly call wait() or use other methods to control when to wait for the subprocess to finish.

It's useful when you need to interact with a long-running process, stream its output, or send input to it while it's running.
"""
stdout, stderr = process.communicate()
