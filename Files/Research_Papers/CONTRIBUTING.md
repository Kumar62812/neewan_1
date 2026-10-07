# Contributing to FORMAL-AMBIG-RTL

## Scope

Contributions are welcome when they improve literature evidence, benchmark quality, formal reproducibility, annotation quality, or experimental transparency.

The repository is a research record. Convenience changes must not compromise provenance.

## Literature

When adding a paper:

1. Prefer the primary paper/source.
2. Add complete bibliographic metadata.
3. Add a row to `literature/literature_matrix.csv`.
4. Place the PDF in the appropriate topical folder when redistribution is permitted.
5. Record DOI/arXiv/publisher information where available.
6. State "Not reported" when the paper does not provide evidence for a matrix field.
7. Do not turn literature summaries into rankings.

## Benchmark instances

Every instance must:

- have a stable ID;
- use the metadata template;
- preserve the exact original requirement wording;
- record provenance;
- document both interpretations;
- preserve the rationale for each interpretation;
- keep reference RTL separate from generated RTL;
- pass the formal and annotation protocol before being labeled certified;
- preserve rejected/negative candidates rather than deleting them.

Do not add a benchmark case because it produces a convenient LLM result.

## RTL

Reference RTL:

- must correspond to the documented interpretation;
- must compile/elaborate;
- must use the declared interface;
- must be stored with its provenance;
- must not be silently changed after formal certification.

Generated RTL:

- must retain the raw model output;
- must never overwrite the raw output after repair;
- manual repair must be stored separately and explicitly labeled.

## Formal artifacts

Every reported formal result should be reproducible from:

- RTL;
- harness;
- assumptions;
- command/script;
- tool/version;
- backend;
- resource limits.

Counterexamples should be retained for reported non-equivalence results.

Do not convert timeout or inconclusive results into success/failure without documented justification.

## Annotations

- Follow the current annotation protocol.
- Keep annotators blinded to model outcomes where required.
- Preserve raw responses and coded responses.
- Store anonymized annotator identifiers.
- Do not modify individual responses to improve agreement.
- Record adjudication separately.

## Prompts and model outputs

Store:

- exact prompt template;
- prompt version/hash;
- model name/version;
- sampling settings;
- seed when supported;
- maximum output settings;
- raw response;
- extraction procedure.

Do not publish credentials, API keys, private data, or secrets.

## Results

Results must be generated from versioned raw data and scripts.

Do not manually edit a result table to improve a metric.

Every reported metric should have:

- numerator/denominator;
- benchmark version;
- model/condition;
- statistical method where applicable.

## Protocol changes

Substantive changes to certification rules, thresholds, metrics, benchmark inclusion, or formal assumptions require a protocol amendment.

Never rewrite historical results to make them appear to have been produced under a later protocol.

## Commit guidance

Prefer focused commits with descriptive messages, for example:

- `Add benchmark schema and validation protocol`
- `Add formal certification harness for FSM reset cases`
- `Add blinded annotation batch`
- `Add reproducible LLM evaluation script`

Do not commit temporary tool outputs, secrets, or large generated artifacts unless they are explicitly part of the reproducibility package.
