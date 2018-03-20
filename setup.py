from setuptools import setup, find_packages

setup(
    name             = 'webcam',
    version          = '1.0',
    description      = 'Python wrapper for liquibase',
    author           = 'kim chang hoi',
    author_email     = 'kopr3963@me.com',
    url              = 'https://github.com/kopr3963/tkinter',
    download_url     = 'https://kopr3963.co.kr/download_list',
    install_requires = [ ],
    packages         = find_packages(exclude = ['docs', 'tests*']),
    keywords         = ['liquibase', 'db migration'],
    python_requires  = '>=2',
    package_data     =  {
        'pyquibase' : [
            'db-connectors/sqlite-jdbc-3.18.0.jar',
            'db-connectors/mysql-connector-java-5.1.42-bin.jar',
            'liquibase/liquibase.jar'
    ]},
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 2.7'
    ]
)