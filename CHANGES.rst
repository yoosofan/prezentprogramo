Prezentprogramo
===============
3.2 (2025/10/04)
----------------
* Fix convert to pdf

3.1 (2025/08/16)
-----------------
* Replace setup.cfg by pyproject.toml
* update impress.js to fix substep

Changes
=======
* fontURL:"js/output/chtml/fonts/tex-woff-v2"
* fontURL:n.Package.resolvePath("output/chtml/fonts/woff-v2"
* ("output/chtml/fonts/tex"

1.0 (2023/10/23)
----------------
- Update impress.js to newer version by
- Update xsl to support data-with
- Rename the application and test by Ahmad Yoosofan

Changing Name
=============
2025/08/19 08:53:17
-------------------
"prezentprogramo" is suggested by AI tools and it also used in the following website

* https://topkeyshop.com/eo/produkto-kategorio/office/
* https://www.eventoj.hu/steb/miksitaj/kaest-1998.pdf
* https://easyshiksha.com/eo/retaj_kursoj/la-kompleta-google-lumbildoj-majstra-klaso-majstro-google-lumbildoj
* https://morningdough.com/eo/google-drive/what-is-google-slides/

Prezentilo 
----------
LibreOffice uses the term "Prezentilo" for LibreOffice Impress.
Therefore, it is better to change the name of the project to "Prezentilo"
instead of "Bildumilo".

* https://help.libreoffice.org/latest/eo/text/simpress/main0503.html
* https://wiki.documentfoundation.org/Faq/Impress/050/eo
* https://help.collaboraoffice.com/latest/eo/text/simpress/04/01020000.html?DbPAR=IMPRESS
* https://eo.wikipedia.org/wiki/Bildumilo
* https://github.com/LaPingvino/komputeko-data-malnova/blob/master/komputeko.tsv
      * presentation program (Powerpoint, Impress) (subst.)
      * lumbilda prezentilo         bildumilo
* https://help.libreoffice.org/latest/eo/text/shared/guide/dev_tools.html?&DbPAR=CALC&System=UNIX

prezentprogramo


2023 opinions
-------------
"bildumilo" was chosen at that time.

https://clig.dev/#introduction

esperanto "bildumilo"  "prezentilo"

https://eo.wikipedia.org/wiki/Bildumilo

Bildumilo aŭ prezentilo aŭ prezentadprogramo estas komputila programaro, per kiu oni povas prezenti serion de bildoj.

Specoj
Plej simplaj bildumiloj prezentas nur pretajn bildojn. Ekzemple ili surekranigas enkomputiligitajn fotojn laŭ konstanta ritmo, eventuale adaptatante ilin al la grando de la ekrano, korektante kolorojn, kaj tiel plu.

Pli ampleksaj prezentadprogramoj ne nur enprenas bildojn, sed ebligas ilin krei. Ili disponigas internan sortimenton de figuroj (ortanguloj, elipsoj, sagoj, desegnetoj de diversaj objektoj), per kies kunmeto la uzanto preparas siajn bildojn.

Uzo
La bildojn oni povas vidi sur la komputila ekrano mem. Per videoprojekciilo oni povas ilin montri sur granda ekrano aŭ blanka muro. En ĉi lasta maniero la bildumiloj ofte estas uzataj en kompanioj aŭ en aliaj cirkonstancoj por akompano de prelegoj.

Ekzemploj
Programoj nur montraj:

IrfanView
Programoj ankaŭ redaktaj:

LibreOffice Impress — PowerPoint — Visio


Prezenta Aplikaĵo
I wanted to use Esperanto or alike for naming the project.

prezento
presentation

prezentaj lumbildoj
presentation slides

slide generator
glita generatoro

prelegaj lumbildoj
lecture slides

prezenta programaro
presentation software 

slideshow generator
generatoro de bildoprezento

bildoprezento
slide show

Ahmad Yoosofan, [10/18/23 9:42 PM]
Prezenta programaro

Ahmad Yoosofan, [10/18/23 9:42 PM]
prezenta aplikaĵo
presentation application

Ahmad Yoosofan, [10/18/23 9:59 PM]
presentation generator 
generatoro de prezento

slideshow generator 
generatoro de bildoprezento

Hovercraft Changes
==================
2.8 (unreleased)
----------------

- Changed official support to 3.7, 3.8, 3.9, 3.10 and 3.13. Other Python 3 versions may or may not work.


2.7 (2020-02-08)
----------------

- Added the pre-check for file or folder existence when serving or
  creating the presentation.

- Juan Bondi made videos of the installation.


2.7beta1 (2019-11-06)
---------------------

This release moves Hovercraft! over to impress.js 1.0.0. This version of
impress.js has many new features and a new plugin system, which has plenty of
benefits, especially since some features of Hovercraft!, primarily
impressConsole.js, now are plugins to impress.js, so that's less
maintenance burden on me.

The most obvious changes from the previous version of Hovercraft! are:

 - The ``--skip-help`` argument, and ``:skip-help:`` control now disables
   the help popup altogether. This is because impress.js currently has no
   way to stop the help from displaying on load except disabling the help
   completely. This may change in the future.

- Also switched the default MathJax to 2.7.5, a minor update.
  impress.js MathJax extension is simply just Mathjax, there is no additional
  integration, so Hovercraft! doesn't change how Mathjax is integrated.

- Hovecraft! now supports the new impress.js "substep" plugin, so that
  you can show paragraphs lists item by item (see documentation).

Other changes are:

- You can now include audio and video by including the HTML5 <video> and
  <audio> tags in ..raw: html sections.

- Dropped support for Python 3.5, added support for 3.8.

- Many, many documentation fixes and improvements.


2.6 (2018-10-04)
----------------

- The ReStructuredText directive "figure" now is translated into the HTML5
  tag "figure", with the caption becoming a figcaption tag.

- Restored the warning that you need Python 3.5 or higher when trying to
  install with Python 2.

- Simplify in-process execution of Hovercraft! [tonysyu]

- Document how to make custom directives. [tonysyu]


2.5 (2017-12-10)
----------------

- Hovercraft! now displays the version number when called with -v or --version.

- New version of impressConsole that includes styling of the previews and
  a goto command <G>.

- ``:css-console:`` and ``:css-preview:`` added to style the console and
  add extra styles in the previews.

- :auto-console: and -a had stopped working [maxwell-k].


2.4 (2017-07-18)
----------------

- Option to display slide numbers [frederikmoellers]

- #51: Positioning relative to other slide [naraesk]

- Removed the code that uses pkg_util to access included templates. We don't
  support installing Hovercraft! as a ZIP file anyway, so it only complicates
  things for no good reason.

- Support for .. header:: and .. footer:: that can be used for static
  content.

- Dropped support for Python 3.3 and 3.4, because I now use recursive glob.

- Templates can now have a resource-directories statements, to specify extra
  directories of resources. This can be used in templates for JS libraries,
  like MathJax.

- The MathJax argument can now be a local copy.

- Switched the default MathJax URL to https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1


2.3 (2017-04-12)
----------------

- Better implementation of #98

- #72: Support for adding additional JS files [hbldh]

- Upgraded impress.js to 0.6.0

- Support for mathematical formulas with Mathjax [arabidopsis]

- Default template use UTF-8 [mariobodemann]

- Added support for Python 3.6

- readthedocs moved domain [adamchainz]


2.2 (2016-10-15)
----------------

- #98: Presentation not update when using gedit


2.1 (2016-02-27)
----------------

- #87: Support multiple :css: statements. [bitwalker]

- #86, #88: In-template resources failed for external templates.

- #89: The file monitoring could make the CPU go to 100%. [b6d]

- #81: positions.rst example was out of date.

- Dropped Python 3.2 support, because docutils doesn't seem to
  work on Python 3.2 any longer. With docutils 0.9 it probably
  still works.

- Updated tests to work with newer Pygments.

- #96: Relative paths was not working.

- #91: When modifying included files the presentation was not updated.


2.0 (2015-06-14)
----------------

- Better support for :class:. [fahhem]

- Now supports data-perspective. [fahhem]

- Fixed typos in template.py. [fahhem, ggtools]


2.0b1 (2014-11-27)
------------------

- IMPORTANT! The positioning has been reimplemented. The most important change
  is that there is no longer any calculation of relative movement when you use
  absolute coordinates. Therefore, if you use absolute coordinates on some slides
  and then have no coordinates on other slides, your positioning may no longer
  be correct with version 2.0.

- IMPORTANT! Moved the "note" XML transformation into the templates, as this is an
  impress.js feature, and other libraries, such as Reveal.js, will render it
  differently. If you make your own templates, you need to update them accordingly!

- Relative coordinates (starting with r) are now supported for all positioning,
  attributes including rotation and scaling.

- Now includes a server-mode, that will serve the presentation via http and
  also re-generate the presentation if the source-files change.

- Images can now also have a :class: attribute.

- Added support for multiple levels of slides. This is to make it able
  to support for example Reveal.js through external templates.


1.1 (2013-03-15)
----------------

- ReST comments are no longer rendered to HTML. [carljm]

- Fixed a bug in the path handling for CSS resources. [carljm]

- Various fixes and improvements in ReST handling. [cjw296]


1.0 (2013-02-22)
----------------

- #1, #2: Add key-binding to pop up the help, a parameter and a presentation
  field setting to not show the help at load.

- Added documentation for #8: Naming steps.

- #7: You can now define CSS-files to be included with a :css:-field in the
  presentation.

- #3: You can now leave out the presenter notes from the output with the
  parameter -n or --skip-notes

- Added a "simple" template that has no presenter console.

- Updated to impress-console 1.1, fixing a Firefox bug.

- Added support for more HTML metadata.

- Finished documentation and examples.


1.0b2 (2013-02-13)
------------------

- Added syntax highlighting support.

- #9: All positioning variables except data-x and data-y are now "sticky" so
      they will keep their previous value if not defined.

- Documentation on https://hovercraft.readthedocs.io/


1.0b1 (2013-02-07)
------------------

- Initial release.
