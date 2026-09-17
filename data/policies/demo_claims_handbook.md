# Demo Claims Handling Handbook

This file is synthetic operational guidance used to exercise ActuaryFlow-AI.

## Intake
Capture the loss date, location, claimant role, policy identifier, narrative, alleged cause, claimed amount, and available evidence. Do not infer missing facts as true.

## Evidence
Prefer primary documents, policy wording, endorsements, photographs, invoices, adjuster reports, and verified external data. Record provenance for every retrieved passage.

## Escalation
Escalate when policy wording is ambiguous, retrieved evidence conflicts, the loss is materially above configured authority, fraud indicators are present, a sensitive attribute could affect reasoning, or model confidence is low.

## Automation boundary
The AI may summarize evidence, retrieve clauses, run approved calculations, identify inconsistencies, and draft questions. A qualified human retains authority for consequential claim and coverage decisions.
