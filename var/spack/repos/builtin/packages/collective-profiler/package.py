# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install collective-profiler
#
# You can edit this file again by typing:
#
#     spack edit collective-profiler
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class CollectiveProfiler(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/gvallee/collective_profiler"
    url      = "https://github.com/gvallee/collective_profiler/archive/refs/tags/ISC21_cc_v1.zip"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('21_cc_v1', sha256='941760343b39543e9d11fa821d928f51bebd258dfde46624cee850121037faea')

    # FIXME: Add dependencies if required.
    depends_on('go')
    depends_on('mpi')

    def install(self, spec, prefix):
        mkdirp(self.prefix.lib)

        install('src/alltoallv/liballtoallv_counts.so', self.prefix.lib)
        install('src/alltoallv/liballtoallv_exec_timings.so', self.prefix.lib)
        install('src/alltoallv/liballtoallv_late_arrival.so', self.prefix.lib)
        install('src/alltoallv/liballtoallv_backtrace.so', self.prefix.lib)
        install('src/alltoallv/liballtoallv_location.so', self.prefix.lib)
        install('src/alltoallv/liballtoallv.so', self.prefix.lib)
