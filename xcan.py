import os,time,sys,requests
print('\u001b[32m')
bnr='''
 /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$
| $$  / $$ /$$__  $$ /$$__  $$| $$$ | $$
|  $$/ $$/| $$  \__/| $$  \ $$| $$$$| $$
 \  $$$$/ | $$      | $$$$$$$$| $$ $$ $$
  >$$  $$ | $$      | $$__  $$| $$  $$$$
 /$$/\  $$| $$    $$| $$  | $$| $$\  $$$
| $$  \ $$|  $$$$$$/| $$  | $$| $$ \  $$
|__/  |__/ \______/ |__/  |__/|__/  \__/

'''
print(bnr)
print('\u001b[0m[1] Sqli Scan\n[2] XSS Scan\n[3] Port Scan\n[4] LFI Scan\n[0] Exit')
opt = input('\n\u001b[36mEnter a option : \u001b[0m')
if opt=='1':
	time.sleep(.5)
	os.system('python sql.py')
elif opt=='2':
	print('\n')
	os.system('python xss.py')
elif opt=='3':
	ip = input('Enter IP : ')
	os.system('\u001b[32mnmap '+ip+'\u001b[0m')
elif opt=='4':
	lfiurl=input('Enter URL : ')
	reqlfi=requests.get(lfiurl+'/etc/passwd')
	if 'root:' in reqlfi.text:
		print('\u001b[32mLFI Detected!\u001b[0m')
	else:
		print('\u001b[31mLFI not Detected!\u001b[0m')
elif opt=='0':
	sys.exit()
else:
	print('\u001b[31mNot Found!!\u001b[0m')
