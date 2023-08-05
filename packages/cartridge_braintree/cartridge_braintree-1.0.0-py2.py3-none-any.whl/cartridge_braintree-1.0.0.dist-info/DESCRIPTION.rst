cartridge_braintree
===================

Braintree Payments processing for Mezzanine/Cartridge.
Supports Cartridge 0.11 and newer.

Instructions for use
--------------------

1. Install cartridge_braintree::

      pip install cartridge_braintree

   If you need the correct sorting of not ASCII country names use::

      pip install cartridge_braintree[countries_utf8_sorting]

   This will add 'pyuca' to the requirements.

2. Add 'cartridge_braintree' to your ``INSTALLED_APPS``. List it higher than
   'cartridge.shop', otherwise the cartridge_braintree template will
   not be selected.

3. Set up the following settings in your ``settings.py`` or ``local_settings.py``::

      BRAINTREE_MERCHANT_ID = <your merchant ID>
      BRAINTREE_PUBLIC_KEY = <your public key>
      BRAINTREE_PRIVATE_KEY = <your private key>

   .. Note::
      When ``DEBUG`` is ``True`` the *Braintree Sandbox environment* will be
      used, otherwise the *Braintree Production environment* is used.

   See also
   https://articles.braintreepayments.com/control-panel/important-gateway-credentials

4. cartridge_braintree uses a modified checkout form, which does the following:

   - Changes the shipping and billing country fields to a Select
     widget. This ensures that the country selected can be converted to
     a valid code for Braintree's payment processing.
     The supported countries can be set in ``settings.SHOP_SUPPORTED_COUNTRIES``,
     which is a list of alpha2 country codes and/or tuples in the form
     (alpha2, country_name).

     For example if you want to select the countries in the EU area use::

        SHOP_SUPPORTED_COUNTRIES = [
            'AL', 'AT', 'BA', 'BE', 'BG', 'CH', 'CY', 'DE', 'DK', 'EE', 'ES',
            'FI', 'FR', 'GB', 'GR', 'HR', 'HU', 'IE', 'IS', 'IT', 'LT', 'LV',
            'MK', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'RS', 'SE', 'SI'
         ]

     The country/countries (as alpha2 codes) listed in
     ``settings.SHOP_PRIMARY_COUNTRIES`` will show up at the top of the
     country selection fields.

   - Credit Card number and CCV fields are rendered using the
     ``NoNameTextInput`` widget so that the data is not submitted to the
     server. Javascript processes these fields to create a
     ``payment_method_nonce``, which is then stored in a hidden form
     element.

   - Uses `jquery.payment <https://github.com/stripe/jquery.payment>`_ from stripe
     for client-side validation of the payment form and submits the errors in the
     hidden ``braintree_errors`` field to the server to handle them as Django errors.

   See
   https://developers.braintreepayments.com/guides/transactions/python

5. Set the payment handler to be the Braintree payment handler::

      SHOP_HANDLER_PAYMENT = 'cartridge_braintree.braintree_payment.payment_handler'

   If you are overriding the templates in your own apps, then be sure to
   include the relevant ``braintreejs.html`` template.

   See https://www.braintreepayments.com/docs/python/guide/getting_paid
   for Braintree's tutorial.

6. Include ``cartridge_braintree.urls`` for ``shop/checkout`` in ``urls.py``
   before Cartridge urls::

      urlpatterns += [

          # cartridge_braintree URLs.
          url("^shop/(?=checkout(/?)$)", include("cartridge_braintree.urls")),

          # Cartridge URLs.
          url("^shop/", include("cartridge.shop.urls")),
          url("^account/orders/$", order_history, name="shop_order_history"),

7. If you want to use PayPal payments with Braintree activate them in
   the Admin Site Settings and set the currency to use with PayPal.

   Alternatively you can set them in ``settings.py`` in the form::

      BRAINTREE_PAYPAL_ACTIVATE = True
      BRAINTREE_PAYPAL_CURRENCY = "EUR"

   In this case the settings will not be shown in the Admin.


CHANGES
=======

1.0.0 (2016-07-08)
------------------

- **Breaking change**: Simplify urls setup. [ryneeverett]
  When upgrading, change cartridge_braintree urls to
  ``url("^shop/(?=checkout(/?)$)", include("cartridge_braintree.urls")),``
   in ``urls.py``.
- Make it a stable release version as it's already well tested.
- Introduce `semantic versioning`_.
- Use zest.releaser for release.

.. _semantic versioning: http://semver.org

1.0b17 (2016-04-17)
-------------------

- Upgrade jquery.payment.js to v1.3.3. [ryneeverett]

1.0b16 (2016-04-17)
-------------------

- Fix documentation bug.
  It should be ``BRAINTREE_MERCHANT_ID`` not ``BRAINTREE_MERCHANT``
  in ``settings.py``.

1.0b16 (2016-04-17)
-------------------

- Fix documentation bug.
  It should be ``BRAINTREE_MERCHANT_ID`` not ``BRAINTREE_MERCHANT``
  in ``settings.py``.

1.0b14 (2016-03-14)
-------------------

- Replace the payform jQuery plugin with
  `jquery.payment <https://github.com/stripe/jquery.payment>`_
  from stripe.
  This fixes some bugs with card number and CCV formatting.

1.0b13 (2016-02-03)
-------------------

- Move static content to subfolder.
- Clean up translation files.
- Minor fixes and javascript optimizations.

1.0b10 (2016-01-30)
-------------------

- Overextents templates instead of overriding them.
- Show Card payment form when Django returns errors.
- Add placeholders for card number and CCV
  and trigger numeric keyboard on iPhone.
- Add dependency on Cartridge 0.11.
  Drop support for older Cartridge versions.
- Minor fixes.

1.0b8 (2016-01-25)
------------------

- Upgrade to Cartridge 0.11.
- Clean up the template directory.

1.0b4 (2016-01-21)
------------------

This is an entire rewrite release of the whole app by Henri Hulski.

- Rewriting the app to match the new Braintree v.zero API.
- Refactor country support for billing/shipping inspired by
  `django-countries <https://github.com/SmileyChris/django-countries>`_.
  and using their translations of country names.
- Add client site credit card validation and number formatting using the
  jQuery plugin from `payform <https://github.com/jondavidjohn/payform>`_.
- Include PayPal payments.
- Add country names translations from django-countries.
  Full translation of the app for German, French and Polish.
- Change license from MIT to BSD.
- Make it a full PyPI package.

Initial release (2013-07-28)
----------------------------

Initial release by Danny Sag (molokov).


