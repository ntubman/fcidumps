*******************************************************************************
* MACIS INPUT FILES (WM - Aug 19, 2026)
*******************************************************************************
There's a python script that generates the MACIS input file for each of the 
10 molecules with the cc-pVDZ (frozen-core) basis set. NTDETS_MAX was set
to 1,000,000 and NCDETS_MAX was set to 0.1*NTDETS_MAX. The factor of 0.1
should be refined since the search depends on NCDETS_MAX. Maybe try 0.2
and 0.3 as well. Smaller might work.

The value of REFINE_ETOL is should be adjusted for desired precision and the
PT2 flag can be turned on and off is the PT2 calculation is desired. I don't
remember why I set CI_MAX_SUB to 500, but I was running the 
standalone_driver.cxx in the feature/pt2 branch of the code for my 
calculations, so any input values should consider this.


*******************************************************************************
* FCIDUMP FILES (WM - Aug 19, 2026)
*******************************************************************************

There are 20 fcidump files in the fcidumps/data/fcidumps directory. Ten use
the small STO-3G basis set, and ten use the larger cc-pVDZ basis set with
the frozen core approximation. The two tables below give key data for each
system.

NINACTIVE: Number of orbitals to leave out of the active space. For these
           systems always set to zero unless debugging or benchmarking.

NACTIVE: Number of active orbitals. For the cc-pVDZ basis set, the fcidump 
         files have already removed the frozen orbitals, so NINACTIVE should
         still be set to zero.

NALPHA: Number of electrons with alpha spin.

NBETA: Number of electrons with beta spin.

MS2: |NALPHA - NBETA|; even though o2 has triplet ground state, the fcidump 
     file was generated for orbitals for the lowest singlet state (MS2=0). 

MAX-DETS: The maximum number of determinants that preserve NALPHA and NBETA.

PG-ORDER: The order of the molecular point group. I include it here because
          the number of MAX-DETS with non-zero amplitudes is roughly
          MAX-DETS / PG-ORDER. For example, with c2h2 with STO-3G basis, here 
          will be roughly 627,264 / 8 ~ 78,000 non-zero amplitudes. For the
          STO-3G basis set, this might matter since MAX-DETS is so small. For
          h2o with cc-pVDZ, it might be near possible to get all ~7.8E7 / 4
          non-zero amplitudes.


Basis: STO-3G
Molecule    NINACTIVE   NACTIVE     NALPHA      NBETA       MS2         MAX-DETS    PG-ORDER
c2h2                0        12          7          7         0          627,264           8
ch4                 0         9          5          5         0           15,876           4
h2co                0        12          8          8         0          245,025           4
h2o2                0        12          9          9         0           48,400      1 or 2
h2o                 0         7          5          5         0              441           4
hcn                 0        11          7          7         0          108,900           4
n2                  0        10          7          7         0           14,400           8
nh3                 0         8          5          5         0            3,136           4
o2                  0        10          8          8         0            2,025           8
sih4                0        13          9          9         0          511,225           4


Basis: cc-pVDZ / frozen core approximation
Molecule    NINACTIVE   NACTIVE     NALPHA      NBETA       MS2         MAX-DETS    PG-ORDER
c2                  0        26          4          4         0         2.2E8              8
c2h2                0        36          5          5         0         1.4E11             8
ch4                 0        33          4          4         0         1.7E9              4
h2co                0        36          6          6         0         3.8E12             4
h2o2                0        36          7          7         0         7.0E13        1 or 2
h2o                 0        23          4          4         0         7.8E7              4
hcn                 0        31          5          5         0         2.9E10             4
n2                  0        26          5          5         0         4.3E9              8
nh3                 0        28          4          4         0         4.2E8              4
sih4                0        33          4          4         0         1.7E9              4

