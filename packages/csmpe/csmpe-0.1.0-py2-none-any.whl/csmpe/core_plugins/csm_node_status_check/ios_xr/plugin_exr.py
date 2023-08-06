# =============================================================================
# asr9k
#
# Copyright (c)  2016, Cisco Systems
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
# =============================================================================


import re

from csmpe.plugins import CSMPlugin


class Plugin(CSMPlugin):
    """This plugin checks the states of all nodes"""
    name = "Node Status Check Plugin"
    platforms = {'NCS6K'}
    phases = {'Pre-Upgrade', 'Post-Upgrade'}

    def _parse_show_platform(self, output):
        inventory = {}
        lines = output.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 0 and line[0].isdigit():
                states = re.split('\s\s+', line)
                if not re.search('CPU\d+$', states[0]):
                    continue
                node, node_type, state, admin_state, config_state = states
                entry = {
                    'type': node_type,
                    'state': state,
                    'admin_state':admin_state,
                    'config_state': config_state
                }
                inventory[node] = entry
        return inventory

    def run(self):
        """
        Platform: NCS6K
        sysadmin-vm:0_RP0:NCS-Deploy2# show platform
        Mon May  16 21:41:08.690 UTC
        Location  Card Type               HW State      SW State      Config State
        ----------------------------------------------------------------------------
        0/0       NC6-10X100G-M-K         OPERATIONAL   SW_INACTIVE   NSHUT
        0/2       NC6-10X100G-M-P         OPERATIONAL   OPERATIONAL   NSHUT
        0/3       NC6-60X10GE-M-S         OPERATIONAL   SW_INACTIVE   NSHUT
        0/RP0     NC6-RP                  OPERATIONAL   OPERATIONAL   NSHUT
        0/RP1     NC6-RP                  OPERATIONAL   OPERATIONAL   NSHUT
        0/FC0     NC6-FC                  OPERATIONAL   N/A           NSHUT
        0/FC1     NC6-FC                  OPERATIONAL   N/A           NSHUT
        0/FC2     NC6-FC                  OPERATIONAL   N/A           NSHUT
        0/FC3     NC6-FC                  OPERATIONAL   N/A           NSHUT
        0/CI0     NCS-CRFT                OPERATIONAL   N/A           NSHUT
        0/FT0     NC6-FANTRAY             OPERATIONAL   N/A           NSHUT
        0/PT0     NCS-DC-PWRTRAY          OPERATIONAL   N/A           NSHUT
        0/PT1     NCS-DC-PWRTRAY          OPERATIONAL   N/A           NSHUT
        0/PT2     NCS-DC-PWRTRAY          OPERATIONAL   N/A           NSHUT
        0/PT3     NCS-DC-PWRTRAY          OPERATIONAL   N/A           NSHUT
        0/PT4     NCS-DC-PWRTRAY          OPERATIONAL   N/A           NSHUT

        Platform: ASR9K-X64
        sysadmin-vm:0_RSP0# show platform
        Thu May  19 05:15:38.345 UTC
        Location  Card Type               HW State      SW State      Config State
        ----------------------------------------------------------------------------
        0/RSP0    A9K-RSP880-SE           OPERATIONAL   OPERATIONAL   NSHUT
        0/RSP1    A9K-RSP880-SE           POWERED_OFF   SW_INACTIVE   NSHUT
        """
        output = self.ctx.send("admin show platform")
        print(output)
        inventory = self._parse_show_platform(output)
        valid_state = [
            'IOS XR RUN',
            'PRESENT',
            'READY',
            'FAILED',
            'OK',
            'DISABLED',
            'UNPOWERED',
            'ADMIN DOWN',
            'OPERATIONAL',
            'NOT ALLOW ONLIN',  # This is not spelling error
        ]
        for key, value in inventory.items():
            if 'CPU' in key:
                if value['state'] not in valid_state:
                    self.ctx.warning("{}={}: {}".format(key, value, "Not in valid state for upgrade"))
                    break
        else:
            self.ctx.save_data("inventory", inventory)
            self.ctx.info("All nodes in valid state for upgrade")
            return True

        self.ctx.error("Not all nodes in correct state. Upgrade can not proceed")
