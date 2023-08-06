#!/usr/bin/env python

import argparse
import json
import logging
import os
import sys

import pysam
import sqlalchemy

def check_readgroup(readgroup_dict, logger):
    if not 'CN' in readgroup_dict:
        logger.info('"CN" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'ID' in readgroup_dict:
        logger.info('"ID" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'LB' in readgroup_dict:
        logger.info('"LB" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'PL' in readgroup_dict:
        logger.info('"PL" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'PU' in readgroup_dict:
        logger.info('"PU" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    if not 'SM' in readgroup_dict:
        logger.info('"SM" is missing from readgroup: %s' % readgroup_dict)
        sys.exit(1)
    # if not 'DT' in readgroup_dict
    return


def extract_readgroup_json(bam_path, engine, logger):
    step_dir = os.getcwd()
    bam_file = os.path.basename(bam_path)
    bam_name, bam_ext = os.path.splitext(bam_file)
    samfile = pysam.AlignmentFile(bam_path, 'rb')
    samfile_header = samfile.header
    readgroup_dict_list = samfile_header['RG']
    if len(readgroup_dict_list) < 1:
        logger.debug('There are no readgroups in BAM: %s' % bam_name)
        logger.debug('\treadgroup: %s' % readgroup_dict_list)
        sys.exit(1)
    else:
        for readgroup_dict in readgroup_dict_list:
            logger.info('readgroup_dict=%s' % readgroup_dict)
            #check_readgroup(readgroup_dict, logger)
            readgroup_json_file = readgroup_dict['ID'] + '.json'
            logger.info('readgroup_json_file=%s\n' % readgroup_json_file)
            with open(readgroup_json_file, 'w') as f:
                json.dump(readgroup_dict, f, ensure_ascii=False)
    return


def setup_logging(args, uuid):
    logging.basicConfig(
        filename=os.path.join(uuid + '.log'),
        level=args.level,
        filemode='w',
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d_%H:%M:%S_%Z',
    )
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    logger = logging.getLogger(__name__)
    return logger


def main():
    parser = argparse.ArgumentParser('convert readgroups to json')

    # Logging flags.
    parser.add_argument('-d', '--debug',
        action = 'store_const',
        const = logging.DEBUG,
        dest = 'level',
        help = 'Enable debug logging.',
    )
    parser.set_defaults(level = logging.INFO)

    # Required flags.
    parser.add_argument('-u', '--uuid',
                         required = True,
                        help = 'analysis_id string',
    )
    parser.add_argument('-b', '--bam_path',
                        required = True,
                        help = 'BAM file.'
    )

    args = parser.parse_args()
    uuid = args.uuid
    bam_path = args.bam_path
    
    logger = setup_logging(args, uuid)

    sqlite_name = uuid + '.db'
    engine_path = 'sqlite:///' + sqlite_name
    engine = sqlalchemy.create_engine(engine_path, isolation_level='SERIALIZABLE')

    extract_readgroup_json(bam_path, engine, logger)
    return

if __name__ == '__main__':
    main()
