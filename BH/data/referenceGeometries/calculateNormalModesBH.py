import os
from ase.units import Ry
from ase.vibrations import Vibrations
from ase.io.trajectory import Trajectory
from ase.calculators.siesta import Siesta
from ase.calculators.siesta.parameters import Species

from basis import basisSet
from arguments import singlePointArguments

traj = Trajectory('./BHstructures.traj')

oxygenIndex = [atom.index for atom in traj[0] if atom.symbol == 'O'][0]
hydrogen1Index = [atom.index for atom in traj[0] if atom.symbol == 'H'][0]
hydrogen2Index = [atom.index for atom in traj[0] if atom.symbol == 'H'][1]

for j in range(len(traj)):
    system = traj[j]

    for k in range(0, oxygenIndex):
        if k <= 31:
            system[k].tag = 1
        elif k >= 32:
            system[k].tag = 2

    siesta = Siesta(
        label=f'structure-{j}',
        mesh_cutoff=700*Ry,
        kpts=[1, 1, 1],
        xc="BH",
        species=[
            Species(symbol="H", basis_set=basisSet("H"), pseudopotential="H.psf"),
            Species(symbol="O", basis_set=basisSet("O"), pseudopotential="O.psf"),
            Species(symbol='Au', basis_set=basisSet('Au2'), pseudopotential='Au.gga.psf', tag=1),
            Species(symbol='Au', basis_set=basisSet('Au3'), pseudopotential='Au.gga.psf', tag=1)
        ],
        fdf_arguments=singlePointArguments(),
    )

    system.calc = siesta

    if not os.path.exists(f'structure-{j}'):
        os.makedirs(f'structure-{j}')

    os.chdir(f'image-{j}')

    vib = Vibrations(
        atoms=system,
        indices=[ oxygenIndex, hydrogen1Index, hydrogen2Index ],
        name=f'structure-{j}',
        delta=0.02,
        nfree=2
    )

    vib.run()
    print(vib.get_vibrations().get_energies_and_modes())
    vib.summary()

    os.chdir('../')

    system = None
    siesta = None