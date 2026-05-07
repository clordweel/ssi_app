app_name = "ssi_app"
app_title = "SSI App"
app_publisher = "SSI"
app_description = "SSI multi-module custom app"
app_email = "noreply@ssi.local"
app_license = "mit"

# Fixtures
# ------------------------------------------------------------------------------
# Frappe migrate 只会导入「本 app 包目录下 fixtures/」里的顶层 *.json（不递归子目录）。
# 见 frappe.utils.fixtures.import_fixtures — hooks 中的路径字符串不会被当作导入清单。
# 下列 hooks.fixtures 供 bench export-fixtures 使用：DocType + filters（与顶层 JSON 内容对应）。
fixtures = [
	{
		"dt": "Account Category",
		"filters": [["description", "like", "%中国准则%"]],
	},
	{
		"dt": "Financial Report Template",
		"filters": [["template_name", "=", "资产负债表（中国准则）"]],
	},
	{
		"dt": "Terms and Conditions",
		"filters": [
			[
				"name",
				"in",
				[
					"工业品采销合同补充条款",
					"采购合同条款 - POT/2026-10",
					"工业产品买卖条款 - 简易合同",
					"工业产品采购条款 - POT/2026-11",
					"销售合同条款 - SOT/2026-10",
				],
			]
		],
	},
	{
		"dt": "Print Format",
		"filters": [["module", "in", ["ssi_stock", "ssi_app", "ssi_accounts"]]],
	},
	{"dt": "Print Style", "filters": [["name", "=", "SSI 通用打印样式"]]},
	{"dt": "Letter Head", "filters": [["name", "=", "SSI 通用打印页头"]]},
]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ssi_app",
# 		"logo": "/assets/ssi_app/logo.png",
# 		"title": "SSI App",
# 		"route": "/ssi_app",
# 		"has_permission": "ssi_app.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ssi_app/css/ssi_app.css"
# app_include_js = "/assets/ssi_app/js/ssi_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/ssi_app/css/ssi_app.css"
# web_include_js = "/assets/ssi_app/js/ssi_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ssi_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ssi_app/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "ssi_app.utils.jinja_methods",
# 	"filters": "ssi_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ssi_app.install.before_install"
# after_install = "ssi_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ssi_app.uninstall.before_uninstall"
# after_uninstall = "ssi_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ssi_app.utils.before_app_install"
# after_app_install = "ssi_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ssi_app.utils.before_app_uninstall"
# after_app_uninstall = "ssi_app.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "ssi_app.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ssi_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ssi_app.tasks.all"
# 	],
# 	"daily": [
# 		"ssi_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"ssi_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ssi_app.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ssi_app.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ssi_app.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "ssi_app.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ssi_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ssi_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ssi_app.utils.before_request"]
# after_request = ["ssi_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["ssi_app.utils.before_job"]
# after_job = ["ssi_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ssi_app.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# Require all whitelisted methods to have type annotations
require_type_annotated_api_methods = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

