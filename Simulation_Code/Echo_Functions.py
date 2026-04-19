#Necessary Libraries

import numpy as np
import scipy.constants as c
import scipy as sc
from qutip import Qobj, create, destroy, sigmax, sigmay, sigmaz

#hbar = 1

def commutator(A, B):
    return A * B - B * A
def anticommutator(A, B):
    return A * B + B * A



def x_eigenstates(t, w0=0, **kwargs):
    w0 = w0(t) if callable(w0) else w0
    H = w0 * sigmax()
    return H
def y_eigenstates(t, w0=0, **kwargs):
    H = w0 * sigmay()
    return H
def Larmour(t, w0=0, **kwargs):
    H = w0 * sigmaz()
    return H
def LabRabi(t, w0=0, Omega=0, **kwargs):
    Omega = Omega(t) if callable(Omega) else Omega
    H = w0*sigmaz() + Omega*np.cos(2*w0*t)*sigmax()
    return H
def RotatingRabi(t,w0=0, Omega=0, **kwargs):
    Omega = Omega(t) if callable(Omega) else Omega
    H = w0*sigmaz() + 0.5*Omega*sigmax()
    return H

def SpinLock(t, w0=0, Omega1=0, Omega2=0, **kwargs):
    Omega1 = Omega1(t) if callable(Omega1) else Omega1
    Omega2 = Omega2(t) if callable(Omega2) else Omega2
    H = 0.5*Omega1*sigmax() + 0.5*Omega2*sigmay() + w0*sigmaz()
    return H

def CCD(t, w0=0, Omega=0, em=0, wm=0, **kwargs):
    Omega = Omega(t) if callable(Omega) else Omega

    H = 0.5*(Omega*sigmax() - 2*em*np.sin(wm * t)*sigmay()) + w0*sigmaz()
    return H





def evolution(t, rho_flat,system, **kwargs):
    # Reshape the flattened density matrix back to its original shape
    rho = Qobj(rho_flat.reshape((2, 2)))

    H = globals()[system](t,**kwargs)  # Get the Hamiltonian based on the system argument
    
    # Calculate the time derivative of the density matrix using the von Neumann equation
    drho_dt = -1j * commutator(H, rho)
    for L in kwargs.get('L_ops', []):
        drho_dt += L * rho * L.dag() - 0.5 * anticommutator(L.dag() * L, rho)
    
    # Flatten the time derivative back to a 1D array for integration
    return drho_dt.full().flatten()
