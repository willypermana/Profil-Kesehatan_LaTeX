import numpy as np
import matplotlib.pyplot as plt
import pandas
from textwrap import wrap
from matplotlib.ticker import FuncFormatter
import locale
locale.setlocale(locale.LC_ALL, 'id_ID.UTF8')

berkasData = r'D:\path\ke\direktori\bab_04\bab_04_01_dataJaminanKesehatan.csv'
judulDiagram = 'Cakupan BPJS Kesehatan'
berkasSimpan = r'D:\path\ke\direktori\bab_04\bab_04_01_jaminanKesehatan_a.pdf'

# read data file
colnames = ['jenisJaminan','jumlahPeserta']
data = pandas.read_csv(berkasData, names=colnames, sep=';')
labelJenis = data.jenisJaminan.tolist()
listJumlah = data.jumlahPeserta.tolist()
sliceJumlah = np.array(data.jumlahPeserta.tolist())
porcent = 100.*sliceJumlah/sliceJumlah.sum()

fig1, ax1 = plt.subplots()
# explodeTuple = (0.05, 0, 0.1, 0.0, 0.1, 0.3)
# patches, texts, autotexts = ax1.pie(listPagu, autopct='%.2f%%', pctdistance=0.85, explode=explodeTuple, startangle=80)
explodeTuple = (0.05, 0, 0.15, 0.0, 0.2)
patches, texts, autotexts = ax1.pie(listJumlah[0:5], autopct='%.2f%%', pctdistance=1.2, explode=explodeTuple, startangle=80)

for t, tes1 in enumerate(autotexts):
    tes1.set_size(9)

centre_circle = plt.Circle((0,0),0.65,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

labels = ['{0} - {1:n} orang'.format(i,j) for i,j in zip(labelJenis, sliceJumlah[0:5])]

sort_legend = False
if sort_legend:
    patches, labels, dummy =  zip(*sorted(zip(patches, labels, slicePagu),
                                          key=lambda labelJenis: labelJenis[2],
                                          reverse=True))


box = ax1.get_position()
ax1.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
plt.legend(patches, labels, loc='center', bbox_to_anchor=(0.5, -0.1),fontsize=8, fancybox=True, shadow=True, ncol=2)
		   
plt.axis('equal')

pyrfig = plt.figure(1)
pyrfig.suptitle(judulDiagram)
pyrfig.set_figwidth(8)
pyrfig.set_figheight(5)
fig.savefig(berkasSimpan, bbox_inches='tight')
plt.close(pyrfig)
#plt.show()
