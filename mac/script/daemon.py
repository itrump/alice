#!/usr/bin/env python
# coding: utf-8

import argparse
import os
import sys
import time
import atexit
import logging
import signal

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='mydaemon.log',
                        filemode='a')

class Daemon(object):
    """
    A generic daemon class.

    Usage: subclass the Daemon class and override the run() method
    """

    def __init__(self, pidfile, stdin='/dev/null',
                 stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def daemonize(self):
        """
        do the UNIX double-fork magic, see Stevens' "Advanced 
        Programming in the UNIX Environment" for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        """
        # Do first fork
        logging.debug('before fork')
        self.fork()
        logging.debug('fork seems ok')

        # Decouple from parent environment
        self.dettach_env()
        logging.debug('dettach env seems ok')

        # Do second fork
        self.fork()
        logging.debug('second fork seems ok')

        # Flush standart file descriptors
        sys.stdout.flush()
        logging.debug('stdout flush seems ok')
        sys.stderr.flush()
        logging.debug('stderr flush seems ok')

        # 
        self.attach_stream('stdin', mode='r')
        self.attach_stream('stdout', mode='a+')
        self.attach_stream('stderr', mode='a+')
        logging.debug('attach stream seems ok')
       
        # write pidfile
        self.create_pidfile()
        logging.debug('create pid file seems ok')

    def attach_stream(self, name, mode):
        """
        Replaces the stream with new one
        """
        stream = open(getattr(self, name), mode)
        os.dup2(stream.fileno(), getattr(sys, name).fileno())

    def dettach_env(self):
        os.chdir("/")
        os.setsid()
        os.umask(0)

    def fork(self):
        """
        Spawn the child process
        """
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write("Fork failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

    def create_pidfile(self):
      try:
        logging.warning('in create pid file')
        atexit.register(self.delpid)
        logging.warning('after register delpid')
        pid = str(os.getpid())
        open(self.pidfile,'w+').write("%s\n" % pid)
        logging.warning('after write pid file')
      except Exception as e:
          logging.warning('exception:%s', e)

    def delpid(self):
        """
        Removes the pidfile on process exit
        """
        os.remove(self.pidfile)

    def start(self):
        """
        Start the daemon
        """
        # Check for a pidfile to see if the daemon already runs
        pid = self.get_pid()

        if pid:
            message = "pidfile %s already exist. Daemon already running?\n"
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)

        # Start the daemon
        logging.debug('in base class start()')
        self.daemonize()
        logging.debug('base class daemonize seems ok')
        self.run()

    def get_pid(self):
        """
        Returns the PID from pidfile
        """
        try:
            pf = open(self.pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except (IOError, TypeError):
            pid = None
        return pid

    def stop(self, silent=False):
        """
        Stop the daemon
        """
        # Get the pid from the pidfile
        pid = self.get_pid()

        if not pid:
            if not silent:
                message = "pidfile %s does not exist. Daemon not running?\n"
                sys.stderr.write(message % self.pidfile)
            return # not an error in a restart

        # Try killing the daemon process    
        try:
            while True:
                os.kill(pid, signal.SIGTERM)
                time.sleep(0.1)
        except OSError as err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                sys.stdout.write(str(err))
                sys.exit(1)

    def restart(self):
        """
        Restart the daemon
        """
        self.stop(silent=True)
        self.start()

    def run(self):
        """
        You should override this method when you subclass Daemon. It will be called after the process has been
        daemonized by start() or restart().
        """
        raise NotImplementedError


class MyDaemon(Daemon):
    logging.debug('in derive class MyDaemon')
    def run(self):
        count = 0
        logging.debug('in derive class run()')
        while True:
          try:
            logging.debug('in derive class while loop')
            count += 1
            if count > 30:
                break
            logging.debug("[%d] daemon running..." % count)
            time.sleep(2)
          except Exception as e:
              logging.warning('exception in while,%s' % e)
        logging.debug('after while loop')


def main():
    """
    The application entry point
    """
    print  'in main'
    parser = argparse.ArgumentParser(
        #prog='PROG',
        description='Daemon runner',
        epilog="That's all folks"
    )

    parser.add_argument('operation',
                    metavar='OPERATION',
                    type=str,
                    help='Operation with daemon. Accepts any of these values: start, stop, restart, status',
                    choices=['start', 'stop', 'restart', 'status'])

    args = parser.parse_args()
    operation = args.operation

    # Daemon
    daemon = MyDaemon('/tmp/python.pid',
    )

    print 'daemon generated.'

    if operation == 'start':
        print("Starting daemon")
        logging.info('derive class start')
        daemon.start()
        logging.info('derive class start seems ok')
        pid = daemon.get_pid()
        logging.info('pid:%d' % pid)

        if not pid:
            print("Unable run daemon")
        else:
            print("Daemon is running [PID=%d]" % pid)

    elif operation == 'stop':
        print("Stoping daemon")
        daemon.stop()

    elif operation == 'restart':
        print("Restarting daemon")
        daemon.restart()
    elif operation == 'status':
        print("Viewing daemon status")
        pid = daemon.get_pid()

        if not pid:
            print("Daemon isn't running ;)")
        else:
            print("Daemon is running [PID=%d]" % pid)

    sys.exit(0)

if __name__ == '__main__':
    main()
