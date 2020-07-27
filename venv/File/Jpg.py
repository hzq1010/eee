import io

with open('000.jpg','rb') as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b'\xff\xd8'):
    text = u'is JPEG(%d bytes long)\n'
else:
    text = u'is random(%d bytes long)\n'

with io.open('summary.txt','w',encoding='gbk') as  outf:
    outf.write(text %len(jpgdata))