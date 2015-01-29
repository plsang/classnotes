### T�rk�e

ODE, �ok De�i�kenli Calculus, Lineer Cebir, Hesapsal Bilim,
Istatistik, Fonksiyonel Analiz video derslerinden, ya da ders
kitaplarindan alinan notlarin Latex ile yazilmis ve PDF olarak
�retilmi� dosyalar� burada bulunabilir. Matematik ve Uygulamal�
Matematik hakkinda yazilmis yazilarimiz da var. Ornek Python kodlari
gerektigi yerde yazi icinde ya da onunla beraber ayni dizinde
olacaktir.

Dok�manlar�n i�inde gorulen kod python/ipython ortami icinden
isletilebilir. ipython kurmak icin

```
http://ipython.org/install.html
```

Kurulum olarak en acisiz kurulum Anaconda uzerinden

```
http://continuum.io/downloads
```

Komut satirindan [1] ipython baslatmak icin

```
ipython notebook --pylab=inline
```

kullanilabilir. Tabii bu durumda belgelerde gorulen kodlar elle
girilecektir. Eger kodlari not defteri disinda, dosya bazli, pur
Python olarak isletmek isterseniz, 

```
import numpy as np
import matploblib.pylab as plt
```

ibarelerini script'in basina eklemek gerekir. Bu durumda kodlar
`dosya.py` gibi bir dosya icinde kaydedilir, ve `python dosya.py` ile
komut satirindan isletilir.

Kurulmasi gereken bazi Python paketleri (eger Anaconda tarafindan kurulmadiysa)

Scikit Learn
Pandas
Numpy
Scipy

Not: Daha komplike bir kullanim, Emacs icinde LaTeX dokumani *icinde*
iken Python kodlarini `emacs-ipython` adli bir teknoloji uzerinden
direk belge icinde isletmektir (arka planda ipython'a baglaniyor, yani
ayni temel yapi kullaniliyor). Bu durumda, emacs-ipython gereken tum
ipython ayarlarini kendisi yapiyor.

[1] Komut satiri nedir? Windows uzerindeyseniz `Start | All Programs |
Accessories | Command Prompt` ile baslatilir. Terminal usulu metin
bazli bir iletisim aracidir. Ubuntu uzerinde `Applications |
Accessories | Terminal` ile baslatilabilir. Kodlari ve dokumanlari
nereye actiysaniz, o dizine komut satirindan `cd [dizin ismi]` ile
gidebilirsiniz, ve buradan ipyton komutunu isletebilirsiniz, ya da
dokuman icindeki kodlari bir dosya.py dosyasina yazdiktan sonra
`python dosya.py` ile kodlari isletebilirsiniz.

### English

Here are lecture notes in ODE, Multivariate Calculus, Linear Algebra,
Computational Science, Statistics, Functional Analysis classes written
in Latex, in Turkish. There is also a small handbook of collected math,
applied math articles. All necessary Python code is also shared[ in
the same directory as the article / classnote.

--

Blog

http://sayilarvekuramlar.blogspot.com

Classnotes

https://dl.dropboxusercontent.com/u/1570604/skfiles/app-math-tr.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/ode_mattuck.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/compscieng1.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/compscieng2.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/linear_strang.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/multivar_calculus.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/stat.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/pde.pdf

https://dl.dropboxusercontent.com/u/1570604/skfiles/functional_analysis.pdf

### Latex Format

The format of these documents, fonts, the pseudocode look-and-feel was
taken from Andrew Cotter's thesis called *Stochastic Optimization for
Machine Learning*.

