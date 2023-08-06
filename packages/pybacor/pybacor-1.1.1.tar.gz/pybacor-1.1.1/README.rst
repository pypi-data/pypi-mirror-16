=======
Pybacor
=======

Ibacor API for Python. Check `PyPI <https://pypi.python.org/pypi/pybacor/1.1.0>`_ .

Installing
^^^^^^^^^^

To install, type::
	
	pip install pybacor


KTP API Pybacor
^^^^^^^^^^^^^^^

for now, only available ktp.

To use (with caution), simply do::

    >>> from pybacor import ktp
    >>> data  = ktp.IbacorKTP('xxxx02150791xxxx')
    >>> data.nama
    'marzuki'

status is true when the data is found::

	>>> data.status
	True

You can access a common field for ktp::
	
	>>> data.nik
	'3173021507910004'
	>>> data.nama
	'marzuki'
	>>> data.kelamin
	'laki-laki'
	>>> data.kelurahan
	'tanjung duren selatan'
	>>> data.kecamatan
	'grogol petamburan'
	>>> data.kota
	'jakarta barat'
	>>> data.provinsi
	'dki jakarta'
	>>>


