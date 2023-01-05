import os
import h5py as h5
import numpy as np

# map the table filename to the filters associated with it
tables = {
    'Table3' : ['Kepler', 'CoRot', 'Spitzer filter1', 'Spitzer filter2',
                'Spitzer filter3', 'Spitzer filter4'],
    'Table11' : ['u', 'v', 'b', 'y', 'U', 'B', 'V', 'R', 'I', 'J', 'H', 'K'],
    'Table19' : ['Sloan u\'', 'Sloan g\'', 'Sloan r\'', 'Sloan i\'',
                 'Sloan z\'', '2MASS J', '2MASS H', '2MASS Ks']
}

# directories that contain the table files
directories = ['limbdark1/ori', 'limbdark2/ori']

# datatype for quadratic limb darkening parameters (tuple of a and b)
quad = h5.h5t.create(h5.h5t.COMPOUND, 2 * 8)
quad.insert(bytes('a', 'utf-8'), 0, h5.h5t.IEEE_F64LE)
quad.insert(bytes('b', 'utf-8'), 8, h5.h5t.IEEE_F64LE)

# datatype for model parameters
typ = h5.h5t.create(h5.h5t.COMPOUND, 32)
typ.insert(bytes('logg',  'utf-8'),  0, h5.h5t.IEEE_F64LE)
typ.insert(bytes('Teff',  'utf-8'),  8, h5.h5t.IEEE_F64LE)
typ.insert(bytes('logZ',  'utf-8'), 16, h5.h5t.IEEE_F64LE)
typ.insert(bytes('vturb', 'utf-8'), 24, h5.h5t.IEEE_F64LE)

with h5.File('limbdark.h5', 'w') as f:
    grp = f.create_group('quadratic')
    params = None

    for table, filters in tables.items():
        nparams, stride = 4, 5
        nfilters = len(filters)

        a = np.empty((0, nparams + nfilters))
        b = np.empty((0, nparams + nfilters))

        for directory in directories:
            # form the full filename
            f = os.path.join(directory, table)

            # load the tsv data
            dat = np.loadtxt(f, skiprows=1)
            a = np.concatenate((a, dat[0::stride]))
            b = np.concatenate((b, dat[1::stride]))

        if params is None:
            params = a[:,:4]
            # create a parameters dataset exactly once
            dset = grp.create_dataset('params', dtype=typ, shape=(a.shape[0],))
            dset['logg']  = a[:,0]
            dset['Teff']  = a[:,1]
            dset['logZ']  = a[:,2]
            dset['vturb'] = a[:,3]
        else:
            # otherwise, make sure all parameters are identical (they should be)
            assert np.allclose(params, a[:,:4])

        for i, filt in enumerate(filters):
            # add the data for this filter's parameters
            dset = grp.create_dataset(filt, dtype=quad, shape=(a.shape[0],))
            dset['a'] = a[:,nparams+i]
            dset['b'] = b[:,nparams+i]

# vim: set ft=python:
