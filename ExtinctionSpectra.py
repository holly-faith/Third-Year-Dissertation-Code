import matplotlib.pyplot as plt
import math


# Parses data from textfile and produces x and y axis arrays from text file
def wavelength_intensity(filename): # input must be string (use '...')
    f = open(filename,'r')
    w = []
    i = []
    for line in f:
            data = line.split()
            w.append(float(data[0]))
            i.append(float(data[1]))
            
    f.close()
    return w, i

# CONSTANTS
t1 = 100*10**(-3) #seconds
t2 = 2000*10**(-3) #seconds


# Creates Ext coefficient by plugging I_spec into formula
# plug INTENSITIES of spec, bg2, ref, bg1 and match POLARISATION
  

# plot all p lines on one graph for angles 0-40
# create list: p spectrum intensities
# bgi_p_t2 used for all
# bgi_p_t1 used for all
# p_ref used for all
# create list of degrees to loop over
# wavelengths the same for all

wavelengths = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_0deg_2000ms_p_QEP009221_14-48-30-204.txt")[0]

bg2p = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_background_2000ms_p_QEP009221_15-35-38-209.txt")[1]
refp = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_ref_100ms_p_QEP009221_14-35-02-989.txt")[1]
bg1p = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_background_100ms_p_QEP009221_15-36-02-481.txt")[1]

deg0_intensitiesp = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_0deg_2000ms_p_QEP009221_14-48-30-204.txt")[1]
deg10_intensitiesp = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_10deg_2000ms_p_QEP009221_14-51-42-196.txt")[1]
deg20_intensitiesp = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_20deg_2000ms_p_QEP009221_15-04-52-196.txt")[1]
deg30_intensitiesp = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_30deg_2000ms_p_QEP009221_15-18-22-187.txt")[1]
deg40_intensitiesp_intensitiesp =  wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_40deg_2000ms_p_QEP009221_15-27-16-183.txt")[1]



bg2s = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_background_2000ms_s_QEP009221_15-37-08-980.txt")[1]
refs = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_ref_100ms_s_QEP009221_14-35-56-605.txt")[1]
bg1s = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_background_100ms_s_QEP009221_15-36-44-680.txt")[1]

deg0_intensitiess = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_0deg_2000ms_s_QEP009221_14-47-20-199.txt")[1]
deg10_intensitiess = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_10deg_2000ms_s_QEP009221_14-52-52-196.txt")[1]
deg20_intensitiess = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_20deg_2000ms_s_QEP009221_14-58-48-194.txt")[1]
deg30_intensitiess = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_30deg_2000ms_s_QEP009221_15-19-52-187.txt")[1]
deg40_intensitiess = wavelength_intensity(r"C:/Users/holly/OneDrive/Desktop/Third Year Project/Au Spectroscopy Data/Sample1_40deg_2000ms_s_QEP009221_15-25-06-183.txt")[1]


# returns an array of extinction coefficients
def extinctionspectra(I_spec, I_BG2, I_ref, I_BG1):
    a = []
    for i in range(len(I_spec)):
        a.append(float(-(math.log10((I_spec[i] - I_BG2[i])/((t2/t1)*(I_ref[i] - I_BG1[i]))))))
    
    return a

# a list of lists of extinction coefficients for each angle of incidence
p_ext = [extinctionspectra(deg0_intensitiesp, bg2p, refp, bg1p), extinctionspectra(deg10_intensitiesp, bg2p, refp, bg1p), extinctionspectra(deg20_intensitiesp, bg2p, refp, bg1p), extinctionspectra(deg30_intensitiesp, bg2p, refp, bg1p)]
incidents = ['0', '10', '20', '30', '40']


for i in range(4): 
    plt.plot(wavelengths, p_ext[i], label= incidents[i] + ' degree angle of incidence')
    
plt.legend()
plt.xlabel('wavelength (nm)')
plt.ylabel('extinction')
plt.title('P-polarised extinction spectra for multiple angles of incidence')
plt.show()
    

s_ext = [extinctionspectra(deg0_intensitiess, bg2s, refs, bg1s),extinctionspectra(deg10_intensitiess, bg2s, refs, bg1s),extinctionspectra(deg20_intensitiess, bg2s, refs, bg1s),extinctionspectra(deg30_intensitiess, bg2s, refs, bg1s),extinctionspectra(deg40_intensitiess, bg2s, refs, bg1s)]

for i in range(4): 
    plt.plot(wavelengths, s_ext[i], label= incidents[i] + ' degree angle of incidence')
    
plt.legend()
plt.xlabel('wavelength (nm)')
plt.ylabel('extinction')
plt.title('S-Polarised extinction spectra for multiple angles of incidence')
plt.show()
