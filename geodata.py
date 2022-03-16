import json
from datetime import datetime, timedelta
now = datetime.now()
todayIST = ( datetime.now() +
 timedelta( hours=5.5 )).strftime("%d-%m-%Y:%H:%M:%S")
todayUTC = datetime.now()
todayUTC = todayUTC.strftime("%d-%m-%Y:%H:%M:%S")
today = todayUTC+"UTC"
def lambda_handler(event, context):
 request = event['Records'][0]['cf']['request']
 url_list = ['abc.xyz.com']
 headers = request['headers']
 viewerCountry = headers.get('cloudfront-viewer-country')
 if viewerCountry:
 country = viewerCountry[0]['value']
 body = {"viewerCountryCode":country}
 body = str(body)
 body = body.replace("'",'"')
 origin = headers.get('origin')
 if origin:
 origin = origin[0]['value']
 origin_scheme = origin.split(':')[0]
 origin_domain = origin.split('://')[1]
 try:
 origin_domain_1 = origin_domain.split('.')[1]
 origin_domain_2 = origin_domain.split('.')[2]
 link = origin_domain_1+'.'+origin_domain_2
 except:
 link = origin_domain
 link = link.split('/')[0]
 print(link)
 if link in url_list:
 response = {
 'status': '200',
 'statusDescription': 'OK',
 'headers': {
 'access-control-allow-origin' : [
 {
 'key': 'Access-Control-Allow-Origin',
 'value': origin
 }
 ],
 "content-type": [
 {
 'key': 'Content-Type',
 'value': 'text/html'
 }
 ]
 },
 'body': body
 }
 else:
 response = {
 'status': '403',
 'statusDescription': 'OK',
 'headers': {
 "content-type": [
 {
 'key': 'Content-Type',
 'value': 'application/json'
 }
 ]
 },
 'body': 'UnAuthorized'
 }
else:
 response = {
 'status': '200',
 'statusDescription': 'OK',
 'headers': {
 "content-type": [
 {
 'key': 'Content-Type',
 'value': 'application/json'
 }
 ]
 },
 'body': body
 }
 return response
