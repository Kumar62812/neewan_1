#!/usr/bin/env bash
set -u -o pipefail

# P01 reproducible formal runner.
# Toolchain: Yosys + SymbiYosys (sby) + Z3, using smtbmc z3.
# Both runs use the same mux2to1_properties.sv and Boolean-input contract.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVIDENCE="$ROOT/evidence"
mkdir -p "$EVIDENCE"

fail_missing() {
    echo "ERROR: required tool '$1' is not installed or not on PATH." >&2
    echo "Install/activate the approved Yosys + SymbiYosys + Z3 environment and rerun." >&2
    exit 2
}

command -v yosys >/dev/null 2>&1 || fail_missing yosys
command -v sby   >/dev/null 2>&1 || fail_missing sby
command -v z3    >/dev/null 2>&1 || fail_missing z3

if ! git -C "$ROOT/../../../../../.." rev-parse --show-toplevel >/dev/null 2>&1; then
    echo "ERROR: P01 runner must be executed inside a Git checkout." >&2
    exit 2
fi

REPO_ROOT="$(git -C "$ROOT/../../../../../.." rev-parse --show-toplevel)"
COMMIT_SHA="$(git -C "$REPO_ROOT" rev-parse HEAD)"
BRANCH="$(git -C "$REPO_ROOT" branch --show-current)"

{
    echo "P01 formal verification provenance"
    echo "timestamp=$(date -Iseconds)"
    echo "repository=$REPO_ROOT"
    echo "branch=$BRANCH"
    echo "commit_sha=$COMMIT_SHA"
    echo "yosys=$(yosys -V)"
    echo "sby=$(sby --version 2>&1 || true)"
    echo "z3=$(z3 --version 2>&1 || true)"
    echo "properties=$ROOT/properties/mux2to1_properties.sv"
    echo "reference_harness=$ROOT/harness_reference.sv"
    echo "wrong_harness=$ROOT/harness_wrong.sv"
    echo "reference_config=$ROOT/reference.sby"
    echo "wrong_config=$ROOT/wrong.sby"
    echo "assumptions=None beyond declared one-bit Boolean inputs"
} | tee "$EVIDENCE/provenance.txt"

echo
echo "=== REFERENCE RTL: expected PASS ==="
rm -rf "$ROOT/reference" "$ROOT/wrong"
(
    cd "$ROOT"
    sby -f reference.sby
) 2>&1 | tee "$EVIDENCE/reference.log"
REFERENCE_STATUS=${PIPESTATUS[0]}
echo "reference_sby_exit=$REFERENCE_STATUS" | tee -a "$EVIDENCE/status.txt"

if [ "$REFERENCE_STATUS" -ne 0 ]; then
    echo "ERROR: reference formal task did not complete with the configured expected PASS." >&2
    exit 3
fi

echo
echo "=== WRONG RTL: expected assertion FAIL ==="
(
    cd "$ROOT"
    sby -f wrong.sby
) 2>&1 | tee "$EVIDENCE/wrong.log"
WRONG_STATUS=${PIPESTATUS[0]}
echo "wrong_sby_exit=$WRONG_STATUS" | tee -a "$EVIDENCE/status.txt"

if [ "$WRONG_STATUS" -ne 0 ]; then
    echo "ERROR: wrong-RTL formal task did not complete with the configured expected FAIL." >&2
    exit 4
fi

cat > "$EVIDENCE/RESULTS_PENDING_REVIEW.md" <<'EOF'
# P01 Formal Evidence — Review Required

The runner completed both configured SBY tasks with their expected SBY outcomes.
Before the formal gate is marked complete, inspect the generated SBY reports and
counterexample trace to record:

- compilation/elaboration success for both designs;
- identical property module and Boolean-input contract;
- reference assertion PASS;
- wrong-RTL assertion FAIL;
- actual legal `a`, `b`, and `sel` values in the counterexample;
- expected `y` and observed `y`;
- absence of undocumented assumptions.

Do not treat a shell exit status alone as certification evidence.
EOF

echo "P01 formal tasks completed with configured expected outcomes. Inspect evidence/ before certification."
