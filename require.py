#include iVPN -> https://github.com/razyar/iVPN
#tor - proxychains ver3 - ver4 - proxychains-ng - proxychains.conf


import os

def install_requires():
	os.system('sudo apt-get install tor')
	os.system('sudo apt-get install proxychains')
	os.system('sudo apt-get install proxychains4')


def configure():
	os.system('unzip proxychains-ng.zip')
	os.chdir('proxychains-ng')
	os.system('./configure'); os.system('make'); os.system('sudo make install')


def config_confFile():
	os.system('sudo cp proxychains.conf /etc/')


install_requires()
configure()
config_confFile()
