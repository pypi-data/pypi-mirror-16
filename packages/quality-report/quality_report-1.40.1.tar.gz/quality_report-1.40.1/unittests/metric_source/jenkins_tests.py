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

import io
import datetime
import unittest
import urllib2

from qualitylib.metric_source import Jenkins, JenkinsOWASPDependencyReport


def to_jenkins_timestamp(date_time, epoch=datetime.datetime(1970, 1, 1)):
    """ Convert datetime instance to *milli*seconds since epoch. """
    delta = date_time - epoch
    return (delta.microseconds + (delta.seconds + delta.days * 24 * 3600) * 10**6) / 1000


class JenkinsUnderTest(Jenkins):  # pylint: disable=too-few-public-methods
    """ Override the url_open method to return a fixed HTML fragment. """
    contents = u'{"jobs": []}'

    def url_open(self, url):  # pylint: disable=unused-argument
        """ Return the static content. """
        return io.StringIO(self.contents)


class JenkinsTest(unittest.TestCase):
    """ Unit tests for the Jenkins class. """

    def setUp(self):
        self.__jenkins = JenkinsUnderTest('http://jenkins/', 'username', 'password')

    def test_url(self):
        """ Test the Jenkins url. """
        self.assertEqual('http://jenkins/', self.__jenkins.url())

    def test_no_failing_jobs(self):
        """ Test the number of failing jobs when there are no failing jobs. """
        self.assertEqual({}, self.__jenkins.failing_jobs_url())

    def test_one_failing_job(self):
        """ Test the failing jobs with one failing job. """
        date_time = datetime.datetime(2013, 4, 1, 12, 0, 0)
        self.__jenkins.contents = u'{"jobs": [{"name": "job1", "color": "red", "description": "", ' \
                                  u'"url": "http://url", "buildable": True}], "timestamp": "%s", "builds": [{}]}' % \
                                  to_jenkins_timestamp(date_time)
        expected_days_ago = (datetime.datetime.utcnow() - date_time).days
        self.assertEqual({'job1 (%d dagen)' % expected_days_ago: 'http://url'}, self.__jenkins.failing_jobs_url())

    def test_ignore_disable_job(self):
        """ Test that disabled failing jobs are ignored. """
        self.__jenkins.contents = u'{"jobs": [{"name": "job1", "color": "red", "description": "", ' \
                                  u'"url": "http://url", "buildable": False}], "builds": [{}]}'
        self.assertEqual({}, self.__jenkins.failing_jobs_url())

    def test_ignore_pipeline_job(self):
        """ Test that pipleine jobs without buildable flag are ignored. """
        self.__jenkins.contents = u'{"jobs": [{"name": "job1", "color": "red", "description": "", ' \
                                  u'"url": "http://url"}], "builds": [{}]}'
        self.assertEqual({}, self.__jenkins.failing_jobs_url())

    def test_failing_jobs_url(self):
        """ Test that the failing jobs url dictionary contains the url for the failing job. """
        timestamp = to_jenkins_timestamp(datetime.datetime.utcnow() - datetime.timedelta(days=100))
        self.__jenkins.contents = u'{"jobs": [{"name": "job1", "color": "red", "description": "", ' \
                                  u'"url": "http://url", "buildable": True}], "timestamp": "%s", "builds": [{}]}' % \
                                  timestamp
        self.assertEqual({'job1 (100 dagen)': 'http://url'}, self.__jenkins.failing_jobs_url())

    def test_failing_jobs_url_no_description(self):
        """ Test that the failing jobs url works if there are jobs without description. """
        jan_first = datetime.datetime.utcnow().replace(month=1, day=1, hour=0, minute=0, second=0)
        self.__jenkins.contents = u'{"jobs": [{"name": "job1", "color": "red", "description": None, ' \
                                  u'"url": "http://url", "buildable":  True}], "timestamp": "%s", "builds": [{}]}' % \
                                  to_jenkins_timestamp(jan_first)
        expected_days_ago = (datetime.datetime.utcnow() - jan_first).days
        self.assertEqual({'job1 (%d dagen)' % expected_days_ago: 'http://url'}, self.__jenkins.failing_jobs_url())

    def test_no_unused_jobs(self):
        """ Test the number of unused jobs when there are no unused jobs. """
        self.assertEqual({}, self.__jenkins.unused_jobs_url())

    def test_one_unused_job(self):
        """ Test the unused jobs with one unused job. """
        date_time = datetime.datetime(2000, 4, 1, 12, 0, 0)
        self.__jenkins.contents = u'{"jobs": [{"name": "job1", "color": "red", "description": "", ' \
                                  u'"url": "http://url", "buildable": True}], "timestamp": "%s"}' % \
                                  to_jenkins_timestamp(date_time)
        expected_days_ago = (datetime.datetime.utcnow() - date_time).days
        self.assertEqual({'job1 (%d dagen)' % expected_days_ago: 'http://url'}, self.__jenkins.unused_jobs_url())

    def test_unused_jobs_grace(self):
        """ Test the unused jobs with one unused job within grace time. """
        self.__jenkins.contents = u'{"jobs": [{"name": "job1", "color": "red", "description": "[gracedays=400]", ' \
                                  u'"url": "http://url", "buildable": True}], "timestamp": "%s", "builds": [{}]}' % \
                                  to_jenkins_timestamp(datetime.datetime.utcnow() - datetime.timedelta(days=100))
        self.assertEqual({}, self.__jenkins.unused_jobs_url())

    def test_unused_jobs_after_grace(self):
        """ Test the unused jobs with one unused job within grace time. """
        last_year = datetime.datetime.utcnow().year - 1
        self.__jenkins.contents = u'{"jobs": [{"name": "job1", "color": "red", "description": "[gracedays=200]", ' \
                                  u'"url": "http://url", "buildable": True}], "timestamp": "%s", "builds": [{}]}' % \
                                  to_jenkins_timestamp(datetime.datetime(last_year, 1, 1, 12, 0, 0))
        expected_days_ago = (datetime.datetime.utcnow() - datetime.datetime(last_year, 1, 1, 12, 0, 0)).days
        self.assertEqual({'job1 (%d dagen)' % expected_days_ago: 'http://url'}, self.__jenkins.unused_jobs_url())

    def test_nr_of_active_jobs(self):
        """ Test the number of active jobs. """
        self.assertEqual(0, self.__jenkins.number_of_active_jobs())

    def test_unstable_arts_none(self):
        """ Test the number of unstable ARTs. """
        self.__jenkins.contents = u'{"jobs": []}'
        self.assertEqual({}, self.__jenkins.unstable_arts_url('projects', 21))

    def test_unstable_arts_one_just(self):
        """ Test the number of unstable ARTs with one that just became
            unstable. """
        hour_ago = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
        self.__jenkins.contents = u'{"jobs": [{"name": "job-a"}], "timestamp": "%s"}' % to_jenkins_timestamp(hour_ago)
        self.assertEqual({}, self.__jenkins.unstable_arts_url('job-a', 3))

    def test_unstable_arts_one(self):
        """ Test the number of unstable ARTs. """
        week_ago = datetime.datetime.utcnow() - datetime.timedelta(days=7)
        self.__jenkins.contents = u'{"jobs": [{"name": "job-a"}], "timestamp": "%s"}' % to_jenkins_timestamp(week_ago)
        self.assertEqual({'job-a (7 dagen)': 'http://jenkins/job/job-a/'}, self.__jenkins.unstable_arts_url('job-a', 3))

    def test_unstable_art_old_age(self):
        """ Test the unstable ART url for a build with a very old age. """
        date_time = datetime.datetime(2000, 1, 1, 0, 0, 0)
        self.__jenkins.contents = u'{"jobs": [{"name": "job-a"}], "timestamp": "%s"}' % to_jenkins_timestamp(date_time)
        expected_days = (datetime.datetime.utcnow() - date_time).days
        self.assertEqual({'job-a (%s dagen)' % expected_days: 'http://jenkins/job/job-a/'},
                         self.__jenkins.unstable_arts_url('job-a', 3))

    def test_unstable_art_key_error(self):
        """ Test the unstable ART url when a HTTP error occurs. """
        self.__jenkins.contents = u'{"jobs": [{"name": "job-a"}]}'
        self.assertEqual({'job-a (? dagen)': 'http://jenkins/job/job-a/'}, self.__jenkins.unstable_arts_url('job-a', 3))

    def test_resolve_job_name(self):
        """ Test that a job name that is a regular expression is resolved. """
        self.__jenkins.contents = u'{"jobs": [{"name": "job5"}]}'
        self.assertEqual('job5', self.__jenkins.resolve_job_name('job[0-9]$'))

    def test_resolve_job_name_with_partial_match(self):
        """ Test that a job name that is a regular expression is resolved,
            even when it partially matches another job. """
        self.__jenkins.contents = u'{"jobs": [{"name": "job50"}, {"name": "job5"}]}'
        self.assertEqual('job5', self.__jenkins.resolve_job_name('job[0-9]'))


class JenkinsOWASPDependencyReportUnderTest(JenkinsOWASPDependencyReport):  # pylint: disable=too-few-public-methods
    """ Override the url_open method to return a fixed HTML fragment. """
    contents = u'{"jobs": []}'

    def url_open(self, url):  # pylint: disable=unused-argument
        """ Return the static contents or raise an exception. """
        if 'raise' in self.contents:
            raise urllib2.HTTPError(None, None, None, None, None)
        else:
            return io.StringIO(self.contents)


class JenkinsOWASPDependencyReportTest(unittest.TestCase):
    """ Unit tests for the Jenkins OWASP dependency report class. """
    def setUp(self):
        self.__jenkins = JenkinsOWASPDependencyReportUnderTest('http://jenkins/', 'username', 'password')

    def test_high_priority_warnings(self):
        """ Test retrieving high priority warnings. """
        self.__jenkins.contents = u'{"numberOfHighPriorityWarnings":2}'
        self.assertEqual(2, self.__jenkins.nr_warnings(['job'], 'high'))

    def test_normal_priority_warnings(self):
        """ Test retrieving normal priority warnings. """
        self.__jenkins.contents = u'{"numberOfNormalPriorityWarnings":4}'
        self.assertEqual(4, self.__jenkins.nr_warnings(['job'], 'normal'))

    def test_low_priority_warnings(self):
        """ Test retrieving low priority warnings. """
        self.__jenkins.contents = u'{"numberOfLowPriorityWarnings":9}'
        self.assertEqual(9, self.__jenkins.nr_warnings(['job'], 'low'))

    def test_url(self):
        """ Test the url for a OWASP dependency report. """
        self.assertEqual('http://jenkins/job/job_name/lastSuccessfulBuild/dependency-check-jenkins-pluginResult/',
                         self.__jenkins.report_url('job_name'))

    def test_http_error(self):
        """ Test that the default is returned when a HTTP error occurs. """
        self.__jenkins.contents = 'raise'
        self.assertEqual(-1, self.__jenkins.nr_warnings(['job'], 'normal'))
