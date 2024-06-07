{
    'targets': [{
        'target_name': 'win_ioctl',
        'include_dirs':
        [
            '<!(node -e "require(\'nan\')")'
        ],
        'conditions':  [
            [
                "OS=='win'", {
                    'sources': ['src/main.cc'],
                }
            ],
            [
                "OS=='mac'", {
                    'sources': [
                        "<!@(node -p \"require('fs').readdirSync('./examples').map(f=>'src-mac/'+f).join(' ')\")"
                    ],
                }
            ]
        ]
    }]
}
