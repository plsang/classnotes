from sklearn.utils import gen_even_slices
import numpy as np
import itertools

class RBM:
  
  def __init__(self, num_hidden, learning_rate,max_epochs, num_visible=10, batch_size=10):
    self.num_hidden = num_hidden
    self.num_visible = num_visible
    self.learning_rate = learning_rate
    # Agirlik matrisi W'yi yarat (buyukluk num_visible x num_hidden),
    # bunun icin Gaussian dagilimi kullan, ortalama=0, standart sapma 1. 
    self.weights = 0.1 * np.random.randn(self.num_visible, self.num_hidden)    
    # Egilim (bias) icin ilk satir ve ilk kolona 1 degeri koy
    self.weights = np.insert(self.weights, 0, 0, axis = 0)
    self.weights = np.insert(self.weights, 0, 0, axis = 1)
    self.max_epochs = max_epochs
    self.batch_size = batch_size
    
  def fit(self, data):
    """
    Makinayi egit

    Parametreler
    ----------
    data: Her satirin "gorunen" veri oldugu bir matris
    """
    num_examples = data.shape[0]
    n_batches = int(np.ceil(float(num_examples) / self.batch_size))
        
  def run_visible(self, data):
    """
    RBM'in egitilmis olduguna farz ederek, gorunen veri uzerinde
    RBM'i islet, ve h icin bir orneklem al

    Parametreler
    ----------
    data: Her satirin gorunen veri oldugu bir matris
    
    Returns
    -------
    hidden_states: data icindeki her satira tekabul eden gizli h verisi
    """
    num_examples = data.shape[0]
    
    hidden_states = np.ones((num_examples, self.num_hidden + 1))
    
    data = np.insert(data, 0, 1, axis = 1)

    hidden_activations = np.dot(data, self.weights)
    hidden_probs = self._logistic(hidden_activations)
    hidden_states[:,:] = hidden_probs > \
        np.random.rand(num_examples, self.num_hidden + 1)  
    hidden_states = hidden_states[:,1:]
    return hidden_states

          
  def run_hidden(self, data):
    """
    run_visible'a benzer, sadece gizli veri icin gorunen veri uret
    """

    num_examples = data.shape[0]

    visible_states = np.ones((num_examples, self.num_visible + 1))

    data = np.insert(data, 0, 1, axis = 1)

    visible_activations = np.dot(data, self.weights.T)
    visible_probs = self._logistic(visible_activations)
    visible_states[:,:] = visible_probs > \
        np.random.rand(num_examples, self.num_visible + 1)

    visible_states = visible_states[:,1:]
    return visible_states
  
  def _logistic(self, x):
    return 1.0 / (1 + np.exp(-x))
    
  def fit(self, data):
    """
    Makinayi egit

    Parametreler
    ----------
    data: Her satirin "gorunen" veri oldugu bir matris
    """
    num_examples = data.shape[0]
    n_batches = int(np.ceil(float(num_examples) / self.batch_size))
    batch_slices = list(gen_even_slices(n_batches * self.batch_size,
                                        n_batches, num_examples))
    
    for iteration in xrange(1, self.max_epochs + 1):
        for batch_slice in batch_slices:
            print X[batch_slice]
    
if __name__ == "__main__":    
    import numpy as np
    X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    model = RBM(num_hidden=2, learning_rate=0.1,max_epochs=10, num_visible=4, batch_size=2)
    model.fit(X)
    
