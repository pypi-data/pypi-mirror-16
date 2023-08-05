#!/usr/bin/env python

import argparse
import logging
import os
import shutil

from cdis_pipe_utils import pipe_util

def copy_from_list(file_path_list, file_name):
    for file_path in file_path_list:
        if file_name == os.path.basename(file_path):
            shutil.copyfile(file_path, file_name)
    return

def decider(uuid, fastq1_path_list, fastq2_path_list, readgroup_path_list,
            db1_path_list, db2_path_list, logger):
    if fastq1_path_list is None:
        return
    for fastq1_path in fastq1_path_list:
        fastq1_name = os.path.basename(fastq1_path)
        copy_from_list(fastq1_path_list, fastq1_name)
        if fastq1_name.endswith('_1.fq.gz'):
            readgroup_name = fastq1_name.replace('_1.fq.gz', '.json')
            db_name = fastq1_name.replace('_1.fq.gz', '_1.db')
            copy_from_list(readgroup_path_list, readgroup_name)
            copy_from_list(db_path_list, db_name)
        else:
            logger.info('should not be here')
            sys.exit(1)
    for fastq2_path in fastq2_path_list:
        fastq2_name = os.path.basename(fastq2_path)
        db_name = fastq2_name.replace('_2.fq.gz', '_2.db')
        copy_from_list(fastq2_path_list, fastq2_name)
        copy_from_list(db_path_list, db_name)
    return

def main():
    parser = argparse.ArgumentParser('PE bwa decider')

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
                        required = True
    )
    parser.add_argument('-1', '--fastq1_path',
                        action = 'append',
                        required = False
    )
    parser.add_argument('-2', '--fastq2_path',
                        action = 'append',
                        required = False
    )
    parser.add_argument('-r', '--readgroup_path',
                        action = 'append',
                        required = True
    )
    parser.add_argument('--fastqc_db1_path',
                        action = 'append',
                        required = False
    )
    parser.add_argument('--fastqc_db2_path',
                        action = 'append',
                        required = False
    )

    args = parser.parse_args()
    uuid = args.uuid
    fastq1_path_list = args.fastq1_path
    fastq2_path_list = args.fastq2_path
    readgroup_path_list = args.readgroup_path
    db1_path_list = args.fastqc_db1_path
    db2_path_list = args.fastqc_db2_path

    tool_name = 'decider_bwa_pe'
    logger = pipe_util.setup_logging(tool_name, args, uuid)

    hostname = os.uname()[1]
    logger.info('hostname=%s' % hostname)
    
    decider(uuid, fastq1_path_list, fastq2_path_list, readgroup_path_list,
            db1_path_list, db2_path_list, logger)
    
    return


if __name__ == '__main__':
    main()
