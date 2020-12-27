import os
from ftplib import *

def escreverLinha(data):
    arq.write(data)
    arq.write(os.linesep)

ftp_ativo = False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()
arquivo = 'README'

with open(arquivo, 'w') as arq:
    ftp.retrlines('RETR README', escreverLinha)
ftp.quit()
