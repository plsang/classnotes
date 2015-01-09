class Boltzmann:

    def __init__(self,n_iter=100,eta=0.01,sample_size=100,init_sample_size=10):
        self.n_iter = n_iter
        self.eta = eta
        self.sample_size = sample_size
        self.init_sample_size = init_sample_size
    
    def sigmoid(self, u):
        return 1./(1.+np.exp(-u));

    def draw(self, Sin,T):
        """
        draw - perform single Gibbs sweep to draw a sample from distribution
        """
        N=Sin.shape[0]
        S=Sin.copy()
        rand = np.random.rand(N,1)
        for i in xrange(N):
            h=np.dot(T[i,:],S)
            S[i]=2*rand[i]<self.sigmoid(h)-1;
        return S

    def sample(self, T):
        N=T.shape[0]
        s=2*np.random.rand(N)<self.sigmoid(0)-1
        for k in xrange(self.init_sample_size):
            s=self.draw(s,T)
        S=np.zeros((N,self.sample_size))
        S[:,0]=s
        for i in xrange(1,self.sample_size):
            S[:,i]=self.draw(S[:,i-1],T)
        return S.T

    def fit(self, X):
        W_data=np.dot(X.T,X)/X.shape[1];
        print W_data.shape
        W_init = np.random.uniform(size=W_data.shape)
        W_init = np.tril(W_init) + np.tril(W_init, -1).T
        np.fill_diagonal(W_init, 0)
        print W_init
        W = W_init.copy()
        for i in range(self.n_iter):
            print 'Iteration', i
            S = self.sample(W)
            W_guess=np.dot(S.T,S)/S.shape[1];
            W += self.eta * (W_data - W_guess)
            np.fill_diagonal(W, 0)

        return W

import numpy as np

clf = Boltzmann()

A = np.array([\
[-1.,1.,1.,-1],
[1.,1.,-1,-1],
[1.,1.,1.,-1],
[-1, 1.,1.,1.],
[1, -1, 1.,-1]
])

print clf.fit(A)

