import numpy as np

def FaultFreq(n, fr,d,D,phi):
    """
    :param n:   number of rolling elements
    :param fr:  shaft speed
    :param d:   ball diameter
    :param D:   pitch diameter
    :param phi: the angle of load from radial plane
    :return:    four fault frequency
    """
    BPFO = n*fr/2*(1 - d/D*np.cos(phi))
    BPFI = n*fr/2*(1 + d/D*np.cos(phi))
    FTF = fr/2*(1 - d/D*np.cos(phi))
    BSF = D*fr/(d)*(1 - (d/D*np.cos(phi))**2)
    print("BPFO: %.4ffr \nBPFI: %.4ffr \nFTF: %.4ffr \nBSF: %.4ffr"%(BPFI, BPFO, FTF, BSF))
    return BPFO, BPFI, FTF, BSF


if __name__ == '__main__':
    # SKF 6205-2RS JEM: drive end parameters
    n = 9
    fr = 1
    d = 0.3126 * 25.4
    D = 1.537 * 25.4
    phi = 0

    print('Drive end fault frequency:')
    bpfo, bpfi, ftf, bsf = FaultFreq(n, fr, d, D, phi)
    
    # SKF 6203-2RS JEM: fan end parameters
    n = 8
    fr = 1
    d = 0.2656 * 25.4
    D = 1.122 * 25.4
    phi = 0
    print('\nFan end fault frequency:')
    bpfo, bpfi, ftf, bsf = FaultFreq(n, fr, d, D, phi)

