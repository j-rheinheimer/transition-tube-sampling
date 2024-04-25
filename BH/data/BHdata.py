import numpy as np


def cm_to_ev(value):
    conversion_value = 1.23981e-4

    return value * conversion_value


def isolated():
    energies = np.array([ 0.20139897, 0.47574893, 0.49861081 ])

    eigenvalues = np.array([ 1624.4, 3837.2, 4021.6 ])

    eigenvectors = np.array(
        [
            [
                [ 3.05852190e-18,  1.79475926e-03,  6.80839373e-02],
                [ 9.39505355e-18, -4.22107158e-01, -5.56321750e-01],
                [ 9.50304267e-18,  3.93787261e-01, -5.25073405e-01]
            ],

            [
                [ 1.02205820e-17, -3.02631248e-02,  4.33121498e-02],
                [-1.03669556e-17,  7.51208890e-01, -5.35876790e-01],
                [ 5.52904301e-17, -2.70696723e-01, -1.51646117e-01]
            ],

            [
                [ 2.17863682e-18, -6.05155436e-02, -2.17137166e-02],
                [ 1.98699983e-16,  2.18354833e-01, -1.94770107e-01],
                [ 1.65871290e-16,  7.41738400e-01,  5.39133148e-01]
            ]
        ]
    )

    isolated = {
        'name': 'isolated',
        'energies': energies,
        'eigenvalues': eigenvalues,
        'eigenvectors': eigenvectors
    }

    return isolated


def flat():
    energies = np.array([0.20268495, 0.46818512, 0.48178041])

    eigenvalues = np.array([1634.8, 3776.2, 3885.8])

    eigenvectors = np.array(
        [
            [
                [ 0.05504838, -0.0382619 ,  0.01100247],
                [-0.66707872, -0.02764209, -0.16535032],
                [-0.20587847,  0.63506234, -0.00442364]
            ],

            [
                [-0.02955777,  0.04011648, -0.00525801],
                [ 0.01263461, -0.82903811, -0.05221807],
                [ 0.45623045,  0.19286797,  0.12915   ]
            ],

            [
                [-0.04482352, -0.04678399, -0.01472354],
                [-0.04418041,  0.49455005,  0.0214194 ],
                [ 0.7548051 ,  0.2478307 ,  0.2094098 ]
            ]
        ]
    )

    flat = {
        'name': 'flat',
        'energies': energies,
        'eigenvalues': eigenvalues,
        'eigenvectors': eigenvectors
    }

    return flat


def down():
    energies = np.array([ 0.19899331, 0.46422204, 0.47753183 ])

    eigenvalues = np.array([ 1605.0, 3744.2, 3851.6 ])

    eigenvectors = np.array(
        [
            [
                [ 1.73168571e-04,  6.52366370e-04,  6.85932928e-02],
                [-4.10069780e-01, -6.27335599e-03, -5.42102034e-01],
                [ 4.08239253e-01, -4.67697368e-03, -5.37238681e-01]
            ],

            [
                [-1.46575617e-02,  4.28251323e-04,  4.77574811e-02],
                [ 6.75943263e-01, -4.82952592e-03, -4.67648383e-01],
                [-4.42984580e-01, -2.68778258e-03, -2.83883482e-01]
            ],

            [
                [-6.57153779e-02, -8.11358698e-05, -1.06752288e-02],
                [ 3.96375937e-01, -3.32141127e-03, -3.22898188e-01],
                [ 6.46363170e-01,  4.43057052e-03,  4.92461128e-01]
            ]
        ]
    )

    down = {
        'name': 'down',
        'energies': energies,
        'eigenvalues': eigenvalues,
        'eigenvectors': eigenvectors
    }

    return down


def up():
    energies = np.array([0.20591418, 0.45055294, 0.47768863])

    eigenvalues = np.array([1636.5, 3781.6, 3890.6])

    eigenvectors = np.array(
        [
            [
                [-1.64326503e-03,  6.48265382e-04, -6.85098338e-02],
                [-3.95281434e-01, -4.20058003e-03,  5.21188475e-01],
                [ 4.26243945e-01, -4.44638837e-03,  5.54897215e-01]
            ],

            [
                [ 3.49399283e-02,  2.92349868e-04, -4.14407571e-02],
                [ 2.07930893e-01, -8.54779875e-04,  1.04861087e-01],
                [-7.62892907e-01, -3.79133688e-03,  5.56036142e-01]
            ],

            [
                [-5.74667512e-02,  1.99122287e-04, -2.53719177e-02],
                [ 7.58632389e-01, -4.04668496e-03,  5.54690187e-01],
                [ 1.53244864e-01,  9.47291485e-04, -1.50743902e-01]
            ]
        ]
    )

    up = {
        'name': 'up',
        'energies': energies,
        'eigenvalues': eigenvalues,
        'eigenvectors': eigenvectors
    }

    return up


def neb_initial():
    energies = np.array([ 0.20100637, 0.46248715, 0.47438623 ])

    eigenvalues = np.array([ 1621.2, 3730.2, 3826.2 ])

    eigenvectors = np.array(
        [
            [
                [ 8.56471748e-06, -5.94970244e-02,  3.35265834e-02],
                [-4.10628901e-01,  4.71790301e-01, -2.60465795e-01],
                [ 4.10469669e-01,  4.71800149e-01, -2.60599649e-01]
            ],

            [
                [ 2.41594971e-05,  4.24369286e-02, -2.45459637e-02],
                [-5.72442674e-01, -3.36594485e-01,  1.90792397e-01],
                [ 5.72052907e-01, -3.36206274e-01,  1.90392535e-01]
            ],

            [
                [-6.72190616e-02,  1.66903211e-05,  9.44855058e-07],
                [ 5.32807198e-01,  3.64839774e-01, -2.06766938e-01],
                [ 5.33440008e-01, -3.65102867e-01,  2.06748196e-01]
            ]
        ]
    )

    neb_initial = {
        'name': 'neb_initial',
        'energies': energies,
        'eigenvalues': eigenvalues,
        'eigenvectors': eigenvectors
    }

    return neb_initial


def neb_image_1():
    energies = np.array([0.19106203, 0.41100502, 0.47297278])

    eigenvalues = np.array([1541, 3315, 3815])

    eigenvectors = np.array(
        [
            [
                [-4.26945336e-02,  3.91986840e-02,  3.70767831e-02],
                [ 6.20996876e-01, -1.86390635e-01, -3.43109063e-02],
                [ 3.21762674e-02, -4.38734267e-01, -5.49404838e-01]
            ],
            [
                [ 5.62393966e-02, -1.17455580e-02,  7.45531317e-03],
                [ 5.20142564e-02,  7.62148073e-02,  1.06409572e-01],
                [-9.34633052e-01,  1.03871938e-01, -1.86077890e-01]
            ],
            [
                [-2.25890013e-02, -3.32915555e-02, -4.68172578e-02],
                [ 2.39631249e-01,  5.57067612e-01,  7.40987116e-01],
                [ 1.18082864e-01, -2.83610436e-02,  5.16927043e-03]
            ]
        ]
    )

    neb_image_1 = {
        'name': 'neb_image_1',
        'energies': energies,
        'eigenvalues': eigenvalues,
        'eigenvectors': eigenvectors
    }

    return neb_image_1


def neb_image_2():
    energies = np.array([0.09384464, 0.11372953, 0.46017361])

    eigenvalues = np.array([757,  917, 3712])

    eigenvectors = np.array(
        [
            [
                [ 7.62506414e-03,  3.58002330e-03,  7.31920931e-03],
                [-2.88073299e-01, -3.67249363e-02,  1.20957433e-01],
                [-5.39087498e-01,  7.74136773e-01, -3.49033477e-02]
            ],
            [
                [-3.15913267e-02, -3.17051730e-04,  1.65307419e-02],
                [ 4.74974378e-02, -8.53604530e-04, -1.40130970e-02],
                [-5.46105806e-02, -5.99654454e-02, -9.81250671e-01]
            ],
            [
                [ 1.89889227e-02,  1.79765477e-02,  5.47099899e-02],
                [-3.07988486e-01, -2.87196062e-01, -8.69667973e-01],
                [ 6.08237432e-03, -5.09274042e-04,  2.28724133e-03]
            ]
        ]
    )

    neb_image_2 = {
        'name': 'neb_image_2',
        'energies': energies,
        'eigenvalues': eigenvalues,
        'eigenvectors': eigenvectors
    }

    return neb_image_2


def neb_image_3():
    energies = np.array([0.13991138, 0.14292389, 0.46372547])

    eigenvalues = np.array([1129, 1153, 3740])

    eigenvectors = np.array(
        [
            [
                [-1.45107114e-03, -1.93291627e-03, -1.87660906e-03],
                [-6.41105966e-03, -3.96436021e-03,  2.50374563e-03],
                [ 4.27515093e-01, -7.90872996e-01, -4.28488668e-01]
            ],
            [
                [ 4.03524056e-04,  1.46113775e-03,  3.97102881e-03],
                [ 1.47099582e-02, -1.87210219e-03, -3.68568550e-03],
                [-4.39699794e-01,  2.29747775e-01, -8.63379010e-01]
            ],
            [
                [ 2.42126960e-02,  2.09155226e-02,  5.16458838e-02],
                [-3.89074887e-01, -3.33887803e-01, -8.18909524e-01],
                [ 2.40858910e-03, -3.48723271e-04,  7.83141625e-04]
            ]
        ]
    )

    neb_image_3 = {
        'name': 'neb_image_3',
        'energies': energies,
        'eigenvalues': eigenvalues,
        'eigenvectors': eigenvectors
    }

    return neb_image_3


def neb_final():
    energies = np.array([ 0.09340425, 0.14384226, 0.46396419 ])

    eigenvalues = np.array([ 753.4, 1160.2, 3742.1 ])

    eigenvectors = np.array(
        [
            [
                [-4.33006917e-03, -2.24828356e-03,  1.25197482e-03],
                [-2.48649372e-02, -1.06173275e-03,  2.08876521e-03],
                [ 5.00238357e-01, -1.00361054e-02, -8.60638076e-01]
            ],

            [
                [-2.93286209e-03, -1.38380953e-03, -1.88368172e-04],
                [-1.00448961e-02, -2.29749336e-04,  1.49625763e-04],
                [ 7.97306041e-01,  3.80653208e-01,  4.59566368e-01]
            ],

            [
                [ 2.75828860e-03,  5.61802353e-04,  6.06518178e-02],
                [-4.66144372e-02, -8.99905682e-03, -9.65036940e-01],
                [-4.65386883e-05, -8.95202027e-05,  1.46542922e-04]
            ]
        ]
    )

    neb_final = {
        'name': 'neb_final',
        'energies': energies,
        'eigenvalues': eigenvalues,
        'eigenvectors': eigenvectors
    }

    return neb_final


def get_system_data(system):
    name = system()['name']
    energy = system()['energies']
    eigenvalue = cm_to_ev(system()['eigenvalues'])
    eigenvector = system()['eigenvectors']
    eigenvectorNorm = [np.linalg.norm(eigenvector) for eigenvector in system()['eigenvectors']]

    return [name, energy, eigenvalue, eigenvector, eigenvectorNorm]


def get_system_data(system):
    name = system()['name']
    energy = system()['energies']
    eigenvalue = cm_to_ev(system()['eigenvalues'])
    eigenvector = system()['eigenvectors']
    eigenvectorNorm = [np.linalg.norm(eigenvector) for eigenvector in system()['eigenvectors']]

    return [name, energy, eigenvalue, eigenvector, eigenvectorNorm]