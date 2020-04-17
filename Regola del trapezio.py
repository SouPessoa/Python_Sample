#!/usr/bin/env python
# coding: utf-8

# In[22]:


"""In analisi numerica, la regola del trapezio fornisce un procedimento per il
calcolo approssimato di un integrale definito.

Si approssima l'integrale con un trapezio dai vertici:

(a, f(a)) (b,f(b)) (b,0) e (a,0) per l'integrale da (a) a (b) di f(x) in dx.

La formula è (b-a) (f(a)+f(b))/2.

Se l'area dell'integrale si discosta molto da quella di un trapezio si può
suddividere in (n) trapezi separati, ottenendo:

((b-a)/n) * ( (f(a)+f(b))/2) + somm. da k=1 a n-1 di f(a + k* ((b-a)/n)) ."""


# In[23]:


get_ipython().run_line_magic('matplotlib', 'inline')
#genera grafici in linea?


# In[24]:


import numpy as np


# In[25]:


import matplotlib.pyplot as plt     #introduce comandi grafici in stile matplot (?)


# In[26]:


def f(x):                           #definiamo una funzione f(x) come da argomento che segue
    return (x-3)*(x-5)*(x-7)+85

x = np.linspace(0, 10, 200)
y = f(x) #i valori dell'asse y vengono abbinati ad un insieme di valori x generati da linspace (start,stop, numb of samples)


# In[27]:


x


# In[28]:


y


# In[65]:


plt.plot(x, y, lw=3, label="f(x)") #plot x,y con spessore linea 3, etichetta
plt.legend() #inserisce legend
plt.xlabel("x label") #etichetta x
plt.ylabel("y label") #etichetta y
plt.title("Prova Grafico") #titolo grafico
plt.grid(ls='-.', c='grey') #grid, linestyle o ls = "-", "--", "-.",":"


# In[68]:


a, b = 2, 8 #limiti area da integrare
N = 5 #numero di spigoli


# In[69]:


xint = np.linspace (a, b, N) #linspace (start,stop, numb of samples)


# In[70]:


xint


# In[71]:


yint = f(xint)


# In[72]:


yint


# In[115]:


plt.plot(x, y, lw=3, label="f(x)") #plot x,y con spessore linea 3, etichetta
plt.legend() #inserisce legend
plt.xlabel("x label") #etichetta x
plt.ylabel("y label") #etichetta y
plt.title("Prova Grafico") #titolo grafico
plt.grid(ls='-.', c='grey') #grid, linestyle o ls = "-", "--", "-.",":"
yint_min = min (yint)
yint_max = max (yint)
plt.axis([a-1, b+1, (yint_min-10), (yint_max+20)])
plt.fill_between(xint, 0, yint, facecolor='lightblue', alpha=0.9)
plt.text(0.5 * (a + b),35,"$\int_a^b f(x)dx$", horizontalalignment='center', fontsize=30);


# In[117]:


# from __future__ import print_function #anticipa funzione print di python 3 su 2.x
from scipy.integrate import quad #quad: General purpose integration.
integrale, errore = quad(f, a, b) # quad(funzione da integrare, inizio, fine)
integrale_trapezoide = sum( (xint[1:] - xint[:-1]) * (yint[1:] + yint[:-1]) ) / 2
print("L'integrale è:", integrale, "+/-", errore)
print("L'approssimazione del trapezio con", len(xint), "spigoli è:", integrale_trapezoide)


# In[ ]:




