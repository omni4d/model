#!/usr/bin/env python

# This script is intended to be used a a git hook and will prepend the ticket
# number to a commit message in the correct format for Gitlab to parse.
#
# To use, create a shortcut to this file in .git/hooks called
# 'prepare-commit-msg' e.g. from top folder of your project:
#     mkdir .git/hooks
#     cd .git/hooks
#     ln -s ./prepare-commit-msg.py prepare-commit-msg

import sys
import re
from subprocess import check_output

# Collect the parameters
commit_msg_filepath = sys.argv[1]
if len(sys.argv) > 2:
    commit_type = sys.argv[2]
else:
    commit_type = ''
if len(sys.argv) > 3:
    commit_hash = sys.argv[3]
else:
    commit_hash = ''

# Figure out which branch we're on
branch = check_output(
    ['git', 'symbolic-ref', '--short', 'HEAD']
).strip().decode(encoding='UTF-8')

print("prepare-commit-msg: On branch '%s'" % branch)

# Populate the commit message with the issue #, if there is one
if branch.startswith('ticket-'):
    print("prepare-commit-msg: It's a ticket branch.")
    result = re.match('ticket-(.*)', branch)
    issue_number = result.group(1)

    with open(commit_msg_filepath, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write("[#%s] %s" % (issue_number, content))
