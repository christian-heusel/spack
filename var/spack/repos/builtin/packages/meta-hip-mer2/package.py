# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class MetaHipMer2(CMakePackage):
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

    variant('build_type',
            default='Release',
            description='The build type to build',
            values=('Debug', 'Release', 'DebugRelease'))

    variant('mpi', default=True,
            description='Enables MPI')

    depends_on('upcxx+mpi', when='+mpi')
    depends_on('upcxx~mpi', when='~mpi')
    depends_on('zlib')
    depends_on('mpi', when='+mpi')

    # TODO fix upstream
    def patch(self):
        filter_file(
                'ZLIB_INCLUDE_DIRECTORIES',
                'ZLIB_INCLUDE_DIRS',
                'CMakeLists.txt')

    def setup_build_environment(self, env):
        # TODO: Make this configurable via variant
        env.set('UPCXX_CODEMODE', "O3")
        env.set('UPCXX_THREADMODE', "par")

    def cmake_args(self):
        # This seems to be necessary since the cmake file is not happy with
        # spacks env system:
        #
        # UPCXX compiler provided by upcxx-meta CXX:
        #   /usr/bin/g++ ->
        #   /usr/bin/x86_64-linux-gnu-g++-10
        # is different from CMAKE_CXX_COMPILER:
        #   $SPACK_ROOT/spack/lib/spack/env/gcc/g++ ->
        #   $SPACK_ROOT/spack/lib/spack/env/cc
        upcxx_meta = Executable("upcxx-meta")
        args = [
            self.define("CMAKE_CXX_COMPILER",
                        upcxx_meta("CXX", output=str).strip())
        ]

        return args
