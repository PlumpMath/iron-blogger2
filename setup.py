# Copyright 2014 Ian Denhardt <ian@zenhack.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

from setuptools import setup, find_packages
from pip.req import parse_requirements
from os import path
import uuid

req_file = path.join(path.dirname(__file__), 'requirements.txt')
reqs = [str(r.req) for r in parse_requirements(req_file, session=uuid.uuid1())]

setup(name='ironblogger',
      version='0.1',
      url='https://github.com/zenhack/iron-blogger2',
      packages=find_packages(),
      scripts=['scripts/ironblogger'],
      install_requires=reqs,
      )
