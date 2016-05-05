#!/usr/bin/env python2.7


from fabric import tasks
from fabric.api import run
from fabric.api import env
from fabric.api import parallel
from fabric.api import sudo
from fabric.network import disconnect_all
from fabric.contrib.console import confirm
from fabric.colors import red, green
import re
# import os

env.skip_bad_hosts = True
env.abort_on_prompts = True
env.warn_only = True
env.user = 'fabric'
env.key_filename = '/opt/fabric/.ssh/Monkey'
env.ssh_config_path = '/opt/fabric/ssh_config'

def sync-centos6():
  """Does a pulp-admin sync of centos6_updates"""
	run('sudo pulp-admin rpm repo sync run --repo-id=centos6_updates')
	if result.failed:
    abort(red("pulp-admin command failed."))
  else:
    print(green("Success!"))
