# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

from tcadmin.appconfig import AppConfig

from generate import (
    projects,
    grants,
    login_identity,
)


appconfig = AppConfig()

appconfig.generators.register(projects.update_resources)
appconfig.generators.register(grants.update_resources)
appconfig.generators.register(login_identity.update_resources)
