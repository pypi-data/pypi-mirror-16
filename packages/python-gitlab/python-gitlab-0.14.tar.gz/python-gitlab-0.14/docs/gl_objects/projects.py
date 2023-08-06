# list
# Active projects
projects = gl.projects.list()
# Archived projects
projects = gl.projects.list(archived=1)
# Limit to projects with a defined visibility
projects = gl.projects.list(visibility='public')

# List owned projects
projects = gl.projects.owned()

# List starred projects
projects = gl.projects.starred()

# List all the projects
projects = gl.projects.all()

# Search projects
projects = gl.projects.search('query')
# end list

# get
# Get a project by ID
project = gl.projects.get(10)
# Get a project by userspace/name
project = gl.projects.get('myteam/myproject')
# end get

# create
project = gl.projects.create({'name': 'project1'})
# end create

# user create
alice gl.users.list(username='alice')[0]
user_project = gl.user_projects.create({'name': 'project',
                                        'user_id': alice.id})
# end user create

# update
project.snippets_enabled = 1
project.save()
# end update

# delete
gl.projects.delete(1)
# or
project.delete()
# end delete

# fork
fork = gl.project_forks.create(project_id=1)
# or
fork = project.fork()
# end fork

# forkrelation
project.create_fork_relation(source_project.id)
project.delete_fork_relation()
# end forkrelation

# star
project.star()
project.unstar()
# end star

# archive
project.archive_()
project.unarchive_()
# end archive

# events list
gl.project_events.list(project_id=1)
# or
project.events.list()
# end events list

# members list
members = gl.project_members.list()
# or
members = project.members.list()
# end members list

# members search
members = gl.project_members.list(query='foo')
# or
members = project.members.list(query='bar')
# end members search

# members get
member = gl.project_members.get(1)
# or
member = project.members.get(1)
# end members get

# members add
member = gl.project_members.create({'user_id': user.id, 'access_level':
                                    gitlab.Group.DEVELOPER_ACCESS},
                                   project_id=1)
# or
member = project.members.create({'user_id': user.id, 'access_level':
                                 gitlab.Group.DEVELOPER_ACCESS})
# end members add

# members update
member.access_level = gitlab.Group.MASTER_ACCESS
member.save()
# end members update

# members delete
gl.project_members.delete(user.id, project_id=1)
# or
project.members.delete(user.id)
# or
member.delete()
# end members delete

# share
project.share(group.id, group.DEVELOPER_ACCESS)
# end share

# hook list
hooks = gl.project_hooks.list(project_id=1)
# or
hooks = project.hooks.list()
# end hook list

# hook get
hook = gl.project_hooks.get(1, project_id=1)
# or
hook = project.hooks.get(1)
# end hook get

# hook create
hook = gl.project_hooks.create({'url': 'http://my/action/url',
                                'push_events': 1},
                               project_id=1)
# or
hook = project.hooks.create({'url': 'http://my/action/url', 'push_events': 1})
# end hook create

# hook update
hook.push_events = 0
hook.save()
# end hook update

# hook delete
gl.project_hooks.delete(1, project_id=1)
# or
project.hooks.delete(1)
# or
hook.delete()
# end hook delete
