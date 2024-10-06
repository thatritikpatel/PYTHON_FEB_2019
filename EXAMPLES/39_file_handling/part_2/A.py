#module: zipfile

#class: ZipFile

#constants: ZIP_DEFLATED,ZIP_STORED

from zipfile import ZipFile,ZIP_DEFLATED

x=ZipFile('abc.zip','w',ZIP_DEFLATED)

x.write('a.txt')
x.write('b.txt')
x.write('c.txt')

x.close()


