{
    'targets': [{
        'target_name': 'win_ioctl',
        'conditions': [
            [
                'OS=="win"', {
                    'sources': ['src/main.cc' ],
                    'include_dirs':
                    [
                        '<!(node -e "require(\'nan\')")'
                    ],
                }
            ],
            [
                'OS=="mac"', {
                    'sources': ['LICENSE' ],
                }
            ]
        ],
    }]
} # type: ignore
