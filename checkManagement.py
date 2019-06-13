#!/usr/bin/env python

import requests
import argparse

log_info = ''
log_debug = ''

parser = argparse.ArgumentParser(description='Enable/Disable one or more New Relic Synthetic checks')
parser.add_argument('apikey', help='New Relic Admin User API Key')
parser.add_argument('enable', help='Enable or Disable Synthetic checks', choices=['enable','disable'])
parser.add_argument('checkId', 
					help='Whitespace seperated list of Synthetic Check ID\'s to act upon (example: -c aab91f1a-75c4-49bd-b5c9-a78957bddc87 9878f17f-aa12-43a9-8510-6b9ca61ad465)',
					nargs='+')

args = parser.parse_args()

api_key = args.apikey
checkIds = args.checkId

if args.enable == 'enable':
	toEnable = 'ENABLED'
else:
	toEnable = 'DISABLED'

url_check_patch = 'https://synthetics.newrelic.com/synthetics/api/v3/monitors/'

headers_check_patch = {'X-Api-Key': api_key, 'Content-Type':'application/json'}

print('')
print('Script start')
print('Arguments passed:')
print('   api_key: ' + api_key)
print('   toEnable: ' + toEnable)
print('   checkIds: ')
print('      ' + '\n      '.join(checkIds))
print('')
print('')
for checkId in checkIds:
	#print('checkIds: ' + checkId)

	##Patch Synthetic Check with desired status
	response = requests.patch(url_check_patch + checkId, headers=headers_check_patch, json={'status': toEnable})

	if response.status_code == 204:
		print('Success: Synthetics Check ID ' + checkId + ' set to ' + toEnable)
	else:
		print('FAILED: Could NOT change Synthetics Check ID ' + checkId + ' to ' + toEnable)
		print(response.status_code)	
print('')
print('Script complete')
print('')