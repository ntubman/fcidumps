"""
Generates NACTIVE, NALPHA, NBETA, and MAX-DETS for H-chains.
"""
from math import floor
from math import factorial as fact


def get_max_dets(nactive, nalpha, nbeta):
    n_alpha = fact(nactive) / (fact(nalpha) * fact(nactive - nalpha)) 
    n_beta  = fact(nactive) / (fact(nbeta ) * fact(nactive - nbeta )) 

    return n_alpha * n_beta 


def get_data(natoms_list):
    data = []
    for natoms in natoms_list:
        assert natoms % 2 == 0
        nactive = natoms
        nalpha = natoms // 2
        nbeta = nalpha
        max_dets = get_max_dets(nactive, nalpha, nbeta)
        data.append((natoms, nactive, nalpha, nbeta, max_dets))

    return data


def print_data(data):
    print('!%-7s  %8s  %8s  %8s  %16s' % ('molec.', 'nactive', 'nalpha', 'nbeta', 'max-dets'))
    for natoms, nactive, nalpha, nbeta, max_dets in data:
        molecule = 'h%02d' % (natoms)
        max_dets_str = ''
        if max_dets < 10000000:
            max_dets_str = '%d' % (floor(max_dets))
        else:
            max_dets_str = '%.1e' % (max_dets)
        print('%-8s  %8d  %8d  %8d  %16s' % (molecule, nactive, nalpha, nbeta, max_dets_str))


def main():
    natoms_list = list(range(2, 65, 2))
    data = get_data(natoms_list)
    print_data(data)


if __name__ == '__main__':
    main()


