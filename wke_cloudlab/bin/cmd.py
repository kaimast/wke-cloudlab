'''
Command line interface for wke-cloudlab
'''

import logging
import argparse

from wke_cloudlab import create_cluster, generate_profile, extract_config
from wke_cloudlab.config import get_defaults

def _create_cluster(args):
    create_cluster(args.project, args.username, args.certfile, args.slicename,
                   args.num_nodes, args.hardware_type, args.os_image)

def _generate_profile(args):
    generate_profile(args.num_nodes, args.hardware_type, args.os_image,
                 outfile=args.outfile)

def _extract_config(args):
    extract_config(args.manifest_file, args.username, outfile=args.outfile,
                    overwrite=args.overwrite, workdir=args.workdir)

def main():
    ''' Main function for the wke-cloudlab command '''

    logging.basicConfig(level=logging.DEBUG)
    formatter=argparse.ArgumentDefaultsHelpFormatter

    parser = argparse.ArgumentParser(description='update the cluster config',
        formatter_class=formatter)
    subparsers = parser.add_subparsers(dest="command", required=True)

    defaults = get_defaults()

    create_cluster_args = subparsers.add_parser('create-cluster',
        help='Will create a new cluster on cloudlab and create a wke config file for it',
       formatter_class=formatter)
    create_cluster_args.add_argument('--num-nodes', required=True, type=int)
    create_cluster_args.add_argument('--certfile', type=str, required=True)
    create_cluster_args.add_argument('--hardware-type', default=defaults["hardware-type"],
        type=str, help="What type of hardware to use for nodes in the cluster?")
    create_cluster_args.add_argument('--os-image', default=defaults["os-image"], type=str,
        help="What OS to use for nodes in the cluster?")
    if defaults["username"] is not None:
        create_cluster_args.add_argument('--username', default=defaults["username"],
            type=str, help="The cloudlab username")
    else:
        create_cluster_args.add_argument('--username', required=True, type=str,
            help="The cloudlab username")
    create_cluster_args.set_defaults(func=_create_cluster,
        formatter_class=formatter)

    generate_profile_args = subparsers.add_parser('generate-profile',
        help="Creates a cloudlab profile and store it as an XML file")
    generate_profile_args.add_argument('--num-nodes', required=True, type=int,
        help="How many nodes should the topology contain?")
    generate_profile_args.add_argument('--hardware-type', default=defaults["hardware-type"],
       type=str, help="What type of hardware to use for nodes in the topology?")
    generate_profile_args.add_argument('--os-image', default=defaults["os-image"], type=str,
       help="What OS to use for nodes in the topology?")
    generate_profile_args.add_argument('--outfile', default='./cloudlab_profile.xml', type=str,
       help="What file should the Cloudlab profile be written to?")
    generate_profile_args.set_defaults(func=_generate_profile)

    extract_config_args = subparsers.add_parser('extract-config',
        help="Create a wke configuration from a cloudlab manifest",
        formatter_class=formatter)
    extract_config_args.add_argument('manifest_file', type=str,
        help="The location of the manifest XML file")
    extract_config_args.add_argument('--outfile', type=str, default='cluster.toml',
        help="The path the new cluster configuration should be written to")
    extract_config_args.add_argument('--workdir', type=str,
        help="The default working directory for nodes on this cluster")
    extract_config_args.add_argument('--overwrite', default='True',
        help="Should the existing configuration be overwritten?")
    if defaults["username"] is not None:
        extract_config_args.add_argument('--username', default=defaults["username"],
            type=str, help="The cloudlab username")
    else:
        extract_config_args.add_argument('--username', required=True, type=str,
            help="The cloudlab username")
    extract_config_args.set_defaults(func=_extract_config)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
