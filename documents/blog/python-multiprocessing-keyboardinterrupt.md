title: "Python: Using KeyboardInterrupt with a Multiprocessing Pool"
description: There is a better way to do it, and noone has posted it yet.
tags: python, howto
date: 2011-05-31
---
I've recently been working on a parallel processing task in Python, using the multiprocessing module's Pool
class to manage multiple worker processes.  Work comes in large batches, so there are frequent periods
(especially right after startup) where all of the workers are idle.  Unfortunately, when workers are idle,
Python's KeyboardInterrupt is not handled correctly by the multiprocessing module, which results in not only
a lot of stacktraces spewed to the console, but also means the parent process will hang indefinitely.

There is quite a lot of suggestions for mitigating this issue, such as given in [this question on Stack
Overflow][so-keyboardinterrupt].  Many places point to [Bryce Boe's article][bryceboe-keyboardinterrupt],
where he advocates rolling your own replacement for the multiprocessing module's Pool class, but that seems
to not only invite bugs and added maintenance overhead, but also doesn't address the root cause.

I have figured out (what I think is) a better solution to the problem, and have not found anyone else
mentioning it online, so I have decided to share that here.  It not only solves the problem of handling the
interrupt for both idle and busy worker processes, but also precludes the need for worker processes to even
care about KeyboardInterrupt in the first place.

The solution is to prevent the child processes from ever receiving KeyboardInterrupt in the first place, and
leaving it completely up to the parent process to catch the interrupt and clean up the process pool as it
sees fit.  In my opinion this is the most optimal solution, because it reduces the amount of error handling
code in the child process, and prevents needless error spew from idle workers.

The following example shows how to do this, and how it works with both idle and busy workers: 

    #!/usr/bin/env python

    # Copyright (c) Amethyst Reese
    # Licensed under the MIT License

    import multiprocessing
    import os
    import signal
    import time

    def init_worker():
        signal.signal(signal.SIGINT, signal.SIG_IGN)

    def run_worker():
        time.sleep(15)
        
    def main():
        print "Initializng 5 workers"
        pool = multiprocessing.Pool(5, init_worker)

        print "Starting 3 jobs of 15 seconds each"
        for i in range(3):
            pool.apply_async(run_worker)

        try:
            print "Waiting 10 seconds"
            time.sleep(10)

        except KeyboardInterrupt:
            print "Caught KeyboardInterrupt, terminating workers"
            pool.terminate()
            pool.join()

        else:
            print "Quitting normally"
            pool.close()
            pool.join()

    if __name__ == "__main__":
        main()

This code is also available on Github as [amyreese/multiprocessing-keyboardinterrupt][github-keyboardinterrupt].
If you think there's a better way to accomplish this, please feel free to fork it and submit a pull request.
Otherwise, hopefully this helps settle this issue for good.

[so-keyboardinterrupt]: http://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool "Keyboard Interrupts with python's multiprocessing Pool on Stack Overflow"
[bryceboe-keyboardinterrupt]: http://www.bryceboe.com/2010/08/26/python-multiprocessing-and-keyboardinterrupt/ "Python Multiprocessing and KeyboardInterrupt by Bryce Boe"
[github-keyboardinterrupt]: http://github.com/amyreese/multiprocessing-keyboardinterrupt "amyreese/multiprocessing-keyboardinterrupt on Github"

