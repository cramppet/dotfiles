#!/usr/bin/env python

import sys, requests
import xml.etree.ElementTree as ET
from threading import Thread
from time import sleep

KEYWORDS = None
NTHREADS = 100

def info(msg):
  print '\033[1;36m[+] \033[0m%s' % msg

def warning(msg):
  print '\033[1;31m[+] \033[0m%s' % msg

def success(msg):
  print '\033[1;32m[+] \033[0m%s' % msg

def check_host(args):
  ip = args[0]
  port_number = args[1]
  protocol = 'https' if port_number == '443' else 'http'
  url = '%s://%s/' % (protocol, ip)
  try:
    res = requests.get(url, verify=False)
    if res.status_code == 200:
      if has_keyword(res.text):
        success('%s has one or more of the defined keywords' % url)
    else:
      warning('Could not complete check for %s' % url)
  except Exception as ex:
    warning(ex)

def get_lines(filename):
  lines = open(filename).readlines()
  lines = map(lambda x: x.replace('\n', '').replace('\r', ''), lines)
  return lines

def has_keyword(text):
  global KEYWORDS
  text = text.lower()
  for keyword in KEYWORDS:
    if keyword in text:
      return True
  return False

if len(sys.argv) != 3:
  print 'usage: %s <xml file> <keywords file>' % sys.argv[0]
  sys.exit()

tree = ET.parse(sys.argv[1])
root = tree.getroot()
hosts = root.findall('host')
info('Loaded in %d hosts from XML document.' % len(hosts))

keywords = get_lines(sys.argv[2])
info('Loaded in %d keywords from file.' % len(keywords))

for host in hosts:
  if host.find('status').attrib['state'] == 'up':
    ip = host.find('address').attrib['addr']
    ports = host.find('ports').findall('port')
    for port in ports:
      port_number = port.attrib['portid']
      args = (ip, port_number)
      # check_host(args)

