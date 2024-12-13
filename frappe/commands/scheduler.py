import sys

import click

import frappe
from frappe.commands import get_site, pass_context
from frappe.exceptions import SiteNotSpecifiedError
<<<<<<< HEAD
=======
from frappe.utils.bench_helper import CliCtxObj
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)


@click.command("trigger-scheduler-event", help="Trigger a scheduler event")
@click.argument("event")
@pass_context
<<<<<<< HEAD
def trigger_scheduler_event(context, event):
=======
def trigger_scheduler_event(context: CliCtxObj, event):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	import frappe.utils.scheduler

	exit_code = 0

	for site in context.sites:
		try:
<<<<<<< HEAD
			frappe.init(site=site)
=======
			frappe.init(site)
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
			frappe.connect()
			try:
				frappe.get_doc("Scheduled Job Type", {"method": event}).execute()
			except frappe.DoesNotExistError:
				click.secho(f"Event {event} does not exist!", fg="red")
				exit_code = 1
		finally:
			frappe.destroy()

	if not context.sites:
		raise SiteNotSpecifiedError

	sys.exit(exit_code)


@click.command("enable-scheduler")
@pass_context
<<<<<<< HEAD
def enable_scheduler(context):
=======
def enable_scheduler(context: CliCtxObj):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	"Enable scheduler"
	import frappe.utils.scheduler

	for site in context.sites:
		try:
<<<<<<< HEAD
			frappe.init(site=site)
=======
			frappe.init(site)
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
			frappe.connect()
			frappe.utils.scheduler.enable_scheduler()
			frappe.db.commit()
			print("Enabled for", site)
		finally:
			frappe.destroy()
	if not context.sites:
		raise SiteNotSpecifiedError


@click.command("disable-scheduler")
@pass_context
<<<<<<< HEAD
def disable_scheduler(context):
=======
def disable_scheduler(context: CliCtxObj):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	"Disable scheduler"
	import frappe.utils.scheduler

	for site in context.sites:
		try:
<<<<<<< HEAD
			frappe.init(site=site)
=======
			frappe.init(site)
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
			frappe.connect()
			frappe.utils.scheduler.disable_scheduler()
			frappe.db.commit()
			print("Disabled for", site)
		finally:
			frappe.destroy()
	if not context.sites:
		raise SiteNotSpecifiedError


@click.command("scheduler")
@click.option("--site", help="site name")
@click.argument("state", type=click.Choice(["pause", "resume", "disable", "enable", "status"]))
@click.option("--format", "-f", default="text", type=click.Choice(["json", "text"]), help="Output format")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
@pass_context
<<<<<<< HEAD
def scheduler(context, state: str, format: str, verbose: bool = False, site: str | None = None):
=======
def scheduler(context: CliCtxObj, state: str, format: str, verbose: bool = False, site: str | None = None):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	"""Control scheduler state."""
	import frappe
	from frappe.utils.scheduler import is_scheduler_inactive, toggle_scheduler

	site = site or get_site(context)

	output = {
		"text": "Scheduler is {status} for site {site}",
		"json": '{{"status": "{status}", "site": "{site}"}}',
	}

	with frappe.init_site(site=site):
		match state:
			case "status":
				frappe.connect()
				status = "disabled" if is_scheduler_inactive(verbose=verbose) else "enabled"
				return print(output[format].format(status=status, site=site))
			case "pause" | "resume":
				from frappe.installer import update_site_config

				update_site_config("pause_scheduler", state == "pause")
			case "enable" | "disable":
				frappe.connect()
				toggle_scheduler(state == "enable")
				frappe.db.commit()

		print(output[format].format(status=f"{state}d", site=site))


@click.command("set-maintenance-mode")
@click.option("--site", help="site name")
@click.argument("state", type=click.Choice(["on", "off"]))
@pass_context
<<<<<<< HEAD
def set_maintenance_mode(context, state, site=None):
=======
def set_maintenance_mode(context: CliCtxObj, state, site=None):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	"""Put the site in maintenance mode for upgrades."""
	from frappe.installer import update_site_config

	if not site:
		site = get_site(context)

	try:
<<<<<<< HEAD
		frappe.init(site=site)
=======
		frappe.init(site)
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
		update_site_config("maintenance_mode", 1 if (state == "on") else 0)

	finally:
		frappe.destroy()


@click.command("doctor")  # Passing context always gets a site and if there is no use site it breaks
@click.option("--site", help="site name")
@pass_context
<<<<<<< HEAD
def doctor(context, site=None):
=======
def doctor(context: CliCtxObj, site=None):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	"Get diagnostic info about background workers"
	from frappe.utils.doctor import doctor as _doctor

	if not site:
		site = get_site(context, raise_err=False)
	return _doctor(site=site)


@click.command("show-pending-jobs")
@click.option("--site", help="site name")
@pass_context
<<<<<<< HEAD
def show_pending_jobs(context, site=None):
=======
def show_pending_jobs(context: CliCtxObj, site=None):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	"Get diagnostic info about background jobs"
	from frappe.utils.doctor import pending_jobs as _pending_jobs

	if not site:
		site = get_site(context)

	with frappe.init_site(site):
		pending_jobs = _pending_jobs(site=site)

	return pending_jobs


@click.command("purge-jobs")
@click.option("--site", help="site name")
@click.option("--queue", default=None, help='one of "low", "default", "high')
@click.option(
	"--event",
	default=None,
	help='one of "all", "weekly", "monthly", "hourly", "daily", "weekly_long", "daily_long"',
)
def purge_jobs(site=None, queue=None, event=None):
	"Purge any pending periodic tasks, if event option is not given, it will purge everything for the site"
	from frappe.utils.doctor import purge_pending_jobs

	frappe.init(site or "")
	count = purge_pending_jobs(event=event, site=site, queue=queue)
	print(f"Purged {count} jobs")


@click.command("schedule")
def start_scheduler():
	"""Start scheduler process which is responsible for enqueueing the scheduled job types."""
<<<<<<< HEAD
	from frappe.utils.scheduler import start_scheduler

=======
	import time

	from frappe.utils.scheduler import start_scheduler

	time.sleep(0.5)  # Delayed start. TODO: find better way to handle this.
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	start_scheduler()


@click.command("worker")
@click.option(
	"--queue",
	type=str,
	help="Queue to consume from. Multiple queues can be specified using comma-separated string. If not specified all queues are consumed.",
)
@click.option("--quiet", is_flag=True, default=False, help="Hide Log Outputs")
@click.option("-u", "--rq-username", default=None, help="Redis ACL user")
@click.option("-p", "--rq-password", default=None, help="Redis ACL user password")
@click.option("--burst", is_flag=True, default=False, help="Run Worker in Burst mode.")
@click.option(
	"--strategy",
	required=False,
	type=click.Choice(["round_robin", "random"]),
	help="Dequeuing strategy to use",
)
def start_worker(queue, quiet=False, rq_username=None, rq_password=None, burst=False, strategy=None):
<<<<<<< HEAD
	"""Start a backgrond worker"""
=======
	"""Start a background worker"""
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	from frappe.utils.background_jobs import start_worker

	start_worker(
		queue,
		quiet=quiet,
		rq_username=rq_username,
		rq_password=rq_password,
		burst=burst,
		strategy=strategy,
	)


@click.command("worker-pool")
@click.option(
	"--queue",
	type=str,
	help="Queue to consume from. Multiple queues can be specified using comma-separated string. If not specified all queues are consumed.",
)
@click.option("--num-workers", type=int, default=2, help="Number of workers to spawn in pool.")
@click.option("--quiet", is_flag=True, default=False, help="Hide Log Outputs")
@click.option("--burst", is_flag=True, default=False, help="Run Worker in Burst mode.")
def start_worker_pool(queue, quiet=False, num_workers=2, burst=False):
<<<<<<< HEAD
	"""Start a backgrond worker"""
	from frappe.utils.background_jobs import start_worker_pool

	start_worker_pool(
		queue=queue,
		quiet=quiet,
		burst=burst,
		num_workers=num_workers,
	)
=======
	"""Start a pool of background workers"""
	from frappe.utils.background_jobs import start_worker_pool

	start_worker_pool(queue=queue, quiet=quiet, burst=burst, num_workers=num_workers)
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)


@click.command("ready-for-migration")
@click.option("--site", help="site name")
@pass_context
<<<<<<< HEAD
def ready_for_migration(context, site=None):
=======
def ready_for_migration(context: CliCtxObj, site=None):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	from frappe.utils.doctor import any_job_pending

	if not site:
		site = get_site(context)

	try:
<<<<<<< HEAD
		frappe.init(site=site)
=======
		frappe.init(site)
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
		pending_jobs = any_job_pending(site=site)

		if pending_jobs:
			print(f"NOT READY for migration: site {site} has pending background jobs")
			sys.exit(1)

		else:
			print(f"READY for migration: site {site} does not have any background jobs")
			return 0

	finally:
		frappe.destroy()


commands = [
	disable_scheduler,
	doctor,
	enable_scheduler,
	purge_jobs,
	ready_for_migration,
	scheduler,
	set_maintenance_mode,
	show_pending_jobs,
	start_scheduler,
	start_worker,
	start_worker_pool,
	trigger_scheduler_event,
]
