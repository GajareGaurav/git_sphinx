.. a documentation master file, created by
   sphinx-quickstart on Wed Oct 16 17:22:09 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Onetru AI Documentation
========================

Welcome to the **Onetru AI** documentation. This documentation is organized by version, and you can select a version from the dropdown below.

.. note::
   The current version is displayed above. You can select other versions from the dropdown menu.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Version Selector
==================
You can view the documentation for different versions of Onetru AI by selecting a version from the dropdown below.

.. raw:: html

   <div class="rst-versions">
     <span class="rst-current-version">{{ current_version }}</span>
     <div class="rst-other-versions">
       {% for version in versions %}
         <a href="{{ version.url }}">{{ version.name }}</a>
       {% endfor %}
     </div>
   </div>

