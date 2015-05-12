# !/usr/bin/env python
###################################################
# fabric-usergroups
# =================
#
# Fabric script to perform user group modifications
###################################################
__author__ = ''
__date__ = ''

import logging
import sys
import os

from fabric.api import *

# Logging Configuration
SCRIPTLOG_LEVEL_NUM = 9
logging.addLevelName(SCRIPTLOG_LEVEL_NUM, "SCRIPTLOG")


def scriptlog(self, message, *args, **kws):
    """ Custom Log level for this script
    :param message: Logged message
    :param args: Args
    :param kws: Kwargs
    :return: A log entry..
    """
    self._log(SCRIPTLOG_LEVEL_NUM, message, args, **kws)

logging.Logger.scriptlog = scriptlog
logging.basicConfig(filename='logfile.log',
                    format='%(message)s')
logger = logging.getLogger(__name__)


# Set Working Directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Create host list
server_file = '/path/to/file'  # List of servers (one hostname per line)
servers = open(server_file, 'r').readlines()
servers = map(lambda s: s.strip(), servers)
env.hosts = servers
# OR.. specify individual servers
#env.hosts = ['server1', 'server2', 'server3']
# Note - You may also pass in hosts via commandline (see fabric docs for -H)

# Connection Settings
env.timeout = 200
env.warn_only = True
env.skip_bad_hosts = True
env.eagerly_disconnect = True


@task
def addgrp(user=None, grp=None):
    """ Adds a user to a give group name
    :param user: user to add to group
    :param grp: group name to add user to
    :return: log of servers and success/fail message for the group add command
    """
    if not grp:
        print("No group name provided.. exiting.")
        sys.exit()
    logger.scriptlog("\n%s" % env.host)
    addgroup = sudo("groupadd %s" % grp)
    if addgroup.return_code == 0:
        logger.scriptlog("Group added %s" % grp)
    elif addgroup.return_code == 9:
        logger.scriptlog("Group already exists: %s" % grp)
    else:
        logger.scriptlog("An error occured while adding group: %s" % grp)
    try:
        sudo("usermod -aG %s %s" % (grp, user))
        logger.scriptlog("Added %s to group: %s" % (user, grp))
    except Exception as e:
        logger.error(e)


@task
def chkgrp(user=None):
    """ Checks the groups a specified user belongs on all servers
    :param user: username to query
    :return: log of server names with the groups which the user belongs to
    """
    if not user:
        print("No user given.. exiting.")
        sys.exit()
    logger.scriptlog("\n%s" % env.host)
    groups = run("cat /etc/group | grep -i %s" % user)
    if groups.return_code == 1:
        logger.scriptlog("no groups assigned for %s." % user)
    else:
        groups = groups.split('\r')
        groups = map(lambda g: g.split(':', 1)[0].strip('\n'), groups)
        if groups:
            logger.scriptlog("%s's groups: " % user + " ".join(groups))


@task
def remgrp(user=None, exceptgrp=None):
    """ Removes a user from all groups
    :param user: username of which to remove group membership
    :param exceptgrp: single group that the user is allowed membership
    :return: log of servers and the following group membership modifications
    """
    if not user:
        print("No user given.. exiting.")
        sys.exit()
    logger.scriptlog("\n%s's groups on %s" % (user, env.host))
    groups = run("cat /etc/group | grep -i %s" % user)
    if groups.return_code == 1:
        logger.scriptlog("no groups assigned.")
    else:
        groups = groups.split('\r')
        groups = map(lambda g: g.split(':', 1)[0].strip('\n'), groups)
        logger.scriptlog("%s's groups: " % user + " ".join(groups))
        if exceptgrp:
            for group in groups:
                if group == exceptgrp:
                    pass
                else:
                    try:
                        sudo("gpasswd -d %s %s" % (user, group))
                        logger.scriptlog("removed from: %s" % group)
                    except Exception as e:
                        logger.error(e)
        else:
            for group in groups:
                try:
                    sudo("gpasswd -d %s %s" % (user, group))
                    logger.scriptlog("removed from: %s" % group)
                except Exception as e:
                    logger.error(e)
