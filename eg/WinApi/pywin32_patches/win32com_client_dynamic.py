# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2019 EventGhost Project <http://www.eventghost.org/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

# Patch to fix an incorrect return in pywin32.
# Example would be the speech plugin. when setting the attribute
# Voice or AudioOutput a traceback would occur. This "Monkey Patch" resolves
# that issue

import pythoncom


def GetDescInvokeType(entry, invoke_type):
    if not entry or not entry.desc:
        return invoke_type
    varkind = entry.desc[4]
    if (
        varkind == pythoncom.VAR_DISPATCH and
        invoke_type == pythoncom.INVOKE_PROPERTYGET
    ):
        return pythoncom.INVOKE_FUNC | invoke_type
    else:
        return varkind

