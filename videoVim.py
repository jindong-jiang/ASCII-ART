
# -*- coding:utf-8 -*-
import os
from PIL import Image
import shutil

##MNOCbhlnioz*:-.
def Image2Ascii(imagename,filename,express_width,express_height,pic_string = " 1@#$^&*(veq0"):
	img = Image.open(imagename).convert('L')
	width,height = img.size
	img = img.resize((express_width,express_height))
	width , height = img.size
	pix = img.load()
	pic_ascii = ''
	count = 0

	for h in xrange(height):
		for w in xrange(width):
			pic_ascii += pic_string[int(pix[w,h])*(len(pic_string)-1)/255]
		pic_ascii += '\n'
		count += 1
		

	outfile = open(filename,'w')
	outfile.write(pic_ascii)
	outfile.close()

def walkThrough(pvAdrr,fiFileName,dirName = ''):
#下面的代码把pv转成了图片
	commend = 'mplayer -vo jpeg '+os.path.join(os.getcwd(),pvAdrr)
##	if not dirName:
##		os.chdir(dirName)
	os.mkdir('jpg')
	os.mkdir('txt')
	os.chdir('jpg')
	os.system(commend)
	jpg_address = os.getcwd()
	os.chdir(os.path.dirname(os.getcwd()))	
	list_dirs = os.walk(jpg_address)	
	
	for root , dirs,files in list_dirs:
		files.sort()
		for eachfile in files:
			path = os.path.join(root,eachfile)
			filename = eachfile.split('.')[0]+'.txt'
			txtPath = os.path.join(os.getcwd(),'txt',filename)
			Image2Ascii(path,txtPath,73,23)

	cmdline = 'cat ./txt/*.txt > ./' + fiFileName 
	os.system(cmdline)
	shutil.rmtree('jpg')
	shutil.rmtree('txt')


walkThrough('moon.mp4','moon.txt')  



