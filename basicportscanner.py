from socket import *
import optparse
import os
import sys



parse = optparse.OptionParser()
parse.add_option("-u","--url",dest="Url",help="URL Giriniz [Gerekli]")
parse.add_option("-b","--baslangicport",dest="FP",help="Baslangic Portunu Giriniz[default=18]",default=18)
parse.add_option("-s","--sonport",dest="SP",help="Bitiş Portunu Giriniz[default=500]",default=500)
parse.add_option("-t","--taramahizi",dest="TH",help="Tarama Hızını Giriniz[default=0.2]",default=0.2)

user,args=parse.parse_args()
target = user.Url
bp = user.FP
sp = user.SP
th = user.TH
t_IP = gethostbyname(target)
os.system("clear")
os.system("figlet -f shadow PORT SCANNER")
print("""
Bu Program Yakup Eroğlu Tarafından Yazılmıştır. \nKötüye Kullanımda Sorumluluk Tamamen Kullanıcıya aittir.
""")





print ('[*]Taranan IP: ', t_IP)
   
for i in range(int(bp), int(sp)):
	try:
		s = socket(AF_INET, SOCK_STREAM)
		s.settimeout(float(th))
		conn = s.connect_ex((t_IP, i))
		if(conn == 0) :
			print ('[+]Port %d: OPEN' % (i,))
		s.close()
	except KeyboardInterrupt:
		print("\a\n[-]Programdan Çıkılıyor...")
		sys.exit()