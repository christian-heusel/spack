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
#     spack install meta-hip-mer
#
# You can edit this file again by typing:
#
#     spack edit meta-hip-mer
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class MetaHipMer(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://bitbucket.org/berkeleylab/mhm2/src/e674623ebeb52bb0b0e8dbb979ba51aef0ddaa93/docs/mhm_guide.md"
    url = "https://bitbucket.org/berkeleylab/mhm2/downloads/mhm2-2.0.0.tar.gz"

    maintainers = ['christian-heusel', 'DieGoldeneEnte']

    version(
        '2.0.0',
        'd0603a916a25069bb4171fbe8723f78bb9024d9f4a296d8025902e88ad2a14a0')

    depends_on('upcxx')

    def cmake_args(self):
        args = []

        build = Executable("./build.sh")
        build("Release")
        return args

    def install(self, spec, prefix):
        make()
        make('install')
