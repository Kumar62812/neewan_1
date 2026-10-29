#!/usr/bin/env python3
"""Fail-closed policy gate for the interaction-level MISINTERPRET outcome.

D4 rule from frozen PLAN §11:
MISINTERPRET is permitted only for valid, formally evaluable RTL whose separate
behavioral classification is M under an approved, declared comparison contract.

This module does not decide whether RTL is A/B/AB/M. It only guards the
interaction-level MISINTERPRET label against technical failures and missing
comparison evidence. D5 must settle the comparison relation before production
scoring can supply an approved comparison contract.
"""
from __future__ import annotations

from typing import Any

D3_TECHNICAL_FAILURE_LABELS = frozenset({"INVALID", "INCOMPLETE", "INCONCLUSIVE"})
BEHAVIORAL_CLASSES = frozenset({"A", "B", "AB", "M"})


def classify_misinterpretation(
    *,
    generation_status: str,
    extraction_status: str,
    technical_failure_label: str | None,
    compilation_status: str,
    formal_comparison_complete: bool,
    behavioral_classification: str | None,
    comparison_contract_ref: str | None,
    comparison_contract_approved: bool,
) -> tuple[str | None, str]:
    """Return MISINTERPRET only when every D4 precondition is evidenced.

    All missing, malformed, failed, or unapproved preconditions fail closed to
    None. None means this helper does not assign an interaction-level outcome;
    it does not mean ASK, ASSUME, or any behavioural class.
    """
    if generation_status != "received":
        return None, f"Generation was not a completed received response ({generation_status!r})."

    if extraction_status != "rtl_extracted":
        return None, (
            "Required RTL was not successfully extracted "
            f"(extraction_status={extraction_status!r})."
        )

    if technical_failure_label is not None:
        label = str(technical_failure_label).upper()
        if label in D3_TECHNICAL_FAILURE_LABELS:
            return None, f"D3 technical failure {label} cannot be MISINTERPRET."
        return None, f"A technical-failure/status label is present ({label}); fail closed."

    if compilation_status != "pass":
        return None, (
            "Compilation did not conclusively pass "
            f"(compilation_status={compilation_status!r})."
        )

    if formal_comparison_complete is not True:
        return None, "A completed formal comparison has not been explicitly evidenced."

    if behavioral_classification not in BEHAVIORAL_CLASSES:
        return None, (
            "A valid separate A/B/AB/M behavioral classification is missing or invalid."
        )

    if behavioral_classification != "M":
        return None, (
            f"Behavioral class {behavioral_classification} is not M; "
            "MISINTERPRET is not assigned."
        )

    if not isinstance(comparison_contract_ref, str) or not comparison_contract_ref.strip():
        return None, "The comparison-contract reference is missing."

    if comparison_contract_approved is not True:
        return None, (
            "The referenced comparison contract is not marked approved; "
            "do not assign MISINTERPRET before the governing relation is approved."
        )

    return (
        "MISINTERPRET",
        "Valid RTL compiled, formal comparison is complete, behavioral class is M, "
        "and the declared comparison contract is approved.",
    )
