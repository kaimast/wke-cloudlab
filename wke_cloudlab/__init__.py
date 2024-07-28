#! /usr/bin/env python3

# pylint: disable=too-many-locals,too-many-arguments

''' Tool to interact with cloudlab and generate wke configs '''

from geni.rspec.pgmanifest import Manifest
from geni.aggregate import cloudlab

from .cloudlab_context import get_context
from .topology import generate_topology
from .extract import generate_config_file

def generate_profile(num_nodes, hardware_type, os_image, outfile='./cloudlab_profile.xml'):
    ''' Creates the XML file that contains a cloudlab profile  '''
    request = generate_topology(num_nodes, hardware_type, os_image)
    request.writeXML(outfile)

    print(f'Wrote new cloudlabe profile configuration to "{outfile}"')

def extract_config(manifest_file, username, workdir=None, outfile='cluster.toml', overwrite=True):
    ''' Creates a wke configuration from an existing cloudlab manifest '''

    manifest = Manifest(path=manifest_file)
    generate_config_file(manifest, username, workdir=workdir, filename=outfile, overwrite=overwrite)

def create_cluster(project, username, certfile, slicename, num_nodes,
                   hardware_type, os_image):
    ''' Creates a cluster on cloudlab and sets up the local wke config to match it
        (currently broken...) '''

    context = get_context(project, username, certfile)
    request = generate_topology(num_nodes, hardware_type, os_image)
    igm = cloudlab.Utah.createsliver(context, slicename, request)

    generate_config_file(igm, username)
