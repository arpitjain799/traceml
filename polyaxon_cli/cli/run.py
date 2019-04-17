# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import sys

import click

from polyaxon_cli.cli.check import check_polyaxonfile
from polyaxon_cli.cli.getters.project import get_project_or_local
from polyaxon_cli.logger import clean_outputs
from polyaxon_cli.run.conda import run as conda_run
from polyaxon_cli.run.docker import run as docker_run
from polyaxon_cli.run.platform import run as platform_run
from polyaxon_cli.schemas.polyaxonfile import PolyaxonFile
from polyaxon_cli.utils.formatting import Printer
from polyaxon_cli.utils.validation import validate_tags


@click.command()
@click.option('--project', '-p', type=str)
@click.option('--file', '-f', multiple=True, type=click.Path(exists=True),
              help='The polyaxon files to run.')
@click.option('--name', type=str,
              help='Name to give to this run, must be unique within the project, could be none.')
@click.option('--tags', type=str, help='Tags of this run, comma separated values.')
@click.option('--description', type=str,
              help='The description to give to this run.')
@click.option('--ttl', type=int,
              help="TTL for this run after it's done.")
@click.option('--upload', '-u', is_flag=True, default=False,
              help='To upload the repo before running.')
@click.option('--log', '-l', is_flag=True, default=False,
              help='To start logging after scheduling the run.')
@click.option('--local', is_flag=True, default=False,
              help='To start the run locally, with `docker` environment as default.')
@click.option('--conda_env', type=str,
              help='To start a local run with `conda`.')
@click.pass_context
@clean_outputs
def run(ctx,  # pylint:disable=redefined-builtin
        project,
        file,
        name,
        tags,
        description,
        ttl,
        upload,
        log,
        local,
        conda_env):
    """Run polyaxonfile specification.

    Examples:

    \b
    ```bash
    $ polyaxon run -f file -f file_override ...
    ```

    Upload before running

    \b
    ```bash
    $ polyaxon run -f file -u
    ```

    Run and set description and tags for this run

    \b
    ```bash
    $ polyaxon run -f file -u --description="Description of the current run" --tags="foo, bar, moo"
    ```
    Run and set a unique name for this run

    \b
    ```bash
    polyaxon run --name=foo
    ```

    Run for a specific project

    \b
    ```bash
    $ polyaxon run -p project1 -f file.yaml
    ```
    """
    if not file:
        file = PolyaxonFile.check_default_path(path='.')
    if not file:
        file = ''
    specification = check_polyaxonfile(file, log=False).specification

    spec_cond = (specification.is_experiment or
                 specification.is_group or
                 specification.is_job or
                 specification.is_build)
    if not spec_cond:
        Printer.print_error(
            'This command expects an experiment, a group, a job, or a build specification,'
            'received instead a `{}` specification'.format(specification.kind))
        if specification.is_notebook:
            click.echo('Please check "polyaxon notebook --help" to start a notebook.')
        elif specification.is_tensorboard:
            click.echo('Please check: "polyaxon tensorboard --help" to start a tensorboard.')
        sys.exit(1)

    user, project_name = get_project_or_local(project)
    tags = validate_tags(tags)

    if local:
        if conda_env:
            conda_run(ctx=ctx,
                      name=name,
                      project=project,
                      user=user,
                      project_name=project_name,
                      description=description,
                      tags=tags,
                      specification=specification,
                      ttl=ttl,
                      upload=upload,
                      log=log)
        docker_run(ctx=ctx,
                   name=name,
                   project=project,
                   user=user,
                   project_name=project_name,
                   description=description,
                   tags=tags,
                   specification=specification,
                   ttl=ttl,
                   upload=upload,
                   log=log)
    else:
        platform_run(ctx=ctx,
                     name=name,
                     project=project,
                     user=user,
                     project_name=project_name,
                     description=description,
                     tags=tags,
                     specification=specification,
                     ttl=ttl,
                     upload=upload,
                     log=log)
