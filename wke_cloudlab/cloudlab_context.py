#pylint: disable=missing-module-docstring

from geni.aggregate import FrameworkRegistry
from geni.aggregate.context import Context
from geni.aggregate.user import User

def get_context(project, username, certfile):
    '''
    Creates the cloudlab context from the specified project, usernamel,
    and certificate file
    '''

    framework = FrameworkRegistry.get("portal")()
    framework.cert = certfile
    framework.key = certfile

    user = User()
    user.name = username
    user.urn = f"URI:urn:publicid:IDN+emulab.net+user+{username}"
    user.addKey(f"/home/{username}/.ssh/cloudlab.pub")

    context = Context()
    context.addUser(user)
    context.cf = framework
    context.project = project

    return context
