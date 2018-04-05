import urllib
import requests
import re
import argparse
import logging


parser = argparse.ArgumentParser(description='Release links extractor for GitLab')
parser.add_argument('--baseurl', '-b', required=True, help='GitLab api base url, f.e. https://gitlab.example.com/')
parser.add_argument('--token', '-t', required=True, help='Security token')
parser.add_argument('--release', '-r', required=True, help='Release name to fetch file')
parser.add_argument('--project', '-p', required=True, type=str, help='Project name or id, f.e. -p MyProjectGroup/MyProject or -p 10')
parser.add_argument('--filename', '-f', required=True, help='Release attachment filename')
parser.add_argument('--loglevel', default='WARNING', help='Loggin level')
args = parser.parse_args()


numeric_level = getattr(logging, args.loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)

logging.basicConfig(level=numeric_level)

release_artifact = args.filename
tag = args.release
headers = {'PRIVATE-TOKEN': args.token } 
project = args.project 
baseurl = urllib.parse.urljoin(args.baseurl, '/api/v4') 
url = baseurl +'/projects/' + urllib.parse.quote_plus(project) + '/repository/tags/'+tag

logging.debug('Build url `{0}`'.format(url))

r = requests.get(url, headers=headers)
if not r.ok:
    exit(-1)

# Anything that isn't a square closing bracket
name_regex = "[^]]+"
# http:// or https:// or without http(s) prefix followed by anything but a closing paren
url_regex = "(?:http[s]?:/)?/[^)]+"

markup_regex = '\[({0})]\(\s*({1})\s*\)'.format(name_regex, url_regex)

urls = re.findall(markup_regex, r.json()['release']['description'])

matched_urls = [x for x in urls if re.match('.*/{0}'.format(release_artifact) ,x[1])]

print(matched_urls[0][1])
