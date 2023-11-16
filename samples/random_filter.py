# ------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------
from microsoft.featuremanagement import FeatureFilter

import random


@FeatureFilter.alias("Sample.Random")
class RandomFilter(FeatureFilter):
    def evaluate(self, context, **kwargs):
        """Determine if the feature flag is enabled for the given context"""
        value = context.get("parameters", {}).get("Value", 0)
        if value < random.randint(0, 100):
            return True
        else:
            return False
