# Human review workflow

A review case contains the original request, agent output, cited evidence, calculator inputs/results, risk flags, escalation reason, model/configuration identifiers, and an immutable reference to preceding audit events.

The reviewer should be able to accept the support output, modify it, reject it, or request more information. The interface should never collapse "AI suggestion" and "human decision" into a single field.

## Queue priorities

Suggested priority signals include safety/security incidents, policy conflict, material financial impact, low evidence confidence, sensitive-data involvement, suspected fraud, and approaching service-level deadlines. Priority is operational triage, not a substitute for reviewer authority.

## Overrides

Human overrides are expected in a governed system and should be measurable. Capture structured reason categories and free-text notes so evaluation can distinguish model failure, missing evidence, policy nuance, data error, changed business rules, and reviewer preference.
