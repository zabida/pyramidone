from setuptools import setup

requires = [
    'pyramid',
    'Waitress',
]


setup(name='tutorial',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
)