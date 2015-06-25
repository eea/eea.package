""" Entry points
"""
import copy

from zopeskel.plone import BasicZope
from zopeskel.base import get_var
from zopeskel.base import EASY, EXPERT
from zopeskel.vars import StringVar

class EEA(BasicZope):
    """ EEA ZopeSkel templates
    """
    _template_dir = 'templates/eea'
    summary = "EEA-based package"
    help = ""
    category = "EEA"
    required_templates = []
    use_local_commands = True
    use_cheetah = True
    variables = copy.deepcopy(BasicZope.vars)
    variables.insert(1, StringVar(
        'title',
        title='Project Title',
        description='Title of the project',
        modes=(EASY, EXPERT),
        default='EEA Dummy Package',
        help="""
        This becomes the title of the project. It is used in the
        GenericSetup registration for the project and, as such, appears
        in Plone's Add/Remove products form.
        """
    ))
    variables.insert(2, StringVar(
        'ctype',
        title='Archetypes Content-Type',
        description='Archetypes Content-Type Class',
        modes=(EASY, EXPERT),
        default='DummyDocument',
        help="This creates an archetypes content-type."
    ))
    variables.insert(3, StringVar(
        'folderish',
        title='Is folderish',
        description='Is this content-type folderish?',
        modes=(EASY, EXPERT),
        default='True',
        help="This creates an archetypes content-type folderish or not"
    ))

    get_var(variables, 'namespace_package').default = 'eea'
    get_var(variables, 'package').default = 'example'
    get_var(variables, 'description').default = 'EEA Package'
    get_var(variables, 'license_name').default = 'GPL version 2'
    get_var(variables, 'author').default = 'European Environment Agency'
    get_var(variables, 'author_email').default = 'webadmin@eea.europa.eu'
    get_var(variables, 'keywords').default = 'eea zope plone python'
    get_var(variables, 'url').default = 'http://eea.github.io'

    def pre(self, command, output_dir, variables):
        """ Pre
        """
        variables['ctype'] = variables['ctype'].title().replace(" ", "")
        variables['ctype_module'] = variables['ctype'].lower()
