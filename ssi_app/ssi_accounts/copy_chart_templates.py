"""按需复制科目表模板 JSON 至 ERPNext ``verified`` 目录（不使用安装钩子）。

模板放置目录（本 App 内）：``ssi_app/chart_of_accounts/custom/*.json``

目标目录（与 ERPNext v16 约定一致）：
``erpnext/accounts/doctype/account/chart_of_accounts/verified/``

在 bench 根目录执行::

	bench --site <站点名> execute ssi_app.ssi_accounts.copy_chart_templates.copy_chart_templates
	bench --site <站点名> execute ssi_app.ssi_accounts.copy_chart_templates.copy_chart_templates \\
		--kwargs "{'dry_run': True}"

可选：按本 App ``custom`` 目录中的文件名，删除 ERPNext ``verified`` 内同名 JSON
（若你已清空 ``custom``，请先备份文件名再执行，或手工删 ``verified`` 内对应 JSON）::

	bench --site <站点名> execute ssi_app.ssi_accounts.copy_chart_templates.remove_templates_from_erpnext
"""

from __future__ import annotations

import os
import shutil
from typing import Any

import frappe


def _paths() -> tuple[str, str]:
	source = frappe.get_app_path("ssi_app", "chart_of_accounts", "custom")
	target = frappe.get_app_path(
		"erpnext", "accounts", "doctype", "account", "chart_of_accounts", "verified"
	)
	return source, target


def copy_chart_templates(*, dry_run: bool = False) -> dict[str, Any]:
	"""将 ``chart_of_accounts/custom`` 下所有 ``.json`` 复制到 ERPNext ``verified``。

	若目标已存在同名文件，先删除再复制（与常见 cos 实现一致）。
	"""
	source_dir, target_dir = _paths()
	out: dict[str, Any] = {
		"dry_run": dry_run,
		"source_dir": source_dir,
		"target_dir": target_dir,
		"copied": [],
		"skipped": [],
		"errors": [],
	}

	if not os.path.isdir(source_dir):
		out["errors"].append(f"源目录不存在: {source_dir}")
		return out

	json_files = sorted(f for f in os.listdir(source_dir) if f.endswith(".json"))
	if not json_files:
		out["skipped"].append("custom 目录下无 .json 文件")
		return out

	if not dry_run and not os.path.isdir(target_dir):
		out["errors"].append(f"目标目录不存在: {target_dir}")
		return out

	for name in json_files:
		src = os.path.join(source_dir, name)
		dst = os.path.join(target_dir, name)
		try:
			if dry_run:
				out["copied"].append({"file": name, "would_copy_to": dst})
				continue
			if os.path.exists(dst):
				os.remove(dst)
			shutil.copy2(src, dst)
			out["copied"].append({"file": name, "dst": dst})
		except Exception as e:
			msg = f"{name}: {e!s}"
			out["errors"].append(msg)
			frappe.log_error(message=msg, title="SSI copy_chart_templates")

	return out


def remove_templates_from_erpnext(*, dry_run: bool = False) -> dict[str, Any]:
	"""按 ``custom`` 目录中出现的文件名，删除 ERPNext ``verified`` 内同名 JSON。"""
	source_dir, target_dir = _paths()
	out: dict[str, Any] = {
		"dry_run": dry_run,
		"source_dir": source_dir,
		"target_dir": target_dir,
		"removed": [],
		"not_found": [],
		"errors": [],
	}

	if not os.path.isdir(source_dir):
		out["errors"].append(f"源目录不存在: {source_dir}")
		return out

	json_files = sorted(f for f in os.listdir(source_dir) if f.endswith(".json"))
	if not json_files:
		out["not_found"].append("custom 目录下无 .json，无可核对文件名")
		return out

	for name in json_files:
		dst = os.path.join(target_dir, name)
		if not os.path.exists(dst):
			out["not_found"].append(name)
			continue
		try:
			if dry_run:
				out["removed"].append({"file": name, "would_remove": dst})
			else:
				os.remove(dst)
				out["removed"].append({"file": name, "dst": dst})
		except Exception as e:
			msg = f"{name}: {e!s}"
			out["errors"].append(msg)
			frappe.log_error(message=msg, title="SSI remove_chart_templates")

	return out
