# Copyright (C) 2015-2016 Regents of the University of California
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

"""Kills any running jobs trees in a rogue toil.
"""
from __future__ import absolute_import
import logging

from toil.lib.bioio import getBasicOptionParser
from toil.lib.bioio import parseBasicOptions
from toil.common import Toil
from toil.version import version

logger = logging.getLogger( __name__ )

def main():
    parser = getBasicOptionParser()

    parser.add_argument("jobStore", type=str,
              help=("Store in which to place job management files \
              and the global accessed temporary files"
              "(If this is a file path this needs to be globally accessible "
              "by all machines running jobs).\n"
              "If the store already exists and restart is false an"
              " JobStoreCreationException exception will be thrown."))
    parser.add_argument("--version", action='version', version=version)
    options = parseBasicOptions(parser)

    jobStore = Toil.loadOrCreateJobStore(options.jobStore)
    
    logger.info("Starting routine to kill running jobs in the toil workflow: %s" % options.jobStore)
    ####This behaviour is now broken
    batchSystem = Toil.createBatchSystem(jobStore.config) #This should automatically kill the existing jobs.. so we're good.
    for jobID in batchSystem.getIssuedBatchJobIDs(): #Just in case we do it again.
        batchSystem.killBatchJobs(jobID)
    logger.info("All jobs SHOULD have been killed")

def _test():
    import doctest
    return doctest.testmod()
