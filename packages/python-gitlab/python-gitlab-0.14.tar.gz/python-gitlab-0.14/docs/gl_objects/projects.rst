########
Projects
########

Use :class:`~gitlab.objects.Project` objects to manipulate projects. The
:attr:`gitlab.Gitlab.projects` manager objects provides helper functions.

Examples
========

List projects:

The API provides several filtering parameters for the listing methods:

* ``archived``: if ``True`` only archived projects will be returned
* ``visibility``: returns only projects with the specified visibility (can be
  ``public``, ``internal`` or ``private``)
* ``search``: returns project matching the given pattern

Results can also be sorted using the following parameters:

* ``order_by``: sort using the given argument. Valid values are ``id``,
  ``name``, ``path``, ``created_at``, ``updated_at`` and ``last_activity_at``.
  The default is to sort by ``created_at``
* ``sort``: sort order (``asc`` or ``desc``)

.. literalinclude:: projects.py
   :start-after: # list
   :end-before: # end list

Get a single project:

.. literalinclude:: projects.py
   :start-after: # get
   :end-before: # end get

Create a project:

.. literalinclude:: projects.py
   :start-after: # create
   :end-before: # end create

Create a project for a user (admin only):

.. literalinclude:: projects.py
   :start-after: # user create
   :end-before: # end user create

Update a project:

.. literalinclude:: projects.py
   :start-after: # update
   :end-before: # end update

Delete a project:

.. literalinclude:: projects.py
   :start-after: # delete
   :end-before: # end delete

Fork a project:

.. literalinclude:: projects.py
   :start-after: # fork
   :end-before: # end fork

Create/delete a fork relation between projects (requires admin permissions):

.. literalinclude:: projects.py
   :start-after: # forkrelation
   :end-before: # end forkrelation

Star/unstar a project:

.. literalinclude:: projects.py
   :start-after: # star
   :end-before: # end star

Archive/unarchive a project:

.. literalinclude:: projects.py
   :start-after: # archive
   :end-before: # end archive

.. note::

   The underscore character at the end of the methods is used to workaround a
   conflict with a previous misuse of the ``archive`` method (deprecated but
   not yet removed).

Events
------

Use :class:`~gitlab.objects.ProjectEvent` objects to manipulate events. The
:attr:`gitlab.Gitlab.project_events` and :attr:`Project.events
<gitlab.objects.Project.events>` manager objects provide helper functions.

List the project events:

.. literalinclude:: projects.py
   :start-after: # events list
   :end-before: # end events list

Team members
------------

Use :class:`~gitlab.objects.ProjectMember` objects to manipulate projects
members. The :attr:`gitlab.Gitlab.project_members` and :attr:`Project.members
<gitlab.objects.Projects.members>` manager objects provide helper functions.

List the project members:

.. literalinclude:: projects.py
   :start-after: # members list
   :end-before: # end members list

Search project members matching a query string:

.. literalinclude:: projects.py
   :start-after: # members search
   :end-before: # end members search

Get a single project member:

.. literalinclude:: projects.py
   :start-after: # members get
   :end-before: # end members get

Add a project member:

.. literalinclude:: projects.py
   :start-after: # members add
   :end-before: # end members add

Modify a project member (change the access level):

.. literalinclude:: projects.py
   :start-after: # members update
   :end-before: # end members update

Remove a member from the project team:

.. literalinclude:: projects.py
   :start-after: # members delete
   :end-before: # end members delete

Share the project with a group:

.. literalinclude:: projects.py
   :start-after: # share
   :end-before: # end share

Hooks
-----

Use :class:`~gitlab.objects.ProjectHook` objects to manipulate projects
hooks. The :attr:`gitlab.Gitlab.project_hooks` and :attr:`Project.hooks
<gitlab.objects.Projects.hooks>` manager objects provide helper functions.

List the project hooks:

.. literalinclude:: projects.py
   :start-after: # hook list
   :end-before: # end hook list

Get a project hook

.. literalinclude:: projects.py
   :start-after: # hook get
   :end-before: # end hook get

Create a project hook:

.. literalinclude:: projects.py
   :start-after: # hook create
   :end-before: # end hook create

Update a project hook:

.. literalinclude:: projects.py
   :start-after: # hook update
   :end-before: # end hook update

Delete a project hook:

.. literalinclude:: projects.py
   :start-after: # hook delete
   :end-before: # end hook delete
