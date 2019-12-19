RTDStyle
========

::

    ├───.idea
    │   └───inspectionProfiles
    ├───build
    │   ├───doctrees
    │   └───html
    │       ├───_sources
    │       └───_static
    │           ├───css
    │           ├───fonts
    │           │   ├───Lato
    │           │   └───RobotoSlab
    │           └───js
    ├───exts
    └───source
        ├───_static
        └───_templates


**source/_static中新增一个文件**
style.css
::

    .wy-nav-content {
        max-width: none;
    }

**在source/conf.py中修改配置**
::

    html_css_files = [
    'style.css',]