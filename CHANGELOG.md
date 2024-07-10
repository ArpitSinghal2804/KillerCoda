# Yellow belt Stripe 1 scenarios

All notable changes to this repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- see https://github.dxc.com/Platform-DXC/release-pipeline/blob/master/docs/CHANGE.md for details on creating the log -->
<!-- Keywords:
 ADDED - Introduction of a new feature or aspect that did not previously exist.
 CHANGED - Enhancement or change to an existing feature.
 FIXED - Fixing of an existing bug without changing functionality.·
 SECURITY - Relating to any security enhancement, closure of vulnerability, etc.
 PERFORMANCE - Performance enhancement, that doesn't explicitly change functionality.
 DOCUMENTATION - A documentation only change·
 PIPELINE - A change to a component's own CI/CD pipeline
 KNOWNISSUE - A known issue impacting functionality or performance as a part of the release.
 -->

## [UNRELEASED]

## [1.0.2] - 2020-06-22

- [FIXED] Fix default email in prepare.sh when no email is associated to the GitHub account.
- [PIPELINE] Change JSON lint stage using [sahsu/docker-jsonlint](https://hub.docker.com/r/sahsu/docker-jsonlint). Check all JSON files and report the number of files in error.
- [PIPELINE] Change YAML lint stage using [cytopia/yamllint](https://hub.docker.com/r/cytopia/yamllint).

## [1.0.1] - 2020-04-10

- [DOCUMENTATION] Replace @ by / to invoke the bot.

## [1.0.0] - 2020-03-09

- [DOCUMENTATION] Add CHANGELOG
- [FIXED] Variable initialization error in `github-issues.py`
- [PIPELINE] Change pylint stage using [cytopia/pylint:latest](https://hub.docker.com/r/cytopia/pylint) and report for python 3.
