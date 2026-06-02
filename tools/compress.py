# Copyright (C) 2025 Ricardo Guzman - CA2RXU
# 
# This file is part of LoRa APRS iGate.
# 
# LoRa APRS iGate is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version.
# 
# LoRa APRS iGate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with LoRa APRS iGate. If not, see <https://www.gnu.org/licenses/>.

import gzip
import os
import datetime
Import("env")

files = [
  'data_embed/i18n.js',
  'data_embed/script.js',
  'data_embed/style.css',
  'data_embed/bootstrap.js',
  'data_embed/bootstrap.css',
  'data_embed/favicon.png',
]

# These stay raw for i18n runtime
html_file = 'data_embed/index.html'
lang_files = ['data_embed/lang_en.json', 'data_embed/lang_zh.json']

string_to_find_str = "String"
string_to_find_ver = "versionDate"

with open('src/LoRa_APRS_iGate.cpp', encoding='utf-8') as cpp_file:
  for line in cpp_file:
    if string_to_find_str in line and string_to_find_ver in line:
      start = line.find('"') + 1
      end = line.find('"', start)
      if start > 0 and end > start:
        versionDate = line[start:end]
        break

# Process HTML separately (no compression for i18n)
if html_file:
    with open(html_file, 'rb') as f:
        html_content = f.read()
    env_vars = env["BOARD"] + "<br>" + ','.join(env["BUILD_FLAGS"]).replace('-Werror -Wall,', '').replace(',-DELEGANTOTA_USE_ASYNC_WEBSERVER=1', '') + "<br>" + "Version date: " + versionDate
    current_date = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') + " UTC"
    build_info = f'{env_vars}<br>Build date: {current_date}'.encode()
    html_content = html_content.replace(b'%BUILD_INFO%', build_info)
    with open(html_file, 'wb') as f:
        f.write(html_content)

for src in files:
  out = src + ".gz"
  with open(src, 'rb') as f:
    content = f.read()
  with open(out, 'wb') as f:
    f.write(gzip.compress(content, compresslevel=9))