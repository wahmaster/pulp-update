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

def rabbitmq():
	"""Does a pulp-admin sync of datastax"""
	sudo('pulp-admin rpm repo sync run --repo-id=rabbitmq')

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

def centos7Base():
	"""Does a pulp-admin sync of centos7 Base"""
	sudo('pulp-admin rpm repo sync run --repo-id=centos7-base')

def centos7Updates():
	"""Does a pulp-admin sync of centos 7 updates"""
	sudo('pulp-admin rpm repo sync run --repo-id=centos7-updates')

def centos7Extras():
	"""Does a pulp-admin sync of centos 7 Extras"""
	sudo('pulp-admin rpm repo sync run --repo-id=centos7-extras')

def centos7Plus():
	"""Does a pulp-admin sync of centos7 Plus"""
	sudo('pulp-admin rpm repo sync run --repo-id=centos7-plus')

def nginxCentos6():
	"""Does a pulp-admin sync of Nginx centos 6"""
	sudo('pulp-admin rpm repo sync run --repo-id=nginx-centos-6-x86_64')

def puppetPciEl6():
	"""Does a pulp-admin sync of puppet PCI EL 6"""
	sudo('pulp-admin rpm repo sync run --repo-id=puppet-pc1-el6')

def puppetPciEl7():
	"""Does a pulp-admin sync of centos7 Plus"""
	sudo('pulp-admin rpm repo sync run --repo-id=puppet-pc1-el7')

def sensuEl7():
	"""Does a pulp-admin sync of sensu EL7"""
	sudo('pulp-admin rpm repo sync run --repo-id=sensu-el7')

def cent7basetest():
	"""Does a pulp-admin sync of cent7-base-test"""
	sudo('pulp-admin rpm repo sync run --repo-id=cent7-base-test')

def newrelicinfrael6():
	"""Does a pulp-admin sync of newrelic_infra_el6"""
	sudo('pulp-admin rpm repo sync run --repo-id=newrelic_infra_el6')

def nginxcent7():
	"""Does a pulp-admin sync of nginx-cent-7"""
	sudo('pulp-admin rpm repo sync run --repo-id=nginx-cent-7')

def nginxcent6():
	"""Does a pulp-admin sync of nginx-cent-6"""
	sudo('pulp-admin rpm repo sync run --repo-id=nginx-cent-6')

def loginPulp():
	"""Logs into pulp"""
	sudo('pulp-admin login --username=admin --password=IT@B.comRul3z!')

def AllPulpUpdates():
	"""Does a pulp-admin sync of everything"""
	loginPulp()
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
	centos7Base()
	centos7Updates()
	centos7Extras()
	centos7Plus()
	rabbitmq()
	remiEL6()
	nginxCentos6()
	puppetPciEl6()
	puppetPciEl7()
	sensuEl7()
    cent7basetest()
    newrelicinfrael6()

