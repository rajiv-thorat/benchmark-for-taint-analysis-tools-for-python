from importlib.metadata import entry_points
import setuptools

setuptools.setup(
    name='if_statement',
    version='0.0.1',
    entry_points={
        'files': [
            'if_statement_rechable=if-statement.if-statement-rechable-taint:run'
        ]
    }
)