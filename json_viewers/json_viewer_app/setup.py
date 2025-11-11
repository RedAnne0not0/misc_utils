from setuptools import setup

APP = ['json_viewer_app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'app_icon.icns',
    'plist': {
        'CFBundleName': 'JSON Viewer',
        'CFBundleDisplayName': 'LLM Conversation Viewer',
        'CFBundleGetInfoString': "View LLM API conversations",
        'CFBundleIdentifier': "com.jsonviewer.app",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2025, All Rights Reserved"
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
