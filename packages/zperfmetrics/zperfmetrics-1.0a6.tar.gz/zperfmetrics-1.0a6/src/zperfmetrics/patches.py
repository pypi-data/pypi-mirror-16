# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)


def _patch_diazo():
    try:
        from plone.app.theming.transform import ThemeTransform
        from perfmetrics import Metric
        from zperfmetrics import ZMetric
    except ImportError:
        logger.info('No Plone Diazo patches for zperfmetrics')
        return

    # patch to measure plone.app.theming
    logger.info('Activating Plone Diazo patches for zperfmetrics')
    ThemeTransform.setupTransform = Metric(
        stat='diazo.setup',
        method=True,
    )(
        ThemeTransform.setupTransform
    )
    ThemeTransform.transformIterable = ZMetric(
        stat='diazo.transform',
        method=True
    )(
        ThemeTransform.transformIterable
    )


def initialize(context):
    _patch_diazo()
