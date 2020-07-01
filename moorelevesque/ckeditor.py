CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat', 'CodeSnippet']},
             {'name': 'insert',
              'items': ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
              {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-',]},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},

        ],
        'toolbar': 'YourCustomToolbarConfig',
        'width': '100%',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'codesnippet',
            'uploadimage',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}

CKEDITOR_UPLOAD_PATH = "static/images/"
