
server providing decoupled browser creation/driving via zmq



The server listens on a port (default 5402) for command strings. These
commands should be coming from ruamel.browser.client.

Most command strings start with ``br BID ...`` and therefore need
to have unique browser id (``BID``).

You can check if the ``BID`` is available (ie. browser opened from previous
run) using `check BID`. If it is not available you should initialise a new
browser using ``init BID TYPE`, where `TYPE`` is e.g. ``selenium`` for a
Firefox browser driven by selenium.

If the browser you want to create needs to run under VNC, first create a virtual
display using ``display DISPNAME port_num x-size y-size`` and then initialise the
browser using ``init display DISPNAME BID TYP`` (e.g. by doing::

  display virt1 5409 1000 500
  init display virt1 stackoverflow selenium

You can re-use a ``DISPNAME`` for different browsers. If you don't specify a ``display`` the
browser will open on the desktop (which needs to be there).

Once you have a `BID`` for a browser you can sent it commands. All browsers
should implement quitting (invoked by ``br BID quit``) and
setting the verbosity to something else than 0 (``br BID verbose NUM``)

You can find an elment on the page in different ways, by CSS selection
is the recommended way (that skill can be reused when building websites
of your own when specifying CSS files). The syntax is::

   find [store ELEM] css|id|class MSG

where ``MSG`` is used as a parameter to the `css` (or ``id`` or ``class``) selector. If
the optional ``store ELEM`` part is used the element on the page is stored for
further use in ``find`` or other commands that operate on an element or DOM tree part.
Find also sets a "current element" which will be used in future commands if
no specific element is selected with the optional "elem ID" parameter

Other commands available in the selenium back-end::

  title: returns title of current page
  current_url: return URL of page that is open
  get SOMEURL: "browse" to the page SOMEURL
  click [elem ELEM]: click on the current
  displayed [elem ELEM]: check if the element is displayed (returns yes or no)
  keys [elem ELEM] SEQUENCE_OF_KEYS: send keys to the selected element
  down_up [elem ELEM]: similar to click but with a delay after mouse down of 0.5s
  javascript PROGRAM: execute PROGRAM in the browser
  inner [elem ELEM]: return the inner HTML attribute (for further processing on client side)
  hover [elem ELEM]: hover the mouse above an element (might trigger some javascript loading)
  findallid [elem ELEM] CSS: for elements by CSS selector (under ELEM if specified) return IDs

As keys can be sent to the browser individually, you can interact
with pages expecting people to type in an answer (instead of filling a form
element in one go). Using ``inner`` you can also get back what is in
such an element, .e.g. if the browser did some javascript based expansion.


RBSSELENIUM environment variable
--------------------------------

Although automation, especially using VNC displays, doesn't get you
advertisements in your face, you might want to set an environment variable ``RBSSELENIUM``.
Under the absolute path that env. var points to, there should be at least two files::

  adblock/adblock_plus-2.7-fx+sm+tb+an.xpi
  profile00/adblockplus/patterns.ini

Which will be loaded in FireFox preventing advertisements from opening.
This can **hugely** affect the speed with which you can navigate a site.