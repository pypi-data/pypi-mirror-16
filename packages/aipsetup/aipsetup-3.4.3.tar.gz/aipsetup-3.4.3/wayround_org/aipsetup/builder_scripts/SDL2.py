
import logging
import os.path

import wayround_org.aipsetup.build
import wayround_org.aipsetup.buildtools.autotools as autotools
import wayround_org.utils.file

import wayround_org.aipsetup.builder_scripts.std_cmake


class Builder(wayround_org.aipsetup.builder_scripts.std_cmake.Builder):

    def builder_action_configure_define_opts(self, called_as, log):
        return super().builder_action_configure_define_opts(called_as, log) + [
            '-DPULSEAUDIO=ON',
            '-DPULSEAUDIO_SHARED=ON',
            '-DALSA=OFF',
            '-DALSA_SHARED=OFF',
            ]
