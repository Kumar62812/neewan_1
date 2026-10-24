"""Extraction function retained verbatim from the frozen local recorder."""
import re
def extract(raw):
    blocks=re.findall(r'```(?:systemverilog|verilog|sv)\s*\n(.*?)```',raw,re.S|re.I)
    if len(blocks)!=1:return None,'Exactly one HDL block required'
    rtl=blocks[0]
    if re.search(r'\b(?:assume|assert|cover|restrict)\b|\$(?:any|all)(?:seq|const)|\(\*|`',rtl):
        return None,'Formal constructs, attributes or preprocessing directives are ineligible'
    return rtl,''
