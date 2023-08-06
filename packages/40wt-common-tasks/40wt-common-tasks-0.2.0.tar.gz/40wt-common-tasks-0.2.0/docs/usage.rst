=====
Usage
=====

To use 40wt-common-tasks in a project, add something like that in your ``tasks.py`` file:

.. code:: python

  from common_tasks import (
      check_is_dirty,
      make_dashed_aliases,
      update_requirements,
  )

  @task(check_is_dirty)
  def build_release(ctx):
      do_something_clever()

  make_dashed_aliases(locals().values())

After that, you'll be able to run::

  invoke build-release

And it will fail if there is some not commited or not pushed changes in the work directory.
