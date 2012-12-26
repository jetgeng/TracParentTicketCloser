# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='ParentTicketCloser',
    version='0.1.0',
    keywords='trac plugin ticket',
    author='Jet Geng',
    author_email='jetgeng@gmail.com',
    description='Trac Sub-Ticket Closer',
    long_description="""
    当TracSubTicketsPlugin 的所有的子任务都关闭是。同时关闭他的父亲。
    """,
    license = 'EPL',
    #还要去依赖SubTicket
    install_requires = ['Trac >= 0.12dev', 'TracSubTicketsPlugin >= 0.2.0'],
    packages=find_packages(exclude=['*.tests*']),
    entry_points = {
        'trac.plugins': [
            'ParentTicketCloser.api=org.gunn.trac.TicketCloser',
        ],
    },
)
