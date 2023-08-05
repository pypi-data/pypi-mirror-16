# lektor-google-tag-manager

This plugin adds support for
[Google Tag Manager](http://www.google.com/analytics/tag-manager//) to
[Lektor CMS](https://github.com/lektor/lektor).

Once the plugin is enabled, a `generate_google_tag_manager()` function
is available to be included in target `template` which automatically
include Google Tag Manager code in final HTML files rendered by
`Lektor`.

## Basic Usage

### Enabling the Plugin

To enable the plugin add this to your project file:

```ini
[packages]
lektor-google-tag-manager = 0.1
```

### Configuring the Plugin

The plugin needs a config file with your `Google Tag Manager` code in it.

Just create a file named `google-tag-manager.ini` into `./configs`
folder in your Lektor project's base directory. And, put the
`GOOGLE_TAG_MANAGER_ID` key with target property ID of form
`GTM-XXXXXX` which you obtained from:

```ini
GOOGLE_TAG_MANAGER_ID = GTM-XXXXXX
```

### Using in Templates

Now you can add a Google Tag Manager code-snippet in your templates by
just calling the `generate_google_tag_manager` function in its <body>
</body> tag as below.

```html
<div class="gtm-script">{{ generate_google_tag_manager() }}</div>
```

That's it. All the `HTML` files that rendered from that template will
include Google Tag Manager code automatically.

## License

This plugin is released under the BSD license. For more information
read the [License](https://opensource.org/licenses/BSD-3-Clause).

## Acknowledgements

This plugin is inspired by
[lektor-google-analytics](//github.com/kmonsoor/lektor-google-analytics).
