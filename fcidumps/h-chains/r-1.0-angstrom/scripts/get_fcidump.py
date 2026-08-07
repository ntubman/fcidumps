import pyscf
from pyscfutils.fciutils import get_fci_wavefunction

mol = pyscf.M(
atom = '''
   H          0.0000000000          0.0000000000         -2.5000000000
   H          0.0000000000          0.0000000000         -1.5000000000
   H          0.0000000000          0.0000000000         -0.5000000000
   H          0.0000000000          0.0000000000          0.5000000000
   H          0.0000000000          0.0000000000          1.5000000000
   H          0.0000000000          0.0000000000          2.5000000000
''',
basis = 'sto-3g',
symmetry = True,
verbose = 5
)

myhf = mol.RHF().run(conv_tol = 1.0e-12)
pyscf.tools.fcidump.from_scf(myhf, 'h06.fcidump')

