# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class MetaHipMer(CMakePackage):
    """
    MetaHipMer (MHM) is a de novo metagenome short-read assembler. This is
    version 2 (MHM2), which is written entirely in UPC++ and runs efficiently
    on both single servers and on multinode supercomputers, where it can scale
    up to coassemble terabase-sized metagenomes.
    """

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
