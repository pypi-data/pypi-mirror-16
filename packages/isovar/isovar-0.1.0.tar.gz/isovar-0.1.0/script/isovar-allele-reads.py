#!/usr/bin/env python

# Copyright (c) 2016. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Prints names and sequences of reads overlapping a given set of variants.
"""

from __future__ import print_function, division, absolute_import

from isovar.args.rna_reads import (
    make_rna_reads_arg_parser,
    allele_reads_dataframe_from_args
)

parser = make_rna_reads_arg_parser()
parser.add_argument(
    "--output",
    default="isovar-allele-reads-result.csv",
    help="Name of CSV file which contains overlapping read sequences")

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    df = allele_reads_dataframe_from_args(args)
    print(df)
    df.to_csv(args.output)
