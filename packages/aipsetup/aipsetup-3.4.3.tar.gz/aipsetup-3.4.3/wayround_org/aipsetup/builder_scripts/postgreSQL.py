

import os.path
import wayround_org.utils.path
import wayround_org.aipsetup.buildtools.autotools as autotools
import wayround_org.aipsetup.builder_scripts.std


class Builder(wayround_org.aipsetup.builder_scripts.std.Builder):

    def builder_action_configure_define_opts(self, called_as, log):
        return super().builder_action_configure_define_opts(called_as, log) + [
            '--with-tcl',
            '--with-tclconfig={}'.format(
                wayround_org.utils.path.join(
                    self.calculate_install_prefix(),
                    'lib'
                    )
                ),
            '--with-perl',
            '--with-python',
            '--with-openssl',
            '--with-libxml',
            '--with-libxslt',
            ]
