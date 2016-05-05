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

def centos6Updates():
	"""Does a pulp-admin sync of centos6_updates"""
	sudo('pulp-admin rpm repo sync run --repo-id=centos6_updates')

def puppetlabsProductsStage():
	"""Does a pulp-admin sync of puppetlabs products EL6 stage"""
	sudo('pulp-admin rpm repo sync run --repo-id=puppetlabs-products-EL6-stage')

def puppetlabsDependenciesStage():
	"""Does a pulp-admin sync of puppetlabs dependencies EL6 stage"""
	sudo('pulp-admin rpm repo sync run --repo-id=puppetlabs-dependencies-EL6-stage')

def epel6():
	"""Does a pulp-admin sync of epel6"""
	sudo('pulp-admin rpm repo sync run --repo-id=epel6')

def newrelic():
	"""Does a pulp-admin sync of newrelic"""
	sudo('pulp-admin rpm repo sync run --repo-id=newrelic')

def epel7():
	"""Does a pulp-admin sync of epel7"""
	sudo('pulp-admin rpm repo sync run --repo-id=epel7')

def puppetlabsProductsEL7():
	"""Does a pulp-admin sync of puppetlabs products EL7"""
	sudo('pulp-admin rpm repo sync run --repo-id=puppetlabs-products-EL7')

def puppetlabsDependenciesEL7():
	"""Does a pulp-admin sync of puppetlabs dependencies EL7"""
	sudo('pulp-admin rpm repo sync run --repo-id=puppetlabs-dependencies-EL7')

def sensuEL6():
	"""Does a pulp-admin sync of sensu EL6"""
	sudo('pulp-admin rpm repo sync run --repo-id=sensu_el_6')

def datastax():
	"""Does a pulp-admin sync of datastax"""
	sudo('pulp-admin rpm repo sync run --repo-id=datastax')

def puppetlabsProductsEL6():
	"""Does a pulp-admin sync of puppetlabs products EL6"""
	sudo('pulp-admin rpm repo sync run --repo-id=puppetlabs-products-EL6')

def puppetlabsDependenciesEL6():
	"""Does a pulp-admin sync of puppetlabs dependencies EL6"""
	sudo('pulp-admin rpm repo sync run --repo-id=puppetlabs-dependencies-EL6')

def centos6():
	"""Does a pulp-admin sync of centos6"""
	sudo('pulp-admin rpm repo sync run --repo-id=centos6')

def remiEL6():
	"""Does a pulp-admin sync of remi EL5"""
	sudo('pulp-admin rpm repo sync run --repo-id=remi-el6')

def AllPulpUpdates():
	"""Does a pulp-admin sync of everything"""
	centos6Updates()
	puppetlabsProductsStage()
	puppetlabsDependenciesStage()
	epel6()
	newrelic()
	epel7()
	puppetlabsProductsEL7()
	puppetlabsDependenciesEL7()
	sensuEL6()
	datastax()
	puppetlabsProductsEL6()
	puppetlabsDependenciesEL6()
	centos6()
	remiEL6()
