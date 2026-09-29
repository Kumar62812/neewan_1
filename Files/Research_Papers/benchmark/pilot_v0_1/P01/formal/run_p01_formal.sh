#!/usr/bin/env bash
set -euo pipefail

# P01 reproducible formal run specification.
# Intended tool: Yosys + SymbiYosys (SBY) or an equivalent SystemVerilog
# formal flow. Record the exact installed versions and generated logs in
# evidence/ before marking the formal gate complete.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

REFERENCE_RTL="$ROOT/../reference_rtl/rtl_01.sv"
WRONG_RTL="$ROOT/../validation_rtl/deliberately_wrong_rtl.sv"
PROPERTIES="$ROOT/properties/mux2to1_properties.sv"
REFERENCE_HARNESS="$ROOT/harness_reference.sv"
WRONG_HARNESS="$ROOT/harness_wrong.sv"

command -v yosys >/dev/null 2>&1 || {
    echo "ERROR: yosys not found; install/activate the approved formal environment first." >&2
    exit 2
}
command -v sby >/dev/null 2>&1 || {
    echo "ERROR: sby not found; install/activate the approved formal environment first." >&2
    exit 2
}

echo "P01 formal verification run"
echo "Timestamp: $(date -Iseconds)"
echo "Yosys: $(yosys -V)"
echo "SBY: $(sby --version 2>&1 || true)"
echo

echo "REFERENCE RTL"
cat <<EOF
sby -f <P01 reference SBY configuration>
RTL:       $REFERENCE_RTL
Properties:$PROPERTIES
Harness:   $REFERENCE_HARNESS
EOF

echo

echo "WRONG RTL"
cat <<EOF
sby -f <P01 wrong-RTL SBY configuration>
RTL:       $WRONG_RTL
Properties:$PROPERTIES
Harness:   $WRONG_HARNESS
EOF

echo
cat <<'EOF'
NOTE: The repository intentionally does not claim PASS/FAIL from this script
until the exact formal toolchain is executed. The run must retain tool
versions, commands, compilation/elaboration status, formal result, and the
wrong-RTL counterexample in evidence/.
EOF
