# Copyright (C) 2023 Gerard Roche
#
# This file is part of GotoDefinitionSplit.
#
# GotoDefinitionSplit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GotoDefinitionSplit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GotoDefinitionSplit.  If not, see <https://www.gnu.org/licenses/>.

import sublime_plugin


class GotoDefinitionSplit(sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('goto_definition', {
            'side_by_side': True
        })
        self.window.run_command('carry_file_to_pane', {
            'direction': 'right'
        })
