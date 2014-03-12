### Description

This script calculates and prints the latest version from the 
`maven-metadata.xml`  file passed as a commandline param.

It does not work correctly when comparing `0.10` to `0.10-SNAPSHOT` version
but you are not likely to hit this and otherwise it should work correctly.

*In maven versioning scheme `0.10 > 0.10-SNAPSHOT` (contrary to the whole
other world) but you don't (and can't) store both SNAPSHOT and non-SNAPSHOT 
versions in the same Nexus repository.*

### Background

Nexus does not set LATEST version for the artifact, you need to do it yourself
when uploading the artifact.
Otherwise you can use this script to calculate the LATEST versions from all 
versions stored in the repository.
