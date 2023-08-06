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

from ..domain import Requirement
from .. import metric


OWASP = Requirement(
    name='OWASP Top 10 2013',
    url='https://www.owasp.org/',
    metric_classes={metric.HighPriorityOWASPDependencyWarnings, metric.NormalPriorityOWASPDependencyWarnings})

OWASP_ZAP = Requirement(
    name='OWASP Top 10 2013',
    url='https://www.owasp.org/',
    metric_classes={metric.HighRiskZAPScanAlertsMetric, metric.MediumRiskZAPScanAlertsMetric})

TRUSTED_PRODUCT_MAINTAINABILITY = Requirement(
    name='Trusted Product Maintainability, version 6.1',
    url='http://www.sig.eu/nl/diensten/Software%20Product%20Certificering/Evaluation%20Criteria/',
    metric_classes={metric.TotalLOC})

UNITTESTS = Requirement(
    name='Unit and/or integration tests',
    metric_classes={metric.FailingUnittests, metric.UnittestLineCoverage, metric.UnittestBranchCoverage,
                    metric.IntegrationtestLineCoverage, metric.IntegrationtestBranchCoverage,
                    metric.UnitAndIntegrationTestLineCoverage, metric.UnitAndIntegrationTestBranchCoverage})

ART = Requirement(
    name='Automated regression tests',
    metric_classes={metric.FailingRegressionTests, metric.RegressionTestAge})

ART_COVERAGE = Requirement(
    name='Automated regression test coverage',
    metric_classes={metric.ARTStatementCoverage, metric.ARTBranchCoverage})

CODE_QUALITY = Requirement(
    name='Code quality',
    metric_classes={metric.BlockerViolations, metric.CriticalViolations, metric.MajorViolations,
                    metric.CyclomaticComplexity, metric.CyclicDependencies, metric.JavaDuplication,
                    metric.ProductLOC, metric.LongMethods, metric.ManyParameters, metric.CommentedLOC,
                    metric.NoSonar, metric.FalsePositives, metric.SonarAnalysisAge})

JSF_CODE_QUALITY = Requirement(
    name='JSF code quality',
    metric_classes={metric.JsfDuplication, metric.ProductLOC})

PERFORMANCE = Requirement(
    name='Performance',
    metric_classes={metric.ResponseTimes})

# FIXME: There shouldn't be a separate Ymor performance requirement, but before we can fix that, the ResponseTimes and
# YmorResponseTimes metrics need to be merged.
PERFORMANCE_YMOR = Requirement(
    name='Performance (Ymor)',
    metric_classes={metric.YmorResponseTimes})

NO_SNAPSHOT_DEPENDENCIES = Requirement(
    name='No snapshot dependencies',
    metric_classes={metric.SnapshotDependencies})
