#!/data/data/com.termux/files/usr/bin/python
# Start : (2020-08-28 03:07:28)
# Done  : Now!
# © Copyright 2020 Ezz-Kun
# (love-love) kyun-kyunnn (∩˃o˂∩)♡

from bs4 import BeautifulSoup as bs_
from os import system as _Auth
from string import ascii_letters as _ascii
from time import sleep
from random import randint
import sys,re
import requests as _req

m = '\033[1;31m'
k = '\033[1;33m'
h = '\033[1;32m'
b = '\033[1;34m'
p = '\033[1;37m'

__banner__ = (f"""
 {b}╔╗╔{p}┌─┐┌─┐{b}╔╗╔┬{p}┌┬┐┌─┐ {b} ╦ ╦{p}┬─┐{b}╦  
 ║║║{p}├┤ │ │{b}║║║{p}││││├┤───{b}║ ║{p}├┬┘{b}║  
 ╝╚╝{p}└─┘└─┘{b}╝╚╝{p}┴┴ ┴└─┘  {b}╚═╝{p}┴└─{b}╩═╝
 ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ {p}≻{b}
 [{p}●{b}]{p} Author {h}:{p} Ezz-Kun {p}kyun-Kyun {b}♥(ˆ⌣ˆԅ)
 [{p}●{b}]{p} Tools  {h}:{p} Neonime {m}~ {p}Url{b}
 [{p}●{b}]{p} Versi  {h}:{p} {randint(10,999)}.{randint(10,100)} New Vers{k}!

 {b}~ {h}»{b}[{p} Neonime {b}]{h}« {m}!{b}~
""")

fis_batch = []
fis_ongoing = []
fis_movies = []
fis_random = []
fis_hed = {"User-Agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/191.0.0.35.96;]"}

class _sprint(object):
	def __init__(self,string):
		for i in string +'\n':
			sys.stdout.write(str(i))
			sys.stdout.flush()
			sleep(0.00050)

def _BatchPages(url):
	fis_batch.append(url)
	judul = []
	link = []
	try:
		_shogi = _req.get(url,headers=fis_hed).text
		_bes = bs_(_shogi,'html.parser')
		for _Ape in _bes.findAll('div',class_='item'):
			judul.append(_Ape.find('span',class_='title').text)
			link.append(_Ape.find('a')["href"])
		Next_ = _bes.find('div',class_='pag_b').find('a')
		Prev_ = _bes.find('div',class_='pag_a').find('a')
		_Auth('clear')
		_sprint(__banner__)
		_sprint(f'  \t{m}≈ {b}[{p} List Of Batch Anime In Neonime.vip {b}] {m}≈\n')
		for _cek,cek in enumerate(judul):
			_sprint(f' {b}[{p}{_cek+1}{b}].{p} {cek}')
		if Next_ != None:
			_sprint(f'\n\t  {b}[ {p}Type {b}[{h}N{b}]{p} For Next Type {b}[{h}P{b}]{p} For Prev {b}]{p} ')
		cos_ = input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Choice {b}:{p} ')
		if cos_ == '':
			print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Nothing Choice{m}!')
			exit()
		elif str(cos_) in _ascii:
			if str(cos_).lower() == 'n':
				_BatchPages(Next_["href"])
			elif str(cos_).lower() == 'p':
				if Prev_ != None:
					_BatchPages(Prev_["href"])
				else:
					exit(f'{b}[{m}»{p}Neo{m}«{b}]{p} Can Not Previous First Page Lol{m}!{p}')
		elif str(cos_) not in _ascii:
			if int(cos_)-1 < len(judul):
				_BatchDownload(link[int(cos_)-1])
			else:
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Your Choice Out Of Range{m}!')
				exit()
		else:
				exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} Invalid Choice{m}!')
	except _req.exceptions.ConnectionError:
		exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} No Internet Connection{m}!')
	except (EOFError,KeyboardInterrupt):
		exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} Passing{m}!')

class _BatchDownload(object):
	def __init__(self,url):
		self.url = url
		self._info = []
		self._tempo = []
		self.server = []
		self.links = []
		self.reso = []
		self.__information(self.url)
	def __information(self,url):
		try:
			_shogi = _req.get(url,headers=fis_hed).text
			_bes = bs_(_shogi,'html.parser')
			_data = _bes.find('div',class_='sbox')
			for data in _data.findAll('span',class_='dark_text'):
				self._info.append(data.text)
				self._tempo.append(data.nextSibling)
			try:
				_sinon = ''.join(ko.text for ko in bs_(re.search(r'/></p><p>(.*?)\<br/>',_bes.decode()).group(),'html.parser').find_all('p'))
			except AttributeError:
				exit(' {b}[{m}»{p}Neo{m}«{b}]{p} Can Not Find Sinopsys Anime')
			_Auth('clear')
			_sprint(__banner__)
			_sprint(
			f" {b}[{h}≋{b}].{p} Title: {_data.find('h1').text}\n"
			f" {b}[{h}≋{b}].{p} Upload: {_data.findAll('p')[0].text}\n"
			f" {b}[{h}≋{b}].{p} Synopis: {_sinon}"
			)
			for _pis,pis in enumerate(self._info):
				_sprint(f' {b}[{h}≋{b}].{p}{pis}{self._tempo[_pis]}')
			input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Enter To Continue{m}!')
			self.__downloadPage(_bes)
		except _req.exceptions.ConnectionError:
			exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} No Internet Connection{m}!')
		except (EOFError,KeyboardInterrupt):
			exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} Passing{m}!')
	def __downloadPage(self,_parser):
		cek = _parser.findAll('p',class_='smokeurl')
		try:
			for cek_ in cek:
				self.reso.append(cek_.find('strong').text)
			_Auth('clear')
			_sprint(__banner__)
			for xo, xo_ in enumerate(self.reso):
				_sprint(f' {b}[{p}{xo+1}{b}]{p}.{xo_}')
			_cos = _chos = int(input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Resolusi {b}≽{p} '))
			if _cos == '':
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Nothing Choice{m}!')
				exit()
			elif (_cos)-1 < len(self.reso):
				for get_ in cek[_cos-1].find_all('a'):
					self.server.append(get_.text),
					self.links.append(get_["href"])
			else:
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Your Choice Out Of Range{m}!')
				exit()
			for dex,dex_ in enumerate(self.server):
				_sprint(f' {b}[{p}{dex+1}{b}].{p} {dex_} {b}≽{p} {self.links[dex]}')
			_set =  int(input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Open With Browser {b}:{p} '))
			if _set == '':
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Nothing Choice{m}!')
				exit()
			elif (_set)-1 < len(self.links):
				_Auth(f'termux-open {self.links[_set-1]}')
				if len(fis_batch) != 0:
					_BatchPages(fis_batch[0])
					del fis_batch[:]
				elif len(fis_ongoing) != 0:
					_ongoingPage(fis_ongoing[0])
					del fis_ongoing[:]
				elif len(fis_movies) != 0:
					_MoviesPage(fis_movies[0])
					del fis_movies[:]
				else:
					pass
			else:
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Index Out Of Range{m}!')
				exit()
		except (EOFError,KeyboardInterrupt,ValueError):
			exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} Passing{m}!')

def _MoviesPage(url):
	fis_movies.append(url)
	_Judul = []
	Haref_ = []
	try:
		_shogi = _req.get(url,headers=fis_hed).text
		_bes = bs_(_shogi,'html.parser')
		for _sao in _bes.findAll('div',class_='boxinfo'):
			_Judul.append(_sao.find('span',class_='tt').text)
			Haref_.append(_sao.find('a')["href"])
		Next_ = _bes.find('div',class_='pag_b').find('a')
		Prev_ = _bes.find('div',class_='pag_a').find('a')
		_Auth('clear')
		_sprint(__banner__)
		_sprint(f'  \t{m}≈ {b}[{p} List Of Anime Movies In Neonime.vip {b}] {m}≈\n')
		for var, var_ in enumerate(_Judul):
			_sprint(f' {b}[{p}{var+1}{b}].{p} {var_}')
		if Next_ != None:
			_sprint(f'\n\t  {m}≈ {b}[{p} Type {m}[{p}N{m}]{p} For Next Type {m}[{p}P{m}]{p} For Prev {b}]{m} ≈')
		_cus = input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Choice {b}:{p} ')
		if _cus == '':
			print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Nothing Choice{m}!')
			exit()
		elif str(_cus) in _ascii:
			if str(_cus).lower() == 'n':
				_MoviesPage(Next_["href"])
			elif str(_cus).lower() == 'p':
				if Prev_ != None:
					_MoviesPage(Prev_["href"])
				else:
					exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} Can Not Previous First Pages Lol{m}!{p}')
		elif str(_cus) not in _ascii:
			if int(_cus)-1 < len(_Judul):
				_MoviesDownload(Haref_[int(_cus)-1])
			else:
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Index Out Of Range{m}!')
				exit()
		else:
			print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Invalid Choice{m}!')
			exit()
	except _req.exceptions.ConnectionError:
		exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} No Internet Connection{m}!')
	except (EOFError,KeyboardInterrupt):
		exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} Passing{m}!')

class _MoviesDownload(object):
	def __init__(self,url):
		self.url = url
		self.judul = []
		self.link = []
		self.sin = []
		self.sin_ = []
		self.server = []
		self.links = []
		self.reso = []
		self._show_info(self.url)
	def _show_info(self,url):
		try:
			_shogi = _req.get(url,headers=fis_hed).text
			_bes = bs_(_shogi,'html.parser')
			_Auth('clear')
			_sprint(__banner__)
			_sprint(
			f" {b}[{h}≋{b}]{p} Tittle {b}:{p} {_bes.find('div',class_='data').find('h1').text}\n"
			f" {b}[{h}≋{b}]{p} Type {b}:{p} {_bes.find('span',class_='calidad2').text}\n"
			f" {b}[{h}≋{b}]{p} Genre {b}:{p} {', '.join(c.text for c in _bes.findAll('a',rel='category'))}\n"
			f" {b}[{h}≋{b}]{p} Ratting {b}:{p} {_bes.find('span',itemprop='ratingValue').text}\n"
			f" {b}[{h}≋{b}]{p} Published {b}: {_bes.find('i',itemprop='datePublished').text}\n"
			f" {b}[{h}≋{b}]{p} Synopsis {b}:{p} {''.join(l.text for l in _bes.find('div',itemprop='description').findAll('p'))}"
			)
			for _lose in _bes.find('div',itemprop='description').findAll('span',class_='dark_text'):
				self.sin.append(_lose.text)
				self.sin_.append(_lose.nextSiblin)
			for cek_,c in enumerate(self.sin):
				_sprint(f' {b}[{h}≋{b}]{p} {self.sin[cek_]} {self.sin_[cek_]}')
			input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Press Enter To Continue{m}!{p} ')
			self._show_download(_bes)
		except _req.exceptions.ConnectionError:
			exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} No Internet Connection{m}!')
		except (EOFError,KeyboardInterrupt):
			exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} Passing{m}!')
	def _show_download(self,_parser):
		try:
			seki_ = _parser.findAll('div',class_='sbox')[-1]
			_data = seki_.findAll('li')
			for _cler in _data:
				if _cler.text == 'MP4' or _cler.text == 'MKV':
					_data.remove(_cler)
			for _label in _data:
				self.reso.append(_label.find('label').text)
			_Auth('clear')
			_sprint(__banner__)
			for var,var_ in enumerate(self.reso):
				_sprint(f' {b}[{p}{var+1}{b}].{p}{var_}')
			_cos = int(input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Resolusi {b}≽{p} '))
			if _cos == '':
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Nothing Choice{m}!')
				exit()
			elif (_cos-1) < len(_data):
				for get_ in _data[_cos-1].find_all('a'):
					self.server.append(get_.text.strip())
					self.links.append(get_["href"])
			else:
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Your Choice Out Of Range{m}!')
				exit()
			for i,i_ in enumerate(self.links):
				_sprint(f' {b}[{p}{i+1}{b}].{p} {self.server[i]} {b}≽{p} {i_}')
			_Op = int(input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Open With Browser {b}:{p} '))
			if _Op == '':
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Nothing Choice{m}!')
				exit()
			elif (_Op-1) < len(link):
				_Auth(f'termux-open {self.links[_Op-1]}')
				if len(fis_batch) != 0:
					_BatchPages(fis_batch[0])
					del fis_batch[:]
				elif len(fis_ongoing) != 0:
					_ongoingPage(fis_ongoing[0])
					del fis_ongoing[:]
				elif len(fis_movies) != 0:
					_MoviesPage(fis_movies[0])
					del fis_movies[:]
				else:
					pass
			else:
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Your Choice Out Of Range{m}!')
				exit()
		except (EOFError,KeyboardInterrupt,ValueError):
			exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} Passing{m}!')

def _SearchTitle(url):
	judul = []
	link = []
	if 'https://' not in url:
		url = (f"https://neonime.vip/?s={url.replace(' ','+')}")
		fis_random.append(url)
	else:
		url = url
	try:
		_shogi = _req.get(url,headers=fis_hed).text
	except _req.exceptions.ConnectionError:
		exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} No Internet Connection{m}!')
	_bes = bs_(_shogi,'html.parser')
	box__ = _bes.find_all('div',class_='boxinfo episode')
	if len(box__) != 0:
		for _stmp in box__:
			judul.append(_stmp.find('span',class_='tt').get_text())
			link.append(_stmp.find('a')["href"])
		_Auth('clear')
		_sprint(__banner__)
		for va, va_ in enumerate(judul):
			_sprint(f' {b}[{p}{va+1}{b}].{p} {va_}')
		__prev = _bes.find('div',class_='pag_a').find('a')
		__next = _bes.find('div',class_='pag_b').find('a')
		if __next is not None:
			_sprint(f'\n\t  {b}[ {p}Type {b}[{p}N{b}]{p} For Next Type {b}[{p}P{b}]{p} For Prev {b}]{p} ')
		_chos = input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Choice {b}:{p} ')
		if _chos == '':
			print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Nothing Choice{m}!')
			exit()
		elif str(_chos) in _ascii:
			if str(_chos).lower() == 'n':
				_SearchTitle(__next["href"])
			elif str(_chos).lower() == 'p':
				if __prev is not None:
					_SearchTitle(__prev["href"])
				else:
					exit(f'{b}[{m}»{p}Neo{m}«{b}]{p} Can Not Previous Fisrt Page Lol{m}!{p}')
		elif str(_chos) not in _ascii:
			if int(_chos)-1 < len(judul):
				_find_url(link[int(_chos)-1])
			else:
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Your Choice Out Of Range{m}!')
				exit()
		else:
			print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Nothing Choice{m}!')
			exit()
	else:
		print(f" {b}[{m}»{p}Neo{m}«{b}]{p} Tittle ``{' '.join(url.split('=')[-1].split('+'))}`` Not Found In Neonime{m}!")
		exit()

def _find_url(url):
	resolusi = []
	_data = []
	server = []
	link = []
	try:
		_shogi = _req.get(url,headers=fis_hed).text
	except _req.exceptions.ConnectionError:
		exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} No Internet Connection{m}!')
	_bes = bs_(_shogi,'html.parser')
	_box = _bes.find('div',class_='sbox')
	_tmp = _box.find_all('li')
	if len(_tmp) != 0:
		for clear in _tmp:
			if clear.get_text() == 'MP4':
				_tmp.remove(clear)
			elif clear.get_text() == 'MKV':
				_tmp.remove(clear)
			else:pass
			_data.append(clear)
		for _label in _box.find_all('label'):
			resolusi.append(_label.get_text())
		_Auth('clear')
		_sprint(__banner__)
		for var, var_ in enumerate(resolusi):
			_sprint(f' {b}[{p}{var+1}{b}].{p}{var_}')
		try:
			_chos = int(input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Resolusi {b}≽{p} '))
			if _chos == '':
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Nothing Choice{m}!')
				exit()
			elif (_chos-1) < len(_data):
				for pico_ in _data[_chos].findAll('a'):
					server.append(pico_.get_text())
					link.append(pico_["href"])
			else:
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Your Choice Out Of Range{m}!')
				exit()
			for srv, srv_ in enumerate(server):
				_sprint(f' {b}[{p}{srv+1}{b}].{p} {srv_} {b}≽{p} {link[srv]}')
			_set = int(input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Open With Browser {b}:{p} '))
			if _set == '':
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Nothing Choice{m}!')
				exit()
			elif (_set-1) < len(link):
				_Auth(f'termux-open {link[_set-1]}')
				if len(fis_batch) != 0:
					_BatchPages(fis_batch[0])
					del fis_batch[:]
				elif len(fis_ongoing) != 0:
					_ongoingPage(fis_ongoing[0])
					del fis_ongoing[:]
				elif len(fis_movies) != 0:
					_MoviesPage(fis_movies[0])
					del fis_movies[:]
				else:
					pass
			else:
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Index Out Of Range{m}!')
				exit()
		except ValueError:
			print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Your Choice Must Only Number{m}!')
			exit()
	if len(_bes.findAll('p',class_='smokeurl')) == 0:
		_MoviesDownload(url)
	if len(_bes.findAll('p',class_='smokeurl')) != 0:
		_BatchDownload(url)

def _ongoingPage(url):
	fis_ongoing.append(url)
	judul = []
	link = []
	try:
		_shogi = _req.get(url,headers=fis_hed).text
	except _req.exceptions.ConnectionError:
		exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} No Internet Connection{m}!')
	_bes = bs_(_shogi,'html.parser')
	_xbox = _bes.findAll('div',class_='boxinfo')
	for __oyasan in _xbox:
		judul.append(__oyasan.find('span',class_='tt').get_text())
		link.append(__oyasan.find('a')["href"])
	_Auth('clear')
	_sprint(__banner__)
	_sprint(f'  \t{m}≈ {b}[{p} List Of OnGoing Anime In Year 2020 {b}] {m}≈\n')
	for var, var_ in enumerate(judul):
		_sprint(f' {b}[{p}{var+1}{b}].{p} {var_}')
	Prev_ = _bes.find('div',class_='pag_a').find('a')
	Next_ = _bes.find('div',class_='pag_b').find('a')
	if Next_ is not None:
		_sprint(f'\n\t  {b}[{p} Type {b}[{p}N{b}]{p} For Next Type {b}[{p}P{b}]{p} For Prev {b}]{p} ')
	_chos = input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Choice {b}:{p} ')
	if _chos == '':
		print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Nothing Choice{m}!')
		exit()
	elif str(_chos) in _ascii:
		if str(_chos).lower() == 'n':
			_ongoingPage(Next_["href"])
		elif str(_chos).lower() == 'p':
			if Prev_ is not None:
				_ongoingPage(Prev_["href"])
			else:
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Can Not Previous First Pages Lol{m}!{p}')
				exit()
	elif str(_chos) not in _ascii:
		if  int(_chos)-1 < len(judul):
			_ongoingEps(link[int(_chos)-1])
		else:
			print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Index Out Of Range{m}!')
			exit()
	else:
		print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Invalid Choice{m}!')
		exit()

def _ongoingEps(url):
	metadata = []
	tempo = []
	episode = []
	judul = []
	release = []
	sinopsis = []
	try:
		_shogi = _req.get(url,headers=fis_hed).text
	except _req.exceptions.ConnectionError:
		exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} No Internet Connection{m}!')
	_bes = bs_(_shogi,'html.parser')
	_kintel = _bes.find('div',class_='spaceit_pad').find('span').next_sibling
	meta__ = _bes.findAll('div',class_='metadatac')
	for _meta in meta__:
		metadata.append(_meta.find('b').text)
		tempo.append(_meta.find('span').text)
	_desc = _bes.find('div',itemprop='description')
	for _des in _desc.find_all('p'):
		sinopsis.append(str(_des.text))
	_Auth('clear')
	_sprint(__banner__)
	for ii, ii_ in enumerate(metadata):
		_sprint(f' {b}[{p}≆{b}].{p} {ii_} {b}: {p}{tempo[ii]}')
	_sprint(f" {b}[{p}≆{b}].{p} Synopsis {b}:{p} {''.join(sinopsis)}")
	for _sinon in _desc.findAll('div',class_='spaceit_pad'):
		_sprint(f' {b}[{p}≆{b}].{p} {_sinon.text}')
	input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Press Enter To View Eps List {m}!{p} ')
	for _tamper in _bes.find_all('div',class_='episodiotitle'):
		judul.append(_tamper.find('a').get_text())
		episode.append(_tamper.find('a')["href"])
		release.append(_tamper.find('span',class_='date').get_text())
	first_ = _bes.find('span',class_='title').text
	_Auth('clear')
	_sprint(__banner__)
	_sprint(f' {m}⇵ {b}[{p} List Eps Of Anime {h}{first_} {b}] {m}⇵{p}\n')
	for var, var_ in enumerate(judul):
		_sprint(f' {b}[{p}{var+1}{b}].{p} {var_}\n   {h}▪ {p}Release At {m}:{b} {release[var]}{p}')
	_chus = input(f'\n {b}[{h}»{p}Neo{h}«{b}]{p} Choice {b}:{p} ')
	if _chus == '':
		print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Nothing Choice{m}!')
		exit()
	elif str(_chus) in _ascii:
		if str(_chus).lower() == 'n':
			pass
		elif str(_chus).lower() == 'p':
			pass
	elif str(_chus) not in _ascii:
		if int(_chus)-1 < len(judul):
			_find_url(episode[int(_chus)-1])
		else:
			print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Index Out Of Range{m}!')
			exit()
	else:
		print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Invalid Choice{m}!')
		exit()

def is_error():
	try:
		input(f' {b}[{h}»{p}Neo{h}«{b}]{p} Press Enter For Back To Home{m}!{p} ')
		_MainNeo()
	except (EOFError,KeyboardInterrupt):
		exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} Passing{m}!')

def _MainNeo():
	_Auth('clear')
	_sprint(__banner__)
	_sprint(f' {b}[{p}01{b}].{p} Search Anime \n {b}[{p}02{b}].{p} List Anime Ongoing\n {b}[{p}03{b}]. {p}List Anime Movies\n {b}[{p}04{b}].{p} List Anime Batch\n {b}[{p}05{b}].{p} Show More Information\n {b}[{p}06{b}]. {p}Exit{m}!\n{p}')
	try:
		_ciku = int(input(f' {b}[{h}»{p}Neo{h}«{b}]{p} Choice {b}:{p} '))
		if _ciku == '':
			print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Nothing Choice{m}!')
			exit()
		elif _ciku == 1:
			_Auth('clear')
			_sprint(__banner__)
			title_ = input(f' {b}[{h}»{p}Neo{h}«{b}]{p} Title {b} ≽ {p} ')
			if title_ == '':
				print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Tittle Is None{m}!')
				exit()
			else:
				_SearchTitle(title_)
		elif _ciku == 2:
			_ongoingPage('https://neonime.vip/tvshows-genre/ongoing/')
		elif _ciku == 5:
			_sprint(f"""
 {m}▪{p} Gak Ada Function Auto Download Nya, Sengaja 
   Lewat Open Browser Biar Bisa Ke UC Browser& Download
   Juga Jadi Wuzz.. Wuzz..
 {m}▪{p} Neonime Klo Yg Ongoing Lumayan Banyak, Tapi Klo
   Batch Gak Terlalu, Jadi Bisa Pake yg versi Kusonime,
 {b}▪{p} Versi KusoNime {b}≽{p} https://github.com/Ezz-Kun/kusonime-url
 {b}▪{p} Versi OpLoverz {b}≽{p} https://github.com/Ezz-Kun/oploverz-url
 {h}▪{p} Contact Wa : 085325463021
""")
			input(f' {b}[{h}»{p}Neo{h}«{b}]{p} Press Enter To Back {b}!{p} ')
			_MainNeo()
		elif _ciku == 6:
			exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} Exit Tools{m}!')
		elif _ciku == 3:
			_MoviesPage('https://neonime.vip/movies/')
		elif _ciku == 4:
			_BatchPages('https://neonime.vip/batch/')
		else:
			sleep(0.4)
			print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Invalid Choice{m}!')
			exit()
	except (EOFError,KeyboardInterrupt):
		sleep(0.4)
		exit(f' {b}[{m}»{p}Neo{m}«{b}]{p} Passing{m}!')
	except ValueError:
		sleep(0.4)
		print(f' {b}[{m}»{p}Neo{m}«{b}]{p} Your Choice Must Only Number{m}!')
		exit()
	
if __name__=="__main__":
	_MainNeo()
