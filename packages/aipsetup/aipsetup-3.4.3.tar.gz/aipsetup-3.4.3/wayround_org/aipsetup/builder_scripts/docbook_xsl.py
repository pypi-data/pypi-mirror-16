
import logging
import os.path

import wayround_org.aipsetup.build
import wayround_org.utils.archive


def main(buildingsite, action=None):

    ret = 0

    r = wayround_org.aipsetup.build.build_script_wrap(
        buildingsite,
        ['distribute'],
        action,
        "help"
        )

    if not isinstance(r, tuple):
        logging.error("Error")
        ret = r

    else:

        actions = r[1]

        tar_dir = wayround_org.aipsetup.build.getDIR_TARBALL(buildingsite)

        dst_dir = wayround_org.aipsetup.build.getDIR_DESTDIR(buildingsite)

        if 'distribute' in actions and ret == 0:

            zip_file = os.listdir(tar_dir)

            xml_dir = wayround_org.utils.path.join(
                dst_dir,
                'usr',
                'share',
                'xml',
                'docbook'
                )

            if not len(zip_file) == 1:
                ret = 1
                logging.error("tarball file not found")
            else:
                zip_file = zip_file[0]

                os.makedirs(xml_dir)

                wayround_org.utils.archive.extract(
                    wayround_org.utils.path.join(tar_dir, zip_file),
                    xml_dir
                    )

    return ret
