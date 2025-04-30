x = input('File name').strip().lower()
txt = x.split('.')[-1]

if txt == 'jpeg':
    print ('image/jpeg')

elif txt == 'gif':
    print ('image/gif')

elif txt == 'jpg':
    print ('image/jpeg')

elif txt == 'png':
    print ('image/png')

elif txt == 'pdf':
    print ('application/pdf')

elif txt == 'txt':
    print ('text/plain')

elif txt == 'zip':
    print ('application/zip')

else:
    print('application/octet-stream')

