# pylint: disable=missing-module-docstring

from .config import get_defaults

def generate_config_file(manifest, username, workdir=None, filename="cluster.toml", overwrite=True):
    ''' Creates a wke cluster configuration from a cloudlab manifest file '''

    print(f'📝 Generating config file "{filename}"')

    defaults = get_defaults()

    if overwrite:
        flags = 'w'
    else:
        flags = 'x'

    with open(filename, flags, encoding='utf-8') as config_file:
        config_file.write((
            f'# Automatically generated; do not modify directly\n'
            f'\n'
            f'[cluster]\n'
            f'username="{username}"\n'
        ))

        if workdir is None:
            workdir = defaults["workdir"]

        if workdir:
            config_file.write(f'workdir="{workdir}"\n')

        config_file.write('\n[machines]\n')

        if manifest.nodes is None or len(manifest.nodes) == 0:
            raise RuntimeError("No nodes in manifest")


        for machine in manifest.nodes:
            if len(machine.interfaces) != 1:
                raise RuntimeError("Each machine needs exactly one interface")

            external = machine.hostipv4
            internal = machine.interfaces[0].address_info[0]
            machine_id = machine.name

            print(f'\tAddress of "{machine_id}" is "{external}" and "{internal}"')
            config_file.write((
                f'{machine_id} = {{ external_addr="{external}", '
                f'internal_addr="{internal}" }}\n'
            ))
