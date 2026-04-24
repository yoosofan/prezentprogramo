
General guide line for change
-----------------------------

برای پیاده‌سازی جدید ابزار نمایش اسلاید به جز تغییر کتابخانه اصلی جاوا اسکریپت باید شکل دستورها را نیز عوض کنم. برای آغاز هر اسلاید از دستور جدید زیر کمک بگیرم یا اگر در rst هست نام آن را عوض کنم مثلاً slidesb یا همانند آن بگذارم.

.. slide:: title of this slide (optional)
    :class: class-of-this-slide (optional)
    :id: id-of-this-slide (optional)
    :classt: class of title (optional)
    :idt: id of title (optional)

برای تنظیم‌های نخست هر اسلاید نیز یک دستور جدید بگذارم که همه تنظیمات اولیه اسلاید در آن باشد.

.. slide.header:: title of slide
    :css:
    :js:
    :width:
    :height:
 
یک پوشه کلی هم برای rst2sb_slides_assets نیز ساخته شود که تنظیمات عمومی و پرونده‌های جاوااسکریپت ، css و همانند آن در این پوشه گذاشته شود. خروجی همه اسلایدها به صورت پیش‌فرض در یک پوشه بالاتر و در یک زیرپوشه جدید باشد که پوشه‌های درس‌ها جداگانه گذاشته شود یعنی زیر پوشه‌های آن شبیه پوشه‌های اصلی اسلایدها است و خوبی بزرگش این خواهد بود که می‌تواند یک مخزن متفاوت باشد و مخزن اصلی اسلایدها بی‌جهت با html و دیگر چیزها شلوغ نشود. در خط فرمان می‌توان گزینه‌هایی گذاشت که رفتار را شبیه hovercraft یا bildumilo کند و کنار rst خود اسلاید پوشه بسازد.

با این تغییرات هم کار پیاده‌سازی ساده‌تر می‌شود و همین که ساختار به شکل مورد علاقه من در خروجی تبدیل می‌شود. شاید در آینده نیز برای نمایش بهتر پرونده اصلی برای تقسیم بندی هر اسلاید درون پرونده اسلاید افزونه برای ویرایشگر محبوبم ساختم تا راحت‌تر بتوانم میان اسلایدها حرکت کنم همچنین بهتر است این افزونه به طور خودکار شماره اسلاید را در بخش نمایش تقسیم بندی ساختار پرونده قرار دهد

Rewrite to use docutils directly
---------------------------------
MyST-Parser
^^^^^^^^^^^
https://github.com/executablebooks/MyST-Parser
https://myst-parser.readthedocs.io/en/latest/


docutils
^^^^^^^^
docutils change directive options
https://www.docutils.org/docs/howto/rst-directives.html
https://www.docutils.org/docs/howto/rst-roles.html
https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#sections

docutils add options to current directive
https://docutils.sourceforge.io/docs/user/config.html
https://www.docutils.org/docs/user/config.html#configuration-file-sections-entries
https://stackoverflow.com/questions/32167384/how-do-i-convert-a-docutils-document-tree-into-an-html-string/32168938#32168938
https://stackoverflow.com/questions/75164714/how-to-create-a-new-document-in-sphinx-docutils-by-api

https://github.com/regebro/hovercraft/commit/7f714b5592749f9846fa2a115915168586da309a
https://github.com/regebro/hovercraft/commit/a4d470a2562a38e1cc14f8561bb1c1c9f0bfaa0c
https://github.com/regebro/hovercraft/commit/aa3d2fb593106b858b84fb2ba43792fa967f9d69
https://github.com/regebro/hovercraft/commit/3ee4a44a7d1708ba6bb89f9d54371bcf68c98c56
https://github.com/regebro/hovercraft/commit/2ede7bff05a127fef8ab06a87cc3a86f94ac25ee
https://github.com/regebro/hovercraft/commits/master/?after=251890b328bb26540b37498c21647beeaa69a7c9+314

https://github.com/jwodder/rst2json/blob/master/src/rst2json/writers/html5.py

https://stackoverflow.com/questions/47337009/rst2html-on-full-python-project


https://rst2html5.readthedocs.io/en/latest/_modules/docutils/nodes.html

https://rst2html5.readthedocs.io/_/downloads/en/stable/pdf/

https://docutils.sourceforge.io/docs/user/rst/quickref.html#example-callout
https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html


Publish project
^^^^^^^^^^^^^^^
github pypi token to publish
https://github.com/pypa/gh-action-pypi-publish
https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/

https://packaging.python.org/en/latest/overview/
https://packaging.python.org/en/latest/tutorials/packaging-projects/

https://discuss.python.org/t/how-to-release-python-code-on-github/38559
https://realpython.com/pypi-publish-python-package/
https://realpython.com/github-actions-python/
https://anshumanfauzdar.medium.com/using-github-actions-to-bundle-python-application-into-a-single-package-and-automatic-release-834bd42e0670
https://docs.github.com/en/actions/tutorials/build-and-test-code/python
https://stackoverflow.com/questions/77385800/how-do-i-make-a-github-project-automatically-install-my-python-packages-when-dow
github python applicatin create build files automatically
https://github.com/actions/toolkit
https://github.com/actions/toolkit/blob/main/.github/workflows/unit-tests.yml

test pytest
https://docs.pytest.org/en/stable/
github/workflows/test.yml pip install -e ".[test]"
https://github.com/regebro/hovercraft/tree/master/.github/workflows

https://pypi.org/project/Prezentprogramo/

Python syntax checkers break lines
https://discuss.python.org/t/pep-7-break-lines-before-operators-like-pep-8/62402/4
https://stackoverflow.com/questions/7942586/correct-style-for-line-breaks-when-chaining-methods-in-python/7942617#7942617
https://inventwithpython.com/blog/comparing-python-linters-2022.html
https://trunk.io/learn/comparing-ruff-flake8-and-pylint-linting-speed
https://pythonspeed.com/articles/pylint-flake8-ruff/

GUI instead of web browser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
suggest a python GUI package that uses html and css  but doesn't need webbrowser

If you want to build a Python GUI using HTML and CSS but without forcing your users to open a web browser, pywebview is your best bet. [1, 2]
While these libraries use web technologies, they don't require an external browser like Chrome or Firefox to be open. Instead, they use a "webview" component—a built-in part of the operating system (like WinForms on Windows or Cocoa on macOS) to render your UI in a native window. [2, 3, 4]
## Top Recommendations

* pywebview: The most direct choice for what you're asking. It is a lightweight wrapper that displays HTML/CSS in its own native window. It doesn't bundle a heavy browser engine like Electron, making the final executable much smaller.
* [NiceGUI](https://nicegui.io/): A modern framework that lets you build UIs in pure Python but with full support for adding custom HTML and CSS. It can run in "native mode," which automatically opens a separate window using a webview rather than a browser tab.
* [Eel](https://github.com/python-eel/Eel): Often described as a "lightweight Electron for Python". You write your frontend in standard HTML/CSS and your backend in Python, and they communicate seamlessly. It typically opens in a browser-like window, but can be configured to look like a standalone app.
* PySide6 / PyQt6 (with WebEngine): For professional-grade software, you can use the Qt WebEngine module. This embeds a full Chromium-based browser engine directly into a standard Qt desktop window, giving you complete CSS styling power alongside native desktop widgets. [1, 2, 3, 5, 6, 7, 8, 9]

## Quick Comparison

| Library [1, 2, 5, 7, 10, 11] | Primary Language | Best For | Footprint |
|---|---|---|---|
| pywebview | HTML/CSS | Lightweight wrappers | Very Small |
| NiceGUI | Python (supports CSS) | Rapidly building dashboards | Medium |
| Eel | HTML/CSS/JS | Simple offline web-tech apps | Small |
| PySide6 | Python/C++ | Complex, professional apps | Large |

Are you looking to build a simple tool or a large-scale commercial application?

[1] [https://medium.com](https://medium.com/@james.miller941/9-python-gui-libraries-to-build-modern-applications-2c04396b11d8)
[2] [https://python.libhunt.com](https://python.libhunt.com/pywebview-alternatives)
[3] [https://www.pythonguis.com](https://www.pythonguis.com/tutorials/getting-started-nicegui/)
[4] [https://www.reddit.com](https://www.reddit.com/r/learnpython/comments/1gd9pq4/have_gui_without_downloading_external_libraries/)
[5] [https://www.pythonguis.com](https://www.pythonguis.com/faq/html-css-and-js-in-a-desktop-app-qt-webengine-vs-electron-vs/)
[6] [https://www.youtube.com](https://www.youtube.com/watch?v=gyscrrS4hEA&t=17)
[7] [https://python.plainenglish.io](https://python.plainenglish.io/11-python-gui-libraries-that-dont-suck-in-2025-c3f065e75ebf)
[8] [https://www.youtube.com](https://www.youtube.com/watch?v=Bh8pYfwFjA0&t=26)
[9] [https://www.youtube.com](https://www.youtube.com/watch?v=Bh8pYfwFjA0&t=26)
[10] [https://medium.com](https://medium.com/@james.miller941/9-python-gui-libraries-to-build-modern-applications-2c04396b11d8)
[11] [https://www.youtube.com](https://www.youtube.com/watch?v=gyscrrS4hEA&t=17)

PyWebView
`````````
https://pywebview.flowrl.com/examples/
https://github.com/r0x0r/pywebview/blob/docs/examples/todos/main.py
https://pywebview.flowrl.com

PySide
``````
http://pyside.org
https://wiki.qt.io/Qt_for_Python
https://github.com/pyside/pyside-setup

NiceGui
```````
It is not useful because it needs web browser any way

https://nicegui.io
https://nicegui.io/documentation/matplotlib

does python nicegui support mathml natively
does python nicegui support mathml and grid and latest html css changes


does python nicegui support graphviz dot format?
how to use python nicegui for directly render a dot (graphviz) source dynamically?

PDF
----
https://github.com/rggarcia/impressjs2pdf
https://github.com/impress/impress.js/tree/master/src/plugins/mobile

rst2html5
^^^^^^^^^^
After changing the whole structure to directly use rst2html5,
then it could be easier to make a suitable html for print.

opera webdriver
^^^^^^^^^^^^^^^
https://github.com/operasoftware/operachromiumdriver
https://stackoverflow.com/questions/24719270/selenium-webdriver-and-opera-driver
https://github.com/operasoftware/operachromiumdriver/blob/master/examples/desktop_selenium_4.x.py

deck2pdf-python
^^^^^^^^^^^^^^^
https://github.com/astefanutti/decktape

https://github.com/attakei/deck2pdf-python

https://pypi.org/project/deck2pdf/

Python library to generate PDF from presentation html

deck2pdf is converter from your html slide into PDF format keeping slide layout.
Use as CLI only

pipx run deck2pdf https://slides.attakei.net/pyconjp-2022/ output.pdf

uvx deck2pdf https://slides.attakei.net/pyconjp-2022/ output.pdf

.. code::

	uv tool install playwright
	playwright install
	uv tool install deck2pdf

https://stackoverflow.com/questions/73171905/chromium-executable-doesnt-exist-for-running-playwright-within-a-deployed-googl

Mobile Devices
--------------
https://github.com/impress/impress.js/tree/master/src/plugins/mobile

Remote control
--------------
python control impress.js remote server

Impress.js server
^^^^^^^^^^^^^^^^^
https://github.com/tompro/impress-server

Impress-server enables you to share an impress.js presentation with other users. It is not only a remote control, but every user who opens the presentation while it is in presentation mode, will have the state of the presentation synced in real time to his browser.
What problem does it solve ?

In our company we permanently have video conferences with customers. Whenever we want to run a presentation for them we have to do this via a screen sharing tool. Screen sharing is fine but the quality is poor and it uses a lot of bandwith. With impress-server you can run a remote presentation with nearly no bandwidth useage at all and in full impress.js quality.

In addition to that, you can use impress-server just to give you the ability to remote control your presentation with your phone or another computer.
Install

Install via NPM:

npm install -g impress-server

other
^^^^^
https://stackoverflow.com/questions/19626684/how-can-i-make-reveal-js-work-with-a-presenter-remote

impress.js more information
---------------------------
https://github.com/impress/impress.js/blob/master/GettingStarted.md
https://dhananjaypurohit.medium.com/impress-js-a-better-way-of-making-presentations-4e5d7686e98c
http://platika.github.io/impress.js/

impress.js replacement
^^^^^^^^^^^^^^^^^^^^^^
alternative for impress.js for slide show
html slideshow

b6plus.js
`````````
https://www.w3.org/Talks/Tools/b6plus/
https://www.w3.org/Talks/Tools/b6plus-style-2025.html#slipshow
https://www.w3.org/Talks/Tools/b6plus-editor/
https://patrickbrosset.com/slides/AC-2025/#explorer-website
https://temperlang.github.io/tpac2025/Templates/Overview.html
https://www.w3.org/Talks/Tools/b6plus/writing-style-sheets.html

https://w3c.social/@bert
https://www.w3.org/People/Bos/

https://github.com/bert-github?tab=repositories
https://github.com/bert-github/SlideSyncBot
https://github.com/bert-github/SSE-Server

https://www.w3.org/Talks/Tools/b6plus/simple.css

https://github.com/orgs/w3c/repositories?q=sort%3Aname-asc&page=22


slidy2
``````
https://www.w3.org/Talks/Tools/Slidy2/Overview.html#(1)

i-slide
```````
https://w3c.github.io/i-slide/

inspire.js
``````````
https://github.com/LeaVerou/inspire.js/tree/master/src
https://github.com/LeaVerou/inspire.js
https://inspirejs.org

slipshow
````````
https://github.com/panglesd/slipshow
https://slipshow.org/#features

Similar projects
----------------
https://github.com/scommab/impressor
http://scommab.github.io/impressor/show/index.html#/step-2

features
---------
disable and enable mouse or keyboard


Other
------
* prepare for readthedocs and add to it.
* Copy MathJax fonts prezentprogramo/hovercraft/templates/default/js/MathJax/es5/output/chtml/fonts/woff-v2
* Remove extra files:
    * Prevent making extra grap_ii.png for changing yographviz
        * G.draw("test.svg", prog= 'dot', format='svg:cairo')
        * https://stackoverflow.com/a/72152677/886607
        * https://github.com/liuyug/python-docutils-graphviz/tree/master
        * https://github.com/liuyug/python-docutils-graphviz/blob/master/docutils_graphviz.py
        * https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Adding_vector_graphics_to_the_Web
        * https://docutils-ext.readthedocs.io/en/latest/svgt.html
* Add an option to run a new instance of web browser
* Replace `pyhtml2pdf` by `selenium` because of the following vulnerability:
    * https://security.snyk.io/vuln/SNYK-PYTHON-PYHTML2PDF-6254644
    * https://vuldb.com/?id.254137
    * https://vulners.com/github/GHSA-P3RV-QJ56-2FQX
    * https://www.cvedetails.com/cve/CVE-2024-1647/
    * https://cert.ir/node/6248
    * https://nvd.nist.gov/vuln/detail/CVE-2024-1647

    * https://github.com/xhtml2pdf/xhtml2pdf
    * https://github.com/CourtBouillon/weasyprint-samples/tree/master
    * https://github.com/Kozea/WeasyPrint/tree/main


    * https://github.com/plotly/plotly.py
    * https://plotly.com/python/static-image-export/
    * https://plotly.com/python/bar-charts/

    * return [nodes.raw('', parsed, format='html')]   # https://snyk.io/advisor/python/docutils/functions/docutils.parsers.rst.directives.register_directive
    * https://github.com/renatopp/pyramid-blog/blob/7dba5a948af8a61e00fea303367be12e5de6f788/blog/blog/libs/rest/reSTpygments.py#L73
    * https://github.com/renatopp/pyramid-blog/tree/master/blog/blog/libs/rest
    * https://github.com/renatopp/pyramid-blog/blob/master/blog/blog/libs/rest/reSTpygments.py
    * https://github.com/renatopp/pyramid-blog/blob/4cc950d6a82eeaa912c9e1111fe25a8cb836d660/blog/blog/libs/rest/reSTpygments.py#L73

    * https://pygraphviz.github.io/documentation/stable/install.html
* Remove MathJax and use current default as --output-math=MathML

.. _impress.js: http://github.com/bartaz/impress.js
.. _demo: https://regebro.github.io/hovercraft
.. _readthedocs.org: https://hovercraft.readthedocs.io/
.. _pip: http://www.pip-installer.org/en/latest/

COMMENT11


.. code:: sh

	function install_uv_python(){

		# install uv
		# On macOS and Linux.
		curl -LsSf https://astral.sh/uv/install.sh | sh

		uv self update
		uv tool upgrade --all

		uv python install 3.13.6
		uv venv --python 3.13.6  ~/install/uv13.6

		source ~/install/uv13.6

		uv tool install black
		black . --check
		black .

		uv tool install ruff@latest

		ruff check
		ruff check --fix

		uv tool install flake8
		flake8 .
		flake8 . --ignore=E501,W503,E203

		uv tool install autopep8
		autopep8 --in-place --aggressive  --recursive --list-fixes --max-line-length 79 .

		uv build

		# uv publish dist/*
		# uv publish --token <your_pypi_token>

		twine check --strict dist/*
		twine upload dist/*
	}

	function old11(){

		pip3 uninstall prezentprogramo -y

		rsync -av --delete ~/research/projects/prezentprogramo/ ~/temp/prezentprogramo/

		pip3 install ~/temp/prezentprogramo/

		cd ~/research/projects/slide/cm/

		#rm -rf rd/

		prezentprogramo rd.rst

		uv tool install ini2toml[full]
		ini2toml --help
		ini2toml -o setup.toml setup.cfg

	}

related
-------
uv
^^^^
https://blog.appsignal.com/2025/09/24/switching-from-pip-to-uv-in-python-a-comprehensive-guide.html

Add repository to other places
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dainiak
```````
https://github.com/dainiak/lists
https://github.com/dainiak/lists/blob/main/data/slideshow-frameworks.json
https://www.dainiak.com/lists/slideshow-frameworks.html


AI conversations
----------------
Gemini Replacing impress.js by sb6+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Directive Name Fri Apr 24 08:02:25 +04 2026
```````````````````````````````````````````

In implementation of extending docutils abilities, is it possible to use the same directive name for another purpose? How can be implemented ? For example I could use simpler directive name instead of yographviz but I wouldn't be sure that docutils may not use a simpler name in future.

Answer
~~~~~~
Your instinct to use a unique name like yographviz was actually spot-on. When building extensions, name collisions are a genuine concern.
To answer your question directly: **Yes, it is absolutely possible to use the same directive name** (like graphviz instead of yographviz), which effectively overrides any existing directive with that name.
Here is exactly how Docutils handles this and how you can implement it.
### How Directive Registration Works in Docutils
In Docutils, directives are stored in a global dictionary within the docutils.parsers.rst.directives module. When you register a directive, you map a string (the directive name) to a Python class.
If you register a directive using a name that is already taken, **Docutils will silently overwrite the existing mapping**. The last directive registered with that name "wins."
### How to Implement an Override
If you wanted to use the simpler name graphviz, you would implement your directive class as usual, and then register it under the name graphviz.
Here is the Python implementation:
```python
from docutils.parsers.rst import Directive, directives

# 1. Define your custom directive class
class MyGraphvizDirective(Directive):
    has_content = True
    # ... your implementation here ...

    def run(self):
        # ... logic to process the DOT code ...
        return []

# 2. Register it using the simple name
# If 'graphviz' already exists, this overwrites it for your runtime.
directives.register_directive('graphviz', MyGraphvizDirective)

```
By putting this registration code in your prezentprogramo initialization logic (before the parsing of the RST file begins), your custom parser will intercept any .. graphviz:: blocks and route them to your custom class.
### The Risks of Overriding (Why Your Current Approach is Better)
While overriding is easy to implement, your initial caution was correct. Overriding standard names or using highly generic names comes with architectural risks:
 * **Future Docutils Updates:** As you noted, if Docutils ever adds a native graphviz directive, your code will overwrite it. This might be fine if you *want* to override it, but it becomes problematic if users want to use the native Docutils behavior elsewhere in the document.
 * **Sphinx Compatibility:** Many developers use Sphinx (which is built on Docutils) alongside custom tools. Sphinx already has a very famous and heavily used graphviz extension. If a user tries to compile their slides with your tool, and their documentation with Sphinx, having identically named directives with different feature sets or attributes will cause massive headaches.
 * **Loss of Standard Functionality:** If you override a standard directive (like image or table) to add custom presentation logic, you completely lose the ability to use standard images or tables in that document.
### Best Practice: The Namespace Approach
Instead of overriding standard names, the standard academic and enterprise practice for Docutils/Sphinx extensions is to use a **namespace prefix**.
Your yographviz is perfectly fine, but if you want something that feels a bit more standard or readable, you can use a hyphenated prefix indicating your application's namespace. For example:
 * .. pp-graphviz:: (for **p**rezent**p**rogramo)
 * .. yo-graphviz::
This guarantees 100% safety from future Docutils updates and instantly tells anyone reading the RST file that this block is specifically parsed by your custom extension, not standard Docutils.

Can a period (dot) be part of directive name?
`````````````````````````````````````````````
Answer
~~~~~~

Yes, a period (dot) can absolutely be used as part of a directive name!
In fact, according to the official Docutils reStructuredText specification, directive names (referred to as "directive types") are case-insensitive single words that can contain **alphanumerics plus isolated internal hyphens, underscores, plus signs, colons, and periods.**
Using a period is actually a brilliant way to implement the namespace approach we discussed earlier. It is commonly used in object-oriented programming to show ownership or hierarchy, making it very intuitive for developers.
Here is how you can implement and use it in your code.
### 1. Registering the Directive with a Period
You register it exactly the same way as any other name, just including the dot in the string.
```python
from docutils.parsers.rst import Directive, directives

class MyGraphvizDirective(Directive):
    has_content = True
    
    def run(self):
        # Your DOT parsing logic goes here
        return []

# Registering with a period to indicate the 'pp' (prezentprogramo) namespace
directives.register_directive('pp.graphviz', MyGraphvizDirective)

```
### 2. Using it in your reStructuredText
Once registered, you or your users can call it in the .rst file by typing the exact name you registered.
```rst
.. pp.graphviz::
   
   digraph G {
       A -> B;
   }

```
### Why this is an excellent choice:
 * **Zero Collision Risk:** It guarantees you will never clash with Docutils' native graphviz (if they ever make one) or Sphinx's graphviz extension.
 * **Semantic Clarity:** The dot notation (pp.graphviz) instantly communicates to the user that this is the "graphviz component belonging to the pp application." It looks professional and structured!

compare impress.js sb6+
```````````````````````


I can definitely break down the strengths of **impress.js**, but I have to be completely candid with you: I am coming up empty on a presentation library called **sb6+**!
It is possible "sb6+" is an internal tool, a very niche library, or maybe a typo for another popular framework (like **S5/S6**, **Slidev**, **Spectacle**, or even **Storybook 6+** for UI presentations).
While you clarify what sb6+ is, here is a look at what makes impress.js tick, especially compared to standard linear slide tools.
### 🌟 The Magic of impress.js
Impress.js is heavily inspired by Prezi. Instead of a linear stack of slides, it treats your presentation as an **infinite 3D canvas**.
**Key Features:**
 * **Spatial Storytelling:** You place your "slides" (HTML elements) anywhere in a 3D space. You can scale them up or down, rotate them on the X, Y, or Z axes, and push them deep into the background.
 * **CSS3 Power:** It relies entirely on modern CSS3 transforms and transitions. When you move from one slide to the next, the browser automatically animates the camera moving, zooming, and rotating to focus on the next element.
 * **No Fixed Structure:** It is perfect for mind-maps or showing how small details fit into a massive overarching architecture (which is great for complex topics like Compiler hierarchies or Database schemas).
**The Trade-offs:**
 * **Authoring Complexity:** Because you are manually defining data-x, data-y, data-z, data-scale, and data-rotate for every single slide, writing an impress.js presentation by hand in HTML can be tedious and requires a lot of trial and error to get the spacing right.
 * **Not Great for Simple Content:** If you just need to show 20 bullet-point slides sequentially, impress.js is massive overkill and can actually cause motion sickness for your audience if you overuse the spinning transitions.
To help me give you a proper head-to-head comparison, **could you clarify what "sb6+" refers to (e.g., is it a typo for another framework like Slidev or S6, or perhaps a specific standard you are using)?**



Aboat sb6 specifications
````````````````````````

Https://www.w3.org/Talks/Tools/b6plus/

Source code: https://www.w3.org/Talks/Tools/b6plus/slides.zip

Yes, I need only simple slide for my courses. I mostly don't need fancy slides because making and updating my slides in daily basis has enough pressure itself. As you can see, sb6+ have very good internal tools like having market to make lines on a slide like a simple paint program. I actually use Firefox extension for this matter. You can watch my last week videos in my YouTube channel and how I use it. But it took me years to find something like that while sb6+ already has it. Printing sb6+ slides are far easier than impress.js and it doesn't need to have a web browser engine and many extra python packages. Using sb6+ instead of impress.js in prezentprogrammo will decrease a lot of packages dependencies. My first today question was more about adding a directive for each slide by the name slide or variation of it instead of four dash for each slide in current implementation based on hovercraft


Answer
``````

That makes perfect sense! **b6plus** (by Bert Bos at W3C) is an incredible choice for an academic setting. It follows the "Web Standards" philosophy: it's incredibly lightweight, accessible, and uses standard HTML structures rather than complex 3D transformations.
Moving away from hovercraft (which is hard-coded to impress.js) to a custom b6plus generator for **prezentprogramo** will definitely make your workflow faster and reduce your Python dependency hell.
### 1. Replacing the "Four Dash" Separator with a Directive
Currently, hovercraft uses ---- (reStructuredText transitions) to split slides. If you want to use a directive like .. slide:: instead, you can implement a custom Docutils directive.
This is much cleaner because it allows you to add **options** (like a specific slide class or background color) directly to that slide.
**Python implementation for your tool:**
```python
from docutils import nodes
from docutils.parsers.rst import Directive

class Slide(nodes.General, nodes.Element):
    pass

class SlideDirective(Directive):
    has_content = True
    
    def run(self):
        # Create a container node for the slide
        slide_node = Slide()
        # Parse the content inside the .. slide:: block
        self.state.nested_parse(self.content, self.content_offset, slide_node)
        return [slide_node]

# In your setup:
# directives.register_directive('slide', SlideDirective)

```
**What your .rst will look like now:**
```rst
.. slide::
   :class: cover-slide

   Title of Slide
   ==============
   * Bullet one
   * Bullet two

```
### 2. Why b6plus is better for your "Daily Pressure"
You mentioned the pressure of daily updates. Here is why b6plus beats impress.js for a teacher:
 * **The Marker/Pen Tool:** b6plus has that built-in F8 (or similar) drawing mode. In impress.js, the coordinates are so complex that if you draw on the screen and then zoom/rotate to the next slide, the drawings usually don't align or get lost in 3D space.
 * **Printing/PDF:** b6plus uses standard CSS @media print. You just hit Ctrl+P and it prints one slide per page perfectly. impress.js usually requires a headless Chrome instance and a complex script just to get a decent PDF.
 * **Simple Layouts:** b6plus doesn't require you to manage X, Y, and Z coordinates. If you add a paragraph, the slide just grows. In hovercraft/impress.js, if your text is too long, it overflows the "camera view," and you have to manually adjust the scale.
### 3. Implementation Tip for b6plus
When you write your writer for prezentprogramo, you just need to map the Slide node (from the code above) to a <section class="slide"> tag.
**In your Writer's visit_Slide method:**
```python
def visit_Slide(self, node):
    self.body.append('<section class="slide">')

def depart_Slide(self, node):
    self.body.append('</section>')

```
This will produce the exact HTML structure b6plus needs. No more fighting with hovercraft’s layout engine! Since you are already using Firefox extensions for marking, you'll find the native b6plus features even more integrated for your YouTube recordings.

compare impress.js sb6+
```````````````````````


I can definitely break down the strengths of **impress.js**, but I have to be completely candid with you: I am coming up empty on a presentation library called **sb6+**!
It is possible "sb6+" is an internal tool, a very niche library, or maybe a typo for another popular framework (like **S5/S6**, **Slidev**, **Spectacle**, or even **Storybook 6+** for UI presentations).
While you clarify what sb6+ is, here is a look at what makes impress.js tick, especially compared to standard linear slide tools.
### 🌟 The Magic of impress.js
Impress.js is heavily inspired by Prezi. Instead of a linear stack of slides, it treats your presentation as an **infinite 3D canvas**.
**Key Features:**
 * **Spatial Storytelling:** You place your "slides" (HTML elements) anywhere in a 3D space. You can scale them up or down, rotate them on the X, Y, or Z axes, and push them deep into the background.
 * **CSS3 Power:** It relies entirely on modern CSS3 transforms and transitions. When you move from one slide to the next, the browser automatically animates the camera moving, zooming, and rotating to focus on the next element.
 * **No Fixed Structure:** It is perfect for mind-maps or showing how small details fit into a massive overarching architecture (which is great for complex topics like Compiler hierarchies or Database schemas).
**The Trade-offs:**
 * **Authoring Complexity:** Because you are manually defining data-x, data-y, data-z, data-scale, and data-rotate for every single slide, writing an impress.js presentation by hand in HTML can be tedious and requires a lot of trial and error to get the spacing right.
 * **Not Great for Simple Content:** If you just need to show 20 bullet-point slides sequentially, impress.js is massive overkill and can actually cause motion sickness for your audience if you overuse the spinning transitions.
To help me give you a proper head-to-head comparison, **could you clarify what "sb6+" refers to (e.g., is it a typo for another framework like Slidev or S6, or perhaps a specific standard you are using)?**



Aboat sb6 specifications
````````````````````````

Https://www.w3.org/Talks/Tools/b6plus/

Source code: https://www.w3.org/Talks/Tools/b6plus/slides.zip

Yes, I need only simple slide for my courses. I mostly don't need fancy slides because making and updating my slides in daily basis has enough pressure itself. As you can see, sb6+ have very good internal tools like having market to make lines on a slide like a simple paint program. I actually use Firefox extension for this matter. You can watch my last week videos in my YouTube channel and how I use it. But it took me years to find something like that while sb6+ already has it. Printing sb6+ slides are far easier than impress.js and it doesn't need to have a web browser engine and many extra python packages. Using sb6+ instead of impress.js in prezentprogrammo will decrease a lot of packages dependencies. My first today question was more about adding a directive for each slide by the name slide or variation of it instead of four dash for each slide in current implementation based on hovercraft


Answer
``````

That makes perfect sense! **b6plus** (by Bert Bos at W3C) is an incredible choice for an academic setting. It follows the "Web Standards" philosophy: it's incredibly lightweight, accessible, and uses standard HTML structures rather than complex 3D transformations.
Moving away from hovercraft (which is hard-coded to impress.js) to a custom b6plus generator for **prezentprogramo** will definitely make your workflow faster and reduce your Python dependency hell.
### 1. Replacing the "Four Dash" Separator with a Directive
Currently, hovercraft uses ---- (reStructuredText transitions) to split slides. If you want to use a directive like .. slide:: instead, you can implement a custom Docutils directive.
This is much cleaner because it allows you to add **options** (like a specific slide class or background color) directly to that slide.
**Python implementation for your tool:**
```python
from docutils import nodes
from docutils.parsers.rst import Directive

class Slide(nodes.General, nodes.Element):
    pass

class SlideDirective(Directive):
    has_content = True
    
    def run(self):
        # Create a container node for the slide
        slide_node = Slide()
        # Parse the content inside the .. slide:: block
        self.state.nested_parse(self.content, self.content_offset, slide_node)
        return [slide_node]

# In your setup:
# directives.register_directive('slide', SlideDirective)

```
**What your .rst will look like now:**
```rst
.. slide::
   :class: cover-slide

   Title of Slide
   ==============
   * Bullet one
   * Bullet two

```
### 2. Why b6plus is better for your "Daily Pressure"
You mentioned the pressure of daily updates. Here is why b6plus beats impress.js for a teacher:
 * **The Marker/Pen Tool:** b6plus has that built-in F8 (or similar) drawing mode. In impress.js, the coordinates are so complex that if you draw on the screen and then zoom/rotate to the next slide, the drawings usually don't align or get lost in 3D space.
 * **Printing/PDF:** b6plus uses standard CSS @media print. You just hit Ctrl+P and it prints one slide per page perfectly. impress.js usually requires a headless Chrome instance and a complex script just to get a decent PDF.
 * **Simple Layouts:** b6plus doesn't require you to manage X, Y, and Z coordinates. If you add a paragraph, the slide just grows. In hovercraft/impress.js, if your text is too long, it overflows the "camera view," and you have to manually adjust the scale.
### 3. Implementation Tip for b6plus
When you write your writer for prezentprogramo, you just need to map the Slide node (from the code above) to a <section class="slide"> tag.
**In your Writer's visit_Slide method:**
```python
def visit_Slide(self, node):
    self.body.append('<section class="slide">')

def depart_Slide(self, node):
    self.body.append('</section>')

```
This will produce the exact HTML structure b6plus needs. No more fighting with hovercraft’s layout engine! Since you are already using Firefox extensions for marking, you'll find the native b6plus features even more integrated for your YouTube recordings.

Problems of bs6+
````````````````

But there are some problems in B6+ :
1. It uses old form of JavaScript code writing and it doesn't use newer JavaScript way of writing a JavaScript code. Bs6+ is less modular.

2. There are less documentation and usage of it in other projects. Therefore using it may not as easy. Even you didn't know about bs6+ in the first encounter of name and you had to ask me to be more specific.

3. It doesn't have some necessary features like right mouse click to go to the previous slide. It doesn't use wheel mouse for changing slides. The bs6+ way of coding is much harder to extend or change it. It is mostly only one man creation.

What do you think about above problems?
Do you have good solutions for them or at least some suggestions?



You’ve hit on the classic "Academic Tool Dilemma." **b6plus** is brilliant because it is designed by a father of the Web (Bert Bos) to be incredibly lean, but it suffers from being a "frozen in time" project. It is more of a finished work of art than a living framework.
Here is a breakdown of how to address those specific technical hurdles if you decide to stick with it for your prezentprogramo tool.
### 1. The "Old" JavaScript & Lack of Modularity
The code is likely written in the "Global Namespace" style of the early 2000s (pre-ES6).
 * **The Suggestion:** Don't try to refactor his code. Instead, **wrap it**. Since you are building a generator, you can treat b6.js as a "black box" vendor script.
 * **Modernizing it:** If you need to add modular features, you can load b6.js and then write a modern **ES6 Module** wrapper around it that interacts with the DOM events it fires. You keep the "engine" old but build your "dashboard" with modern JS.
### 2. Lack of Documentation & Community
Because only a handful of people at W3C use it, you won't find help on StackOverflow.
 * **The Solution:** Since you are a programmer building a tool for your own courses, you become the documentation. The "source of truth" for b6plus is the **source code itself**—which, fortunately, is very small.
 * **The Silver Lining:** Unlike impress.js or Reveal.js, which have thousands of lines of code, b6plus is small enough that you can read the entire thing in an afternoon. This gives you *more* control, not less.
### 3. Missing Features (Mouse Wheel & Right Click)
This is actually the easiest problem to solve! Because b6plus relies on simple HTML anchors or CSS classes to change slides, you can "inject" these features using a small, modern helper script in your generator.
**Solution: The "Bridge" Script**
In your prezentprogramo output, you can include a tiny 20-line script that adds these UX features without touching Bert Bos’s original code:
```javascript
// A modern helper to fix b6plus UX issues
window.addEventListener('wheel', (e) => {
    if (e.deltaY > 0) {
        // Trigger b6plus "Next" (usually a click or key event)
        document.dispatchEvent(new KeyboardEvent('keydown', {'key': 'PageDown'}));
    } else {
        document.dispatchEvent(new KeyboardEvent('keydown', {'key': 'PageUp'}));
    }
});

window.addEventListener('contextmenu', (e) => {
    e.preventDefault(); // Stop the menu from appearing
    // Trigger b6plus "Previous"
    document.dispatchEvent(new KeyboardEvent('keydown', {'key': 'PageUp'}));
});

```
### The Verdict: Should you use it?
If your priority is **minimalism and the Marker Tool**, b6plus is still a strong candidate despite its "one-man project" status. However, if the "Old JS" bothers you, I recommend looking at **Shower.js**.
**An Alternative: Shower.js**
 * **Similarities:** It is also "HTML-first" and very lightweight.
 * **Advantages:** It is modern, modular (uses Vanilla JS/ES6), and well-documented.
 * **Caveat:** It doesn't have the "Marker" tool built-in, but because it is modular, adding a marker library (like markerjs) to it would be very easy.
**My Peer Suggestion:** If you love the **drawing features** of b6plus, use it but add a "UX Fixer" script like the one I wrote above. It keeps your tool simple, reduces Python dependencies, and gives your students a very fast, printable slide deck. Don't worry about it being a "one-man creation"—in the world of open source, sometimes a small, finished tool is more reliable than a massive, constantly changing framework!

Wrap modernized javascript around old js code
`````````````````````````````````````````````

Thanks, 

1. I didn't fully understand the "Modernizing it". Do you have any small projects that use this method? Or you can make simple example to show how it works?

2. I checked shower.js too but it has some problems too. First and for most it cannot be run without a web server. It is not possible that open an slide in a browser and it works. Making offline html file to put in a simple server like GitHub and a like is one the benefits of hovercraft. I do use it to put my slides easily on the web. For example https://yoosofan.github.io/slide/os/yic/#/step-2

3. You are totally right about my not good spoken way of one man creation. I really didn't mean that. I just wanted to describe the situation but I didn't use the right words to say it.


Answer
~~~~~~


I completely understand—when a project is a "one-man creation," it usually means it’s a specific vision that might not follow common community standards, making it harder to customize. It’s a very practical observation!
Let’s address your points on modernization and the "Offline/File" requirement.
### 1. Modernizing "Old" Code (The Wrapper Method)
By "Modernizing it," I mean treating the old b6plus.js like an engine inside a car. You don't take the engine apart; you just build a new, modern dashboard (your ES6 code) that talks to it.
**The Concept:** Old JS often communicates via **Global Events** (like key presses) or by changing the **URL Hash** (like #/step-2). Your modern script just sends those signals.
**Simple Example:**
Suppose b6plus.js listens for the "Right Arrow" key to change slides. You want to add a "Mouse Wheel" feature using modern ES6 modules.
```javascript
// your-modern-extension.js (ES6 Module)
export const initModernControls = () => {
    window.addEventListener('wheel', (event) => {
        // We detect the wheel move...
        const direction = event.deltaY > 0 ? 'ArrowRight' : 'ArrowLeft';
        
        // ...and we "fake" a keypress that the old b6plus code understands
        const fakeKey = new KeyboardEvent('keydown', { key: direction });
        document.dispatchEvent(fakeKey);
        
        console.log(`Modern JS told the Old JS to go: ${direction}`);
    });
};

```
You would include it in your HTML like this:
```html
<script src="b6plus.js"></script>

<script type="module">
    import { initModernControls } from './your-modern-extension.js';
    initModernControls();
</script>

```
### 2. The "Offline / File://" Requirement
You are 100% correct about **Shower.js**. Many modern frameworks (like Slidev or Reveal.js) rely on "Asynchronous Module Definition" (AMD) or fetching external assets, which triggers **CORS security errors** when you open a file directly from your hard drive (file:///C:/...).
**Why b6plus (and hovercraft) win here:**
They are designed to be "Self-Contained." Because b6plus is just one file and doesn't try to "fetch" other pieces of itself, the browser's security doesn't block it.
If you want to host on GitHub Pages or run from a USB stick without a local server, b6plus is technically superior for that specific use case.
### 3. Suggestions for PrezentProgramo
Since you need **offline capability**, **minimal dependencies**, and **easy printing**, here is my suggestion for your directive-based implementation:
**The Slide Directive (.. slide::)**
Instead of using the four dashes ----, use the directive I mentioned earlier. It makes your RST look much more like professional code:
```rst
.. slide::
   :id: introduction
   :class: title-slide

   Operating Systems
   =================
   Week 5: Memory Management

```
**The Generator Strategy:**
 1. **Extract the CSS/JS:** Copy the b6plus.js and the basic CSS file into your Python package assets.
 2. **The Writer:** Have your Python script wrap each .. slide:: block in a <section class="slide">.
 3. **The "Fixer" Script:** Include a small snippet of JavaScript (using the "Modernization" method above) to add the mouse wheel and right-click functionality you missed.
This way, you get the **best of both worlds**:
 * The **stability and drawing tools** of Bert Bos’s b6plus.
 * The **modern UX** (wheel/right-click) that you want.
 * The **zero-server** requirement so your students can just download a single .html file.
**A relevant follow-up question:**
In your YouTube videos, do you find it more helpful to draw "live" on top of existing text, or do you prefer having a dedicated "blank space" on the slide for sketching?


Pro model limit
```````````````
Fri Apr 24 08:14:28 +04 2026


date based
----------
2026/04/01
^^^^^^^^^^
* Change created folder name for each rst slide to ``rst_name.htmls.prezaentprogramo/``
* Move more about installation to docs/install.rst
    * https://packaging.python.org/en/latest/tutorials/packaging-projects/
    * https://github.com/nedbat/pkgsample/blob/main/Makefile
    * build.sh to Makefile
    * makefile documentation for python
    * https://github.com/python/docs-community/blob/main/Makefile
    * https://svn.python.org/projects/python/trunk/Doc/Makefile
    * https://gist.github.com/MarkWarneke/2e26d7caef237042e9374ebf564517ad
    * https://makefiletutorial.com/
    * https://earthly.dev/blog/python-makefile/
    * https://www.kdnuggets.com/the-case-for-makefiles-in-python-projects-and-how-to-get-started


