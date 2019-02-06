from setuptools import setup

setup(
    name="log_tools",
    version="0.1",
    entry_points={
        'console_scripts': [
            'parse_logs=parse_logs:main',
        ],
    },
)
