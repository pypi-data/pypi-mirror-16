

import os.path
import wayround_org.utils.path
import wayround_org.utils.pkgconfig
import wayround_org.aipsetup.buildtools.autotools as autotools
import wayround_org.aipsetup.builder_scripts.std


class Builder(wayround_org.aipsetup.builder_scripts.std.Builder):

    def builder_action_configure_define_opts(self, called_as, log):
        ret = super().builder_action_configure_define_opts(called_as, log)
        ret += [
            '--without-gtk',
            'CFLAGS=-g -O3 {}'.format(
                wayround_org.utils.pkgconfig.pkgconfig('ncurses', '--cflags')
                )
            ]
        return ret
