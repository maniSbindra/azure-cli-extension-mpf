# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_mpf(cmd, resource_group_name, mpf_name, location=None, tags=None):
    raise CLIError('TODO: Implement `mpf create`')


def list_mpf(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `mpf list`')


def update_mpf(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance