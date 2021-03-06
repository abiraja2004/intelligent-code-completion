##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Gnupg(AutotoolsPackage):
    """GnuPG is a complete and free implementation of the OpenPGP
       standard as defined by RFC4880 """

    homepage = "https://gnupg.org/index.html"
    url = "https://gnupg.org/ftp/gcrypt/gnupg/gnupg-2.1.21.tar.bz2"

    version('2.1.21', '685ebf4c3a7134ba0209c96b18b2f064')

    depends_on('libgcrypt')
    depends_on('libassuan')
    depends_on('libksba')
    depends_on('libgpg-error')
    depends_on('npth')

    def configure_args(self):
        args = ['--with-npth-prefix=%s' % self.spec['npth'].prefix,
                '--with-libgcrypt-prefix=%s' % self.spec['libgcrypt'].prefix,
                '--with-libksba-prefixx=%s' % self.spec['libksba'].prefix,
                '--with-libassuan-prefix=%s' % self.spec['libassuan'].prefix,
                '--with-libpgp-error-prefix=%s' %
                self.spec['libgpg-error'].prefix]
        return args
