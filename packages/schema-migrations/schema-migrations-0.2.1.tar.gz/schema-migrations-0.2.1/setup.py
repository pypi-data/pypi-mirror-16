from setuptools import setup

setup(
    name='schema-migrations',
    use_scm_version=True,
    packages=['schema_migrations'],
    url='https://github.com/dmonroy/schema-migrations',
    license='MIT License',
    author='Darwin Monroy',
    author_email='contact@darwinmonroy.com',
    description='PostgreSQL Schema Migrations',
    install_requires=[
        'psycopg2',
        'pyyaml',
    ],
    setup_requires=[
        'setuptools_scm',
    ]
)
