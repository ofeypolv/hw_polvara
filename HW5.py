import numpy as np
from numpy.fft import rfft,irfft
import matplotlib.pyplot as plt
import requests
import argparse

#1D discrete cosine transform
def dct(y):
    N = len(y)
    y2 = np.empty(2*N,float)
    y2[:N] = y[:]
    y2[N:] = y[::-1]

    c = rfft(y2)
    phi = np.exp(-1j*np.pi*np.arange(N)/(2*N))
    return np.real(phi*c[:N])

#1D inverse discrete cosine transform
def idct(a):
    N = len(a)
    c = np.empty(N+1,complex)

    phi = np.exp(1j*np.pi*np.arange(N)/(2*N))
    c[:N] = phi*a
    c[N] = 0.0
    return irfft(c)[:N]

urls = {
    "dow.txt": "http://www-personal.umich.edu/~mejn/cp/data/dow.txt",
    "dow2.txt": "http://www-personal.umich.edu/~mejn/cp/data/dow2.txt"
}

percs = {"10%": 0.1,"2%": 0.02}

fts = {"DFT": [rfft,irfft],"DCT": [dct,idct]}

parser = argparse.ArgumentParser(description="Dow Jones closing values")
parser.add_argument("URL", type=str,help='Dow Jones closing values file')
parser.add_argument("perc", type=str,help='Percentage of Fourier coefficients to consider')
parser.add_argument("ft", type=str,help='Type of Fourier transform to use')
args = parser.parse_args()

URL_run = urls.get(args.URL, "")
perc_run = percs.get(args.perc, "")
ft_run = fts.get(args.ft, "")

r = requests.get(URL_run)
rows = np.array(r.text.split("\n"))
rows = rows[:len(rows)-1]
dow = rows.astype(np.float)
d = np.arange(0,len(dow))
plt.plot(d,dow,label="data")
plt.xlabel("days")
plt.ylabel("DJ closing values")
coeff = ft_run[0](dow)
coeff[int(perc_run*len(coeff)):] = 0
invf = ft_run[1](coeff)
plt.plot(d,invf,label="ft")
plt.legend()
plt.show()