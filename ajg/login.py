# coding:utf-8
#Recode? silahkan, asalkan jgn di ganti bot follow nya. atau jgn di hapus bot follow dan komen nya silahkan tambahkan punyamu !
#Coding by : Romi Afrizal
from .kontol import *
from .bahasa import lang
from .informasi import generate



class login:
	def __init__(self,url,cookie):
		
		try: respon=req.get(f"{url}/profile.php?v=info",cookies=cookie)
		except koneksi_error: exit(" \x1b[1;91m[!] Tidak ada koneksi")
		if "mbasic_logout_button" in respon.text:
			#print("\n\n ["+U+"*"+P+"] hai \x1b[1;35m"+parser(respon.text,"html.parser").find("title"))
			print("\x1b[1;97m [!] Mohon tunggu")
			url=url.replace("mbasic","free") if "free.facebook" in respon.url else url
			if "Laporkan Masalah" not in respon.text:
				lang(url,cookie)
				try: respon=req.get(f"{url}/profile.php?v=info",cookies=cookie)
				except koneksi_error: exit(" \x1b[1;91m[!] Tidak ada koneksi")
			generate(cookie["cookie"],parser(respon.text,"html.parser"))
			koh=kontolo_gede(url,cookie)
			# jangan di ganti ya bro atau di hapus ya bro :).
			koh.follow("/100035322483719")
			print("\x1b[1;92m ["+U+"*"+P+"] Login berhasil")
			waktu(1)
		else:
			exit("\n\x1b[1;91m [!] cookie invalid")
