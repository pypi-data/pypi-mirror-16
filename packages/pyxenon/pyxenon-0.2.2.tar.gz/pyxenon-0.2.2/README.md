# Python interface to Xenon

[![PyPi version](https://img.shields.io/pypi/v/pyxenon.svg)](https://pypi.python.org/pypi/pyxenon)
[![Apache 2 License](https://img.shields.io/github/license/NLeSC/pyxenon.svg?branch=master)](https://raw.githubusercontent.com/NLeSC/pyxenon/master/LICENSE)
![Python versions](https://img.shields.io/pypi/pyversions/pyxenon.svg)
[![Build Status](https://travis-ci.org/NLeSC/pyxenon.svg?branch=master)](https://travis-ci.org/NLeSC/pyxenon)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/35e155e3bb08459aa2c24622d5fdb0d3)](https://www.codacy.com/app/NLeSC/pyxenon)

Python interface to the [Xenon middleware library](http://nlesc.github.io/Xenon/). Xenon provides a simple programming interface to various pieces of software that can be used to access distributed compute and storage resources. Underneath it uses [JPype](https://jpype.readthedocs.io), which uses the Java Native Interface to interface with a Java Virtual Machine.

## Installation

The package is available on PyPi, to use that release, just install with:
```
pip install -U pyxenon
```

To install from source, run,

```shell
pip install -U .
```

If the install fails due to a missing Java requirement, export environment variable `JAVA_HOME` pointing to your Java installation and try again. 

Currently, Xenon library version 1.1.0 is placed in the `xenon/libs` directory with its dependencies. To use another version, replace these jar files with alternative jar files and run `pip install -U .`. Alternatively, a custom classpath can be provided to `xenon.init()`.

## Usage

Except for initialization and finalization, the API follows the [Xenon 1.1.0 Java API](http://nlesc.github.io/Xenon/versions/1.1.0/javadoc/). First `xenon.init()` must be called to set up the Java Virtual Machine and its classpath. Then `x = xenon.Xenon()` creates a new Xenon instance. Either use with-resources syntax, as shown the following example, or call `x.close()` to end Xenon. If neither is done, the object destructor will try to finalize Xenon. However, Python does not guarantee that this destructor is called, which may cause a Java process running after python has finished execution.

See [JPype documentation](https://jpype.readthedocs.io) for how to use Java classes in Python.

```python
import xenon
import os

# use default classpath
xenon.init()

# start xenon
with xenon.Xenon() as x:
	# create a new job scheduler, using SSH to localhost to submit new jobs.
	jobs = x.jobs()
	sched = jobs.newScheduler('ssh', 'localhost', None, None)

	# make a new job description. The executable must already be present on the target host.
	desc = xenon.jobs.JobDescription()
	desc.setExecutable('hostname')
	desc.setStdout(os.getcwd() + '/stdout.txt')

	# submit a job
	job = jobs.submitJob(sched, desc)
	jobs.waitUntilDone(job, 1000)

	# read the standard output of the job. We can do this directly because
	# we ran on localhost, otherwise, we need to transfer the file first.
	with open(job.getJobDescription().getStdout()) as f:
	    print(f.read())
```

## API

The API consists of all methods and classes exported in `__init__.py`, `xenon.files`, `xenon.jobs`, `xenon.exceptions`, and `xenon.conversions`.  Of each of the classes, find further documentation in the corresponding Xenon class.

Due to a limitation of Java and Python interactions, classes can currently not be imported directly, they need to be called with their module name. For example, `from xenon.exceptions import XenonException; try: ...; except XenonException: ...` will fail. The `XenonException` must be called as `import xenon; xenon.exceptions.XenonException` or `from xenon import exceptions; exceptions.XenonException`.

For more limitations on Java with Python see the [JPype documentation](http://jpype.readthedocs.io/en/latest/). In particular, everywhere where in the Java API a varargs is expected as a function argument (e.g. `public getJobs(Scheduler scheduler, Job... jobs))`), provide an list instead of a variable number of arguments.

## Contributing

Contributions can be made using GitHub pull requests. To add a feature, first install the test requirements
```
pip install -U ".[test]"
```
and then run
```
nosetests
```
until all tests succeed. The command checks against flake8 code standards and syntax errors. Then commit, to make sure the change didn't break any code.  The pull request will be evaluated in [Travis](https://travis-ci.org/NLeSC/pyxenon).
