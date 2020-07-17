# -*- coding: utf-8 -*-
BOT_NAME = "digishop"

SPIDER_MODULES = ["digishop.spiders"]
NEWSPIDER_MODULE = "digishop.spiders"
ROBOTSTXT_OBEY = True

SPIDERMON_ENABLED = True

EXTENSIONS = {"spidermon.contrib.scrapy.extensions.Spidermon": 500}

SPIDERMON_SPIDER_CLOSE_MONITORS = ("digishop.monitors.SpiderCloseMonitorSuite",)

#SPIDERMON_SLACK_SENDER_TOKEN = "your_sender_token"
#SPIDERMON_SLACK_SENDER_NAME = "your_sender_name"
#SPIDERMON_SLACK_RECIPIENTS = ["@yourself", "#yourprojectchannel"]

SPIDERMON_TELEGRAM_SENDER_TOKEN = '1332092371:AAE_U2etZIDvm7EHy8qLzBDaxK8C79_gGyc'
SPIDERMON_TELEGRAM_RECIPIENTS = ['616980939']

ITEM_PIPELINES = {"spidermon.contrib.scrapy.pipelines.ItemValidationPipeline": 800}
SPIDERMON_VALIDATION_MODELS = ("digishop.validators.QuoteItem",)

SPIDERMON_VALIDATION_ADD_ERRORS_TO_ITEMS = True

STATS_CLASS = (
    "spidermon.contrib.stats.statscollectors.LocalStorageStatsHistoryCollector"
)

SPIDERMON_MAX_STORED_STATS = 10  # Stores the stats of the last 10 spider execution

SPIDERMON_PERIODIC_MONITORS = {
    "digishop.monitors.PeriodicMonitorSuite": 10  # every 10 seconds
}
