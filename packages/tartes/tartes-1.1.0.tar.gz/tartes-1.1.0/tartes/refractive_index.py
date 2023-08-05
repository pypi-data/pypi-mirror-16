#!/usr/bin/python

import numpy as np
from .refice import *


def refice2016_allsites(wls):
    """return real and imag part of ice refractive index. wls in meter"""
    refice2016_i = ki2016_allsites_i/(4*np.pi)*(wls2016*1e-9)

    r2008 = refice2008(wls)
    r2016 = np.exp(np.interp(np.log(wls*1e9), np.log(wls2016), np.log(refice2016_i)))

    r = np.where(wls < 600e-9, r2016, r2008[1])
    return r2008[0], r


def refsoot_imag(wavelengths):

    wl_um = 1e6*wavelengths

    index_soot_real = 1.811+0.1263*np.log(wl_um)+0.027*np.log(wl_um)**2+0.0417*np.log(wl_um)**3
    index_soot_im = 0.5821+0.1213*np.log(wl_um)+0.2309*np.log(wl_um)**2-0.01*np.log(wl_um)**3
    m_soot = index_soot_real - 1j*index_soot_im

    ######m_soot = 1.95- 1j*0.79
    temp = (m_soot**2-1)/(m_soot**2+2)
    return temp.imag

    
#HULIS from Hoffer (2006) abs = 4*pi*khi/lambda*1/density
def refhulis_imag(wavelengths):

    wl_um = 1e6*wavelengths

    density_hulis = 2000  # invente pour le moment
    print("Warning: density_hulis = 2000 #invente pour le moment")
    #m_hulis = complex(1.67, -8e17*(wl_um*1e3)**(-7.0639)*1e3*density_hulis*wl_um*1e-6/(4*pi))
    m_hulis = 1.67+1j*-8e17*(wl_um*1e3)**(-7.0639)*1e3*density_hulis*wl_um*1e-6/(4*np.pi)
    temp = (m_hulis**2-1)/(m_hulis**2+2)
    
    return temp.imag
    



wls2016 = np.array([3.200000000000000000e+02,3.400000000000000000e+02,3.600000000000000000e+02,3.800000000000000000e+02,
    4.000000000000000000e+02,4.200000000000000000e+02,4.400000000000000000e+02,4.600000000000000000e+02,
    4.800000000000000000e+02,5.000000000000000000e+02,5.200000000000000000e+02,5.400000000000000000e+02,
    5.600000000000000000e+02,5.800000000000000000e+02,6.000000000000000000e+02,6.200000000000000000e+02,
    6.400000000000000000e+02,6.600000000000000000e+02,6.800000000000000000e+02,7.000000000000000000e+02,
    7.200000000000000000e+02,7.400000000000000000e+02,7.600000000000000000e+02,7.800000000000000000e+02,
    8.000000000000000000e+02,8.200000000000000000e+02,
    8.400000000000000000e+02,8.600000000000000000e+02,8.800000000000000000e+02])


ki2016_allsites_i = np.array([3.066803487174857984e-02,2.651605554756345656e-02,2.273599166530016966e-02,
    2.097706714455724319e-02,1.960328036622836778e-02,1.737098080101528649e-02,
    1.817329929565221491e-02,2.023141123160310598e-02,2.399459119847575581e-02,
    2.965756384721501132e-02,3.809128562334715418e-02,5.007387545129352718e-02,
    6.786277314846404785e-02,9.033217743069171801e-02,1.209321012151513969e-01,
    1.643078586855780954e-01,2.259657652228024005e-01,2.895125390555925993e-01,
    3.466127645338715757e-01,4.348518162734526515e-01,5.538336398136216587e-01,
    6.475725785539989676e-01,8.054669840606335507e-01,1.077546262702049340e+00,
    2.105047338384279598e+00,2.284325387248066441e+00,2.376293449119358581e+00,
    3.230968332143583588e+00,4.975275440449847153e+00])


