# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
"""
Events:
	always
	daily
	monthly
	weekly
"""

<<<<<<< HEAD
# imports - standard imports
=======
import datetime
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
import os
import random
import time
from typing import NoReturn

<<<<<<< HEAD
from croniter import CroniterBadCronError

# imports - module imports
import frappe
from frappe.utils import cint, get_datetime, get_sites, now_datetime
from frappe.utils.background_jobs import set_niceness

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
=======
import setproctitle
from croniter import CroniterBadCronError
from filelock import FileLock, Timeout

import frappe
from frappe.utils import cint, get_bench_path, get_datetime, get_sites, now_datetime
from frappe.utils.background_jobs import set_niceness
from frappe.utils.caching import redis_cache

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULT_SCHEDULER_TICK = 4 * 60
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)


def cprint(*args, **kwargs):
	"""Prints only if called from STDOUT"""
	try:
		os.get_terminal_size()
		print(*args, **kwargs)
	except Exception:
		pass


<<<<<<< HEAD
=======
def _proctitle(message):
	setproctitle.setthreadtitle(f"frappe-scheduler: {message}")


>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
def start_scheduler() -> NoReturn:
	"""Run enqueue_events_for_all_sites based on scheduler tick.
	Specify scheduler_interval in seconds in common_site_config.json"""

	tick = get_scheduler_tick()
	set_niceness()

<<<<<<< HEAD
	while True:
		time.sleep(tick)
		enqueue_events_for_all_sites()


def enqueue_events_for_all_sites() -> None:
	"""Loop through sites and enqueue events that are not already queued"""

	if os.path.exists(os.path.join(".", ".restarting")):
		# Don't add task to queue if webserver is in restart mode
		return

=======
	lock_path = os.path.abspath(os.path.join(get_bench_path(), "config", "scheduler_process"))

	try:
		lock = FileLock(lock_path)
		lock.acquire(blocking=False)
	except Timeout:
		frappe.logger("scheduler").debug("Scheduler already running")
		return

	while True:
		_proctitle("idle")
		time.sleep(sleep_duration(tick))
		enqueue_events_for_all_sites()


def sleep_duration(tick):
	if tick != DEFAULT_SCHEDULER_TICK:
		# Assuming user knows what they want.
		return tick

	# Sleep until next multiple of tick.
	# This makes scheduler aligned with real clock,
	# so event scheduled at 12:00 happen at 12:00 and not 12:00:35.
	minutes = tick // 60
	now = datetime.datetime.now(datetime.timezone.utc)
	left_minutes = minutes - now.minute % minutes
	next_execution = now.replace(second=0) + datetime.timedelta(minutes=left_minutes)

	return (next_execution - now).total_seconds()


def enqueue_events_for_all_sites() -> None:
	"""Loop through sites and enqueue events that are not already queued"""

>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	with frappe.init_site():
		sites = get_sites()

	# Sites are sorted in alphabetical order, shuffle to randomize priorities
	random.shuffle(sites)

	for site in sites:
		try:
			enqueue_events_for_site(site=site)
		except Exception:
			frappe.logger("scheduler").debug(f"Failed to enqueue events for site: {site}", exc_info=True)


def enqueue_events_for_site(site: str) -> None:
	def log_exc():
		frappe.logger("scheduler").error(f"Exception in Enqueue Events for Site {site}", exc_info=True)

	try:
<<<<<<< HEAD
		frappe.init(site=site)
=======
		_proctitle(f"scheduling events for {site}")
		frappe.init(site)
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
		frappe.connect()
		if is_scheduler_inactive():
			return

<<<<<<< HEAD
		enqueue_events(site=site)
=======
		enqueue_events()
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)

		frappe.logger("scheduler").debug(f"Queued events for site {site}")
	except Exception as e:
		if frappe.db.is_access_denied(e):
			frappe.logger("scheduler").debug(f"Access denied for site {site}")
		log_exc()

	finally:
		frappe.destroy()


<<<<<<< HEAD
def enqueue_events(site: str) -> list[str] | None:
	if schedule_jobs_based_on_activity():
		enqueued_jobs = []
		for job_type in frappe.get_all("Scheduled Job Type", filters={"stopped": 0}, fields="*"):
=======
def enqueue_events() -> list[str] | None:
	if schedule_jobs_based_on_activity():
		enqueued_jobs = []
		all_jobs = frappe.get_all("Scheduled Job Type", filters={"stopped": 0}, fields="*")
		random.shuffle(all_jobs)
		for job_type in all_jobs:
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
			job_type = frappe.get_doc(doctype="Scheduled Job Type", **job_type)
			try:
				if job_type.enqueue():
					enqueued_jobs.append(job_type.method)
			except CroniterBadCronError:
				frappe.logger("scheduler").error(
					f"Invalid Job on {frappe.local.site} - {job_type.name}", exc_info=True
				)

		return enqueued_jobs


def is_scheduler_inactive(verbose=True) -> bool:
	if frappe.local.conf.maintenance_mode:
		if verbose:
			cprint(f"{frappe.local.site}: Maintenance mode is ON")
		return True

	if frappe.local.conf.pause_scheduler:
		if verbose:
			cprint(f"{frappe.local.site}: frappe.conf.pause_scheduler is SET")
		return True

	if is_scheduler_disabled(verbose=verbose):
		return True

	return False


def is_scheduler_disabled(verbose=True) -> bool:
	if frappe.conf.disable_scheduler:
		if verbose:
			cprint(f"{frappe.local.site}: frappe.conf.disable_scheduler is SET")
		return True

	scheduler_disabled = not frappe.utils.cint(
		frappe.db.get_single_value("System Settings", "enable_scheduler")
	)
	if scheduler_disabled:
		if verbose:
			cprint(f"{frappe.local.site}: SystemSettings.enable_scheduler is UNSET")
	return scheduler_disabled


def toggle_scheduler(enable):
	frappe.db.set_single_value("System Settings", "enable_scheduler", int(enable))


def enable_scheduler():
	toggle_scheduler(True)


def disable_scheduler():
	toggle_scheduler(False)


<<<<<<< HEAD
def schedule_jobs_based_on_activity(check_time=None):
	"""Returns True for active sites defined by Activity Log
	Returns True for inactive sites once in 24 hours"""
	if is_dormant(check_time=check_time):
		# ensure last job is one day old
		last_job_timestamp = _get_last_modified_timestamp("Scheduled Job Log")
=======
@redis_cache(ttl=60 * 60)
def schedule_jobs_based_on_activity(check_time=None):
	"""Return True for active sites as defined by `Activity Log`.
	Also return True for inactive sites once every 24 hours based on `Scheduled Job Log`."""
	if is_dormant(check_time=check_time):
		# ensure last job is one day old
		last_job_timestamp = _get_last_creation_timestamp("Scheduled Job Log")
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
		if not last_job_timestamp:
			return True
		else:
			if ((check_time or now_datetime()) - last_job_timestamp).total_seconds() >= 86400:
				# one day is passed since jobs are run, so lets do this
				return True
			else:
				# schedulers run in the last 24 hours, do nothing
				return False
	else:
		# site active, lets run the jobs
		return True


def is_dormant(check_time=None):
	# Assume never dormant if developer_mode is enabled
	if frappe.conf.developer_mode:
		return False
<<<<<<< HEAD
	last_activity_log_timestamp = _get_last_modified_timestamp("Activity Log")
=======
	last_activity_log_timestamp = _get_last_creation_timestamp("Activity Log")
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	since = (frappe.get_system_settings("dormant_days") or 4) * 86400
	if not last_activity_log_timestamp:
		return True
	if ((check_time or now_datetime()) - last_activity_log_timestamp).total_seconds() >= since:
		return True
	return False


<<<<<<< HEAD
def _get_last_modified_timestamp(doctype):
	timestamp = frappe.db.get_value(doctype, filters={}, fieldname="modified", order_by="modified desc")
=======
def _get_last_creation_timestamp(doctype):
	timestamp = frappe.db.get_value(doctype, filters={}, fieldname="creation", order_by="creation desc")
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	if timestamp:
		return get_datetime(timestamp)


@frappe.whitelist()
def activate_scheduler():
	from frappe.installer import update_site_config

	frappe.only_for("Administrator")

	if frappe.local.conf.maintenance_mode:
		frappe.throw(frappe._("Scheduler can not be re-enabled when maintenance mode is active."))

	if is_scheduler_disabled():
		enable_scheduler()
	if frappe.conf.pause_scheduler:
		update_site_config("pause_scheduler", 0)


@frappe.whitelist()
def get_scheduler_status():
	if is_scheduler_inactive():
		return {"status": "inactive"}
	return {"status": "active"}


def get_scheduler_tick() -> int:
<<<<<<< HEAD
	return cint(frappe.get_conf().scheduler_tick_interval) or 60
=======
	conf = frappe.get_conf()
	return cint(conf.scheduler_tick_interval) or DEFAULT_SCHEDULER_TICK
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
