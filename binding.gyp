{
    'targets': [{
        'target_name': 'win_ioctl',
        'include_dirs':
        [
            '<!(node -e "require(\'nan\')")',
            '<!(node -e "require(\'node-addon-api\')")'
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
