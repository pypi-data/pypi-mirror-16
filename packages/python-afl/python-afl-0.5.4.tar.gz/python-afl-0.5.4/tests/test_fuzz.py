# encoding=UTF-8

# Copyright © 2015-2016 Jakub Wilk <jwilk@jwilk.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import distutils.version
import glob
import os
import re
import shutil
import subprocess as ipc
import sys
import tempfile
import time

from .tools import (
    SkipTest,
    assert_true,
)

here = os.path.dirname(__file__)

def get_afl_version():
    child = ipc.Popen(['afl-fuzz'], stdout=ipc.PIPE)
    version = child.stdout.readline()
    child.stdout.close()
    child.wait()
    if str != bytes:
        version = version.decode('ASCII')
    version = re.sub(r'\x1b\[[^m]+m', '', version)
    match = re.match(r'^afl-fuzz\s+([0-9.]+)b?\b', version)
    version = match.group(1)
    return distutils.version.StrictVersion(version)

def sleep(n):
    time.sleep(n)
    return n

def check_core_pattern():
    with open('/proc/sys/kernel/core_pattern', 'rb') as file:
        pattern = file.read()
        if str != bytes:
            pattern = pattern.decode('ASCII', 'replace')
        pattern = pattern.rstrip('\n')
        if pattern.startswith('|'):
            raise SkipTest('/proc/sys/kernel/core_pattern = ' + pattern)

def _test_fuzz(workdir, target, dumb=False):
    input_dir = workdir + '/in'
    output_dir = workdir + '/out'
    os.mkdir(input_dir)
    os.mkdir(output_dir)
    with open(input_dir + '/in', 'w') as file:
        file.write('0')
    crash_dir = output_dir + '/crashes'
    queue_dir = output_dir + '/queue'
    have_crash = False
    have_paths = False
    n_paths = 0
    def setup_env():
        os.environ['AFL_SKIP_CPUFREQ'] = '1'
        os.environ['AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES'] = '1'
        os.environ['AFL_NO_AFFINITY'] = '1'
    with open('/dev/null', 'wb') as devnull:
        with open(workdir + '/stdout', 'wb') as stdout:
            cmdline = ['py-afl-fuzz', '-i', input_dir, '-o', output_dir, '--', sys.executable, target]
            if dumb:
                cmdline[1:1] = ['-n']
            print(cmdline)
            afl = ipc.Popen(
                cmdline,
                stdout=stdout,
                stdin=devnull,
                preexec_fn=setup_env,
            )
    try:
        timeout = 10
        while timeout > 0:
            if afl.poll() is not None:
                break
            have_crash = len(glob.glob(crash_dir + '/id:*')) >= 1
            n_paths = len(glob.glob(queue_dir + '/id:*'))
            have_paths = (n_paths == 1) if dumb else (n_paths >= 2)
            if have_crash and have_paths:
                break
            timeout -= sleep(0.1)
        if afl.returncode is None:
            afl.terminate()
            afl.wait()
    except:
        afl.kill()
        raise
    with open(workdir + '/stdout', 'rb') as file:
        stdout = file.read()
        if str != bytes:
            stdout = stdout.decode('ASCII', 'replace')
        print(stdout)
    if not have_crash and '/proc/sys/kernel/core_pattern' in stdout:
        check_core_pattern()
    assert_true(have_crash, "target program didn't crash")
    assert_true(have_paths, 'target program produced {n} distinct paths'.format(n=n_paths))

def test_fuzz(dumb=False):
    def t(target):
        tmpdir = tempfile.mkdtemp(prefix='python-afl.')
        try:
            _test_fuzz(
                workdir=tmpdir,
                target=os.path.join(here, target),
                dumb=dumb,
            )
        finally:
            shutil.rmtree(tmpdir)
    yield t, 'target.py'
    yield t, 'target_persistent.py'

def test_fuzz_dumb():
    if get_afl_version() < '1.95':
        def skip():
            raise SkipTest('afl-fuzz >= 1.95b is required')
    else:
        skip = False
    for t in test_fuzz(dumb=True):
        yield skip or t

# vim:ts=4 sts=4 sw=4 et
