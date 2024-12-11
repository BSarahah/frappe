import "../lib/posthog.js";

class TelemetryManager {
	constructor() {
		this.enabled = false;

		this.project_id = frappe.boot.posthog_project_id;
		this.telemetry_host = frappe.boot.posthog_host;
		this.site_age = frappe.boot.telemetry_site_age;
<<<<<<< HEAD
=======

>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
		if (cint(frappe.boot.enable_telemetry) && this.project_id && this.telemetry_host) {
			this.enabled = true;
		}
	}

	initialize() {
		if (!this.enabled) return;
<<<<<<< HEAD
		let disable_decide = !this.should_record_session();
=======
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
		try {
			posthog.init(this.project_id, {
				api_host: this.telemetry_host,
				autocapture: false,
				capture_pageview: false,
				capture_pageleave: false,
<<<<<<< HEAD
				advanced_disable_decide: disable_decide,
=======
				advanced_disable_decide: true,
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
			});
			posthog.identify(frappe.boot.sitename);
			this.send_heartbeat();
			this.register_pageview_handler();
		} catch (e) {
			console.trace("Failed to initialize telemetry", e);
			this.enabled = false;
		}
	}

	capture(event, app, props) {
		if (!this.enabled) return;
		posthog.capture(`${app}_${event}`, props);
	}

	disable() {
		this.enabled = false;
<<<<<<< HEAD
	}

	can_enable() {
		if (cint(navigator.doNotTrack)) {
			return false;
		}
		let posthog_available = Boolean(this.telemetry_host && this.project_id);
		let sentry_available = Boolean(frappe.boot.sentry_dsn);
		return posthog_available || sentry_available;
=======
		posthog.opt_out_capturing();
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	}

	send_heartbeat() {
		const KEY = "ph_last_heartbeat";
		const now = frappe.datetime.system_datetime(true);
		const last = localStorage.getItem(KEY);

		if (!last || moment(now).diff(moment(last), "hours") > 12) {
			localStorage.setItem(KEY, now.toISOString());
			this.capture("heartbeat", "frappe", { frappe_version: frappe.boot?.versions?.frappe });
		}
	}

	register_pageview_handler() {
<<<<<<< HEAD
		if (this.site_age && this.site_age > 6) {
=======
		if (this.site_age && this.site_age > 5) {
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
			return;
		}

		frappe.router.on("change", () => {
			posthog.capture("$pageview");
		});
	}
<<<<<<< HEAD

	should_record_session() {
		let start = frappe.boot.sysdefaults.session_recording_start;
		if (!start) return;

		let start_datetime = frappe.datetime.str_to_obj(start);
		let now = frappe.datetime.now_datetime();
		// if user allowed recording only record for first 2 hours, never again.
		return frappe.datetime.get_minute_diff(now, start_datetime) < 120;
	}
=======
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
}

frappe.telemetry = new TelemetryManager();
frappe.telemetry.initialize();
