#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Georges Toth (c) 2014 <georges@trypill.org>
#
# python-openhab is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-openhab is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-openhab.  If not, see <http://www.gnu.org/licenses/>.
#


import datetime
import openhab
from openhab import Item


base_url = 'http://localhost:8080/rest'


# fetch all items
items = openhab.fetch_all_items(base_url)


# fetch other items, show how to toggle a switch
sunset = items.get('Sunset')
sunrise = items.get('Sunrise')
knx_day_night = items.get('KNX_day_night')

now = datetime.datetime.now()

if now > sunrise.state and now < sunset.state:
  knx_day_night.on()
else:
  knx_day_night.off()

print knx_day_night.state
