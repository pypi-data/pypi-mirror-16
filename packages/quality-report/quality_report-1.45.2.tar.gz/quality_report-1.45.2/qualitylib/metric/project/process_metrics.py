"""
Copyright 2012-2016 Ministerie van Sociale Zaken en Werkgelegenheid

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from __future__ import absolute_import

from .. import HigherIsBetterMetric
from ..metric_source_mixin import JiraMetricMixin
from ..quality_attributes import PROGRESS


class ReadyUserStoryPoints(JiraMetricMixin, HigherIsBetterMetric):
    """ Metric for measuring the number of user story points ready. """

    name = 'Hoeveelheid ready user story punten'
    unit = 'ready user story punten'
    norm_template = 'Het aantal {unit} is meer dan {target}. Minder dan {low_target} {unit} is rood.'
    template = 'Het aantal {unit} is {value}.'
    target_value = 10
    low_target_value = 20
    quality_attribute = PROGRESS

    def value(self):
        nr_points = self._jira.nr_story_points_ready()
        return -1 if nr_points in (-1, None) else nr_points

    def url(self):
        return dict() if self._missing() else {'Jira': self._jira.user_stories_ready_url()}
