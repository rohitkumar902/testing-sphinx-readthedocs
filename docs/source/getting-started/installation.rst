Installation
============

Install the test package via pip

.. code-block:: bash

   pip install git+https://github.com/youruser/yourrepo.git

Detailed Instructions
---------------------

This guide provides a deep dive into setting up your local environment and 
contributing to the Project YOUVA documentation.

Phase 1: Environment Setup
--------------------------

Before you begin, ensure you have Python 3.8 or higher installed. It is 
strongly recommended to use a virtual environment to avoid dependency conflicts.

1. **Create a Virtual Environment**
   
   Navigate to your project root and run:
   
   .. code-block:: bash

      python -m venv venv

2. **Activate the Environment**

   * **Windows:** ``.\venv\Scripts\activate``
   * **Linux/macOS:** ``source venv/bin/activate``

3. **Install Dependencies**

   Use the command you verified earlier:

   .. code-block:: bash

      pip install sphinx furo

Phase 2: Building Locally
-------------------------

To see your changes before pushing to GitHub and triggering a Read the Docs build, 
you should build the HTML locally.

.. tip::
   Always run a "clean" build if you make significant changes to the folder structure.

Step-by-Step Build:
~~~~~~~~~~~~~~~~~~~

1. Navigate to the directory containing your ``conf.py``.
2. Run the Sphinx build command:

   .. code-block:: bash

      sphinx-build -b html . _build/html

3. Open ``_build/html/index.html`` in your preferred web browser.

Phase 3: Configuring Read the Docs
----------------------------------

Once your local build looks correct, you must connect your repository to 
Read the Docs (RTD).

1. **Create a .readthedocs.yaml file:** This file tells RTD which version of 
   Python to use and which requirements to install.
2. **Webhook Integration:** Ensure your GitHub repository has the RTD 
   webhook active so that every ``git push`` triggers a new build.
3. **Advanced Settings:** In the RTD dashboard, ensure the "Documentation Type" 
   is set to "Sphinx Html".

Troubleshooting
---------------

If your build fails on Read the Docs but works locally, check the following:

* **Path Issues:** Ensure your ``sys.path`` in ``conf.py`` points correctly to your source code.
* **Missing Requirements:** Ensure ``furo`` is listed in your ``requirements.txt`` 
  or your ``.readthedocs.yaml`` file.